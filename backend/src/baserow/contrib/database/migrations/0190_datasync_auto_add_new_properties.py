# Generated by Django 5.0.13 on 2025-06-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0189_alter_tableusageupdate_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="datasync",
            name="auto_add_new_properties",
            field=models.BooleanField(
                db_default=False,
                default=False,
                help_text="If enabled and new properties are detected on sync, then they're automatically added. Note that this means all properties will always be added.",
            ),
        ),
    ]
