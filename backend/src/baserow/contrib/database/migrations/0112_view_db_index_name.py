# Generated by Django 3.2.18 on 2023-05-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0111_alter_airtableimportjob_workspace"),
    ]

    operations = [
        migrations.AddField(
            model_name="view",
            name="db_index_name",
            field=models.CharField(
                null=True,
                blank=True,
                help_text="The name of the database index that is used to speed up the filtering of the view.",
                max_length=30,
            ),
        ),
    ]