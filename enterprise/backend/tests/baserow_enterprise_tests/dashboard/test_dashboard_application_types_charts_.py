import json
from decimal import Decimal
from typing import cast

from django.contrib.contenttypes.models import ContentType
from django.test.utils import override_settings

import pytest

from baserow.contrib.dashboard.application_types import DashboardApplicationType
from baserow.contrib.dashboard.data_sources.models import DashboardDataSource
from baserow.contrib.dashboard.models import Dashboard
from baserow.contrib.dashboard.widgets.models import Widget
from baserow.contrib.dashboard.widgets.service import WidgetService
from baserow.contrib.integrations.local_baserow.models import LocalBaserowIntegration
from baserow.core.handler import CoreHandler
from baserow.core.integrations.models import Integration
from baserow.core.registries import ImportExportConfig
from baserow.core.utils import ChildProgressBuilder, Progress
from baserow_enterprise.dashboard.widgets.models import ChartWidget
from baserow_enterprise.integrations.local_baserow.models import (
    LocalBaserowGroupedAggregateRows,
    LocalBaserowTableServiceAggregationGroupBy,
    LocalBaserowTableServiceAggregationSeries,
    LocalBaserowTableServiceAggregationSortBy,
)


@pytest.mark.django_db
@override_settings(DEBUG=True)
def test_dashboard_export_serialized_with_chart_widget(enterprise_data_fixture):
    enterprise_data_fixture.enable_enterprise()
    user = enterprise_data_fixture.create_user()
    workspace = enterprise_data_fixture.create_workspace(user=user)
    database = enterprise_data_fixture.create_database_application(
        user=user, workspace=workspace
    )
    table = enterprise_data_fixture.create_database_table(database=database)
    field = enterprise_data_fixture.create_number_field(table=table)
    dashboard = cast(
        Dashboard,
        CoreHandler().create_application(
            user,
            workspace,
            type_name="dashboard",
            description="Dashboard description",
            init_with_data=True,
        ),
    )
    integration = Integration.objects.filter(application=dashboard).first()
    dashboard_widget = WidgetService().create_widget(
        user, "chart", dashboard.id, title="Widget 1", description="Description 1"
    )
    service = dashboard_widget.data_source.service
    service.table = table
    service.save()
    LocalBaserowTableServiceAggregationSeries.objects.create(
        service=service, field=field, aggregation_type="sum", order=1
    )
    LocalBaserowTableServiceAggregationGroupBy.objects.create(
        service=service, field=None, order=1
    )
    LocalBaserowTableServiceAggregationSortBy.objects.create(
        service=service,
        sort_on="SERIES",
        reference=f"field_{field.id}_sum",
        order=1,
        direction="ASC",
    )

    serialized = DashboardApplicationType().export_serialized(
        dashboard, ImportExportConfig(include_permission_data=True)
    )

    serialized = json.loads(json.dumps(serialized))
    assert serialized == {
        "id": dashboard.id,
        "name": dashboard.name,
        "description": "Dashboard description",
        "order": dashboard.order,
        "type": "dashboard",
        "integrations": [
            {
                "authorized_user": user.email,
                "id": integration.id,
                "name": "",
                "order": "1.00000000000000000000",
                "type": "local_baserow",
            },
        ],
        "data_sources": [
            {
                "id": dashboard_widget.data_source.id,
                "name": dashboard_widget.data_source.name,
                "order": "1.00000000000000000000",
                "service": {
                    "filter_type": "AND",
                    "filters": [],
                    "id": service.id,
                    "integration_id": service.integration.id,
                    "service_aggregation_group_bys": [
                        {"field_id": None},
                    ],
                    "service_aggregation_series": [
                        {"aggregation_type": "sum", "field_id": field.id},
                    ],
                    "service_aggregation_sorts": [
                        {
                            "direction": "ASC",
                            "reference": f"field_{field.id}_sum",
                            "sort_on": "SERIES",
                        },
                    ],
                    "table_id": table.id,
                    "type": "local_baserow_grouped_aggregate_rows",
                    "view_id": None,
                },
            },
        ],
        "widgets": [
            {
                "data_source_id": dashboard_widget.data_source.id,
                "description": "Description 1",
                "id": dashboard_widget.id,
                "order": "1.00000000000000000000",
                "title": "Widget 1",
                "type": "chart",
            },
        ],
        "role_assignments": [],
    }


