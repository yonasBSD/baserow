# Generated by Django 5.0.9 on 2024-11-07 10:35

import uuid

import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models

import baserow.core.fields


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0090_exportapplicationsjob"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ImportExportTrustedSource",
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
                ("name", models.CharField(blank=True, max_length=255)),
                (
                    "private_key",
                    models.TextField(
                        help_text="The private key used to sign the export."
                    ),
                ),
                (
                    "public_key",
                    models.TextField(
                        help_text="The public key used to verify the signature of the export."
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="exportapplicationsjob",
            name="exported_file_name",
        ),
        migrations.RemoveField(
            model_name="exportapplicationsjob",
            name="workspace_id",
        ),
        migrations.AddField(
            model_name="exportapplicationsjob",
            name="workspace",
            field=models.ForeignKey(
                help_text="The workspace that the applications are going to be exported from.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.workspace",
            ),
        ),
        migrations.AddField(
            model_name="settings",
            name="verify_import_signature",
            field=models.BooleanField(
                db_default=True,
                default=True,
                help_text="Indicates whether the signature of imported files should be verified.",
            ),
        ),
        migrations.RemoveField(
            model_name="exportapplicationsjob",
            name="application_ids",
        ),
        migrations.AddField(
            model_name="exportapplicationsjob",
            name="application_ids",
            field=models.JSONField(
                default=list,
                help_text="The list of application ids that are going to be exported.",
            ),
        ),
        migrations.CreateModel(
            name="ImportExportResource",
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
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        help_text="The UUID of the resource, used in the archive name and as the directory name for temporary storage before archiving or extraction. The folder must be checked and deleted before deleting the instance.",
                    ),
                ),
                (
                    "original_name",
                    models.CharField(
                        help_text=(
                            "The original name of the file. This is only used in the frontend for uploaded files.",
                        ),
                        max_length=255,
                    ),
                ),
                (
                    "size",
                    models.PositiveIntegerField(
                        default=0, help_text="The size of the resource in bytes."
                    ),
                ),
                (
                    "is_valid",
                    models.BooleanField(
                        default=False,
                        help_text=(
                            "Indicates whether the resource is valid and can be used for import or export. If it's not valid, the temporary files should be deleted before deleting the instance.",
                        ),
                    ),
                ),
                (
                    "marked_for_deletion",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates whether the resource is marked for deletion. The temporary files should be deleted before deleting the instance.",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The owner of the resource.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects_and_trash", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="ImportApplicationsJob",
            fields=[
                (
                    "job_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.job",
                    ),
                ),
                (
                    "user_ip_address",
                    models.GenericIPAddressField(
                        help_text="The user IP address.", null=True
                    ),
                ),
                (
                    "user_websocket_id",
                    models.CharField(
                        help_text="The user websocket uuid needed to manage signals sent correctly.",
                        max_length=36,
                        null=True,
                    ),
                ),
                (
                    "user_session_id",
                    models.CharField(
                        help_text="The user session uuid needed for undo/redo functionality.",
                        max_length=36,
                        null=True,
                    ),
                ),
                (
                    "user_action_group_id",
                    models.CharField(
                        help_text="The user session uuid needed for undo/redo action group functionality.",
                        max_length=36,
                        null=True,
                    ),
                ),
                (
                    "application_ids",
                    models.JSONField(
                        default=list,
                        help_text="The list of application IDs that are going to be imported. These IDs must be available in the resource.",
                    ),
                ),
                (
                    "only_structure",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if only the structure of the applications should be exported, without user data.",
                    ),
                ),
                (
                    "workspace",
                    models.ForeignKey(
                        help_text="The workspace id that the applications are going to be imported to.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.workspace",
                    ),
                ),
                (
                    "resource",
                    models.ForeignKey(
                        help_text="The resource that contains the applications to import.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.importexportresource",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.job", models.Model),
        ),
        migrations.AddField(
            model_name="exportapplicationsjob",
            name="resource",
            field=models.ForeignKey(
                help_text="The resource that contains the exported applications.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.importexportresource",
            ),
        ),
    ]
