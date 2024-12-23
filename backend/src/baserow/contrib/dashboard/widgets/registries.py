from abc import ABC
from decimal import Decimal

from baserow.contrib.dashboard.types import WidgetDict
from baserow.core.registry import (
    CustomFieldsInstanceMixin,
    CustomFieldsRegistryMixin,
    EasyImportExportMixin,
    Instance,
    ModelInstanceMixin,
    ModelRegistryMixin,
    Registry,
)

from .exceptions import WidgetTypeDoesNotExist
from .models import Widget

DASHBOARD_WIDGETS = "dashboard_widgets"


class WidgetType(
    EasyImportExportMixin[Widget],
    CustomFieldsInstanceMixin,
    ModelInstanceMixin[Widget],
    Instance,
    ABC,
):
    """Widget type"""

    SerializedDict = WidgetDict
    parent_property_name = "dashboard"
    id_mapping_name = DASHBOARD_WIDGETS
    allowed_fields = ["title", "description"]

    def prepare_value_for_db(self, values: dict, instance: Widget | None = None):
        """
        This function allows you to hook into the moment a widget is created or
        updated. If the widget is updated, `instance` of the current widget
        will be defined.

        :param values: The values that are being updated
        :param instance: (optional) The existing instance that is being updated
        """

        return values

    def after_delete(self, instance: Widget):
        """
        This function allows you to hook into the moment after a widget is
        deleted.

        :param instance: The instance that was deleted.
        """

        pass

    def deserialize_property(
        self,
        prop_name: str,
        value: any,
        id_mapping: dict[str, any],
        **kwargs,
    ) -> any:
        if prop_name == "order" and value:
            return Decimal(value)

        return super().deserialize_property(
            prop_name,
            value,
            id_mapping,
            **kwargs,
        )

    def serialize_property(
        self,
        instance: Widget,
        prop_name: str,
        files_zip=None,
        storage=None,
        cache=None,
    ):
        if prop_name == "order":
            return str(instance.order)

        return super().serialize_property(
            instance,
            prop_name,
            files_zip=files_zip,
            storage=storage,
            cache=cache,
        )


class WidgetTypeRegistry(
    Registry[WidgetType],
    ModelRegistryMixin[Widget, WidgetType],
    CustomFieldsRegistryMixin,
):
    """
    Contains all registered widget types.
    """

    name = "dashboard_widget"
    does_not_exist_exception_class = WidgetTypeDoesNotExist


widget_type_registry = WidgetTypeRegistry()
