# Generated by Django 5.0.13 on 2025-07-07 08:35

import django.db.models.deletion
from django.db import migrations, models

import baserow.core.fields


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0192_field_search_data_initialized_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FieldConstraint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", baserow.core.fields.SyncedDateTimeField(auto_now=True)),
                ("trashed", models.BooleanField(db_index=True, default=False)),
                (
                    "type_name",
                    models.CharField(
                        help_text="The type name of the constraint.", max_length=255
                    ),
                ),
                (
                    "field",
                    models.ForeignKey(
                        help_text="The field this constraint belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="field_constraints",
                        to="database.field",
                    ),
                ),
            ],
            options={
                "ordering": ("type_name",),
                "unique_together": {("field", "type_name")},
            },
        ),
    ]
