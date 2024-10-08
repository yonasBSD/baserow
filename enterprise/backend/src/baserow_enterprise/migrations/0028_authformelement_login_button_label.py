# Generated by Django 4.2.13 on 2024-07-12 12:38

from django.db import migrations

import baserow.core.formula.field


class Migration(migrations.Migration):
    dependencies = [
        ("baserow_enterprise", "0027_migrate_auth_form_style"),
    ]

    operations = [
        migrations.AddField(
            model_name="authformelement",
            name="login_button_label",
            field=baserow.core.formula.field.FormulaField(
                blank=True,
                default="",
                help_text="The label of the login button",
                null=True,
            ),
        ),
    ]