@pytest.mark.django_db()
@override_settings(DEBUG=True)
def test_dashboard_import_serialized_with_widgets(enterprise_data_fixture):
    enterprise_data_fixture.enable_enterprise()
    user = enterprise_data_fixture.create_user()
    workspace = enterprise_data_fixture.create_workspace(user=user)
    database = enterprise_data_fixture.create_database_application(
        user=user, workspace=workspace
    )
    table = enterprise_data_fixture.create_database_table(database=database)
    field = enterprise_data_fixture.create_number_field(table=table)
    field_2 = enterprise_data_fixture.create_number_field(table=table, primary=True)

    id_mapping = {
        "database_tables": {1: table.id},
        "database_fields": {1: field.id},
    }

    serialized = {
        "id": "999",
        "name": "Dashboard 1",
        "description": "Description 1",
        "order": 99,
        "type": "dashboard",
        "integrations": [
            {
                "authorized_user": user.email,
                "id": 1,
                "name": "IntegrationName",
                "order": "1.00000000000000000000",
                "type": "local_baserow",
            },
        ],
        "data_sources": [
            {
                "id": 1,
                "name": "DataSource1",
                "order": "1.00000000000000000000",
                "service": {
                    "filter_type": "AND",
                    "filters": [],
                    "id": 1,
                    "integration_id": 1,
                    "service_aggregation_group_bys": [
                        {"field_id": None},
                    ],
                    "service_aggregation_series": [
                        {"aggregation_type": "sum", "field_id": 1},
                    ],
                    "service_aggregation_sorts": [
                        {
                            "direction": "ASC",
                            "reference": f"field_1_sum",
                            "sort_on": "SERIES",
                        },
                    ],
                    "table_id": 1,
                    "type": "local_baserow_grouped_aggregate_rows",
                    "view_id": None,
                },
            },
        ],
        "widgets": [
            {
                "data_source_id": 1,
                "description": "Description 1",
                "id": 45,
                "order": "1.00000000000000000000",
                "title": "Widget 1",
                "type": "chart",
            },
        ],
    }

    progress = Progress(100)
    progress_builder = ChildProgressBuilder(parent=progress, represents_progress=100)
    assert progress.progress == 0

    dashboard = DashboardApplicationType().import_serialized(
        workspace,
        serialized,
        ImportExportConfig(include_permission_data=True),
        id_mapping,
        progress_builder=progress_builder,
    )

    assert dashboard.name == "Dashboard 1"
    assert dashboard.description == "Description 1"
    assert dashboard.order == 99

    integrations = Integration.objects.filter(application=dashboard)
    integration = integrations[0].specific
    assert integrations.count() == 1
    assert integration.content_type == ContentType.objects.get_for_model(
        LocalBaserowIntegration
    )
    assert integration.authorized_user.id == user.id
    assert integration.name == "IntegrationName"
    assert integration.order == Decimal("1.0")

    data_sources = DashboardDataSource.objects.filter(dashboard=dashboard)
    assert data_sources.count() == 1

    ds1 = data_sources[0]
    ds1.name = "DataSource1"
    ds1.order = Decimal("1.0")
    service = ds1.service.specific
    assert service.content_type == ContentType.objects.get_for_model(
        LocalBaserowGroupedAggregateRows
    )
    assert service.integration_id == integration.id
    assert service.filter_type == "AND"

    series = service.service_aggregation_series.all()
    assert series.count() == 1
    assert series[0].aggregation_type == "sum"
    assert series[0].field_id == field.id

    group_bys = service.service_aggregation_group_bys.all()
    assert group_bys.count() == 1
    assert group_bys[0].field_id is None

    sorts = service.service_aggregation_sorts.all()
    assert sorts.count() == 1
    assert sorts[0].direction == "ASC"
    assert sorts[0].sort_on == "SERIES"
    assert sorts[0].reference == f"field_{field.id}_sum"

    widgets = Widget.objects.filter(dashboard=dashboard)
    assert widgets.count() == 1
    widget1 = widgets[0].specific
    assert widget1.content_type == ContentType.objects.get_for_model(ChartWidget)
    assert widget1.title == "Widget 1"
    assert widget1.description == "Description 1"
    assert widget1.order == Decimal("1.0")
    assert widget1.data_source.id == ds1.id

    assert progress.progress == 100
