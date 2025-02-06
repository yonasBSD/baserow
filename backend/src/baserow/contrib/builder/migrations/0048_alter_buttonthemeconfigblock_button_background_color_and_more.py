# Generated by Django 5.0.9 on 2025-01-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0047_repeatelement_horizontal_gap_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buttonthemeconfigblock",
            name="button_background_color",
            field=models.CharField(
                blank=True,
                default="primary",
                help_text="The background color of buttons",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="buttonthemeconfigblock",
            name="button_border_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="The border color of buttons",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="buttonthemeconfigblock",
            name="button_hover_background_color",
            field=models.CharField(
                blank=True,
                default="#96baf6ff",
                help_text="The background color of buttons when hovered",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="buttonthemeconfigblock",
            name="button_hover_border_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="The border color of buttons when hovered",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="buttonthemeconfigblock",
            name="button_hover_text_color",
            field=models.CharField(
                blank=True,
                default="#ffffffff",
                help_text="The text color of buttons when hovered",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="buttonthemeconfigblock",
            name="button_text_color",
            field=models.CharField(
                blank=True,
                default="#ffffffff",
                help_text="The text color of buttons",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="colorthemeconfigblock",
            name="border_color",
            field=models.CharField(default="#d7d8d9ff", max_length=255),
        ),
        migrations.AlterField(
            model_name="colorthemeconfigblock",
            name="main_error_color",
            field=models.CharField(default="#FF5A4A", max_length=255),
        ),
        migrations.AlterField(
            model_name="colorthemeconfigblock",
            name="main_success_color",
            field=models.CharField(default="#12D452", max_length=255),
        ),
        migrations.AlterField(
            model_name="colorthemeconfigblock",
            name="main_warning_color",
            field=models.CharField(default="#FCC74A", max_length=255),
        ),
        migrations.AlterField(
            model_name="colorthemeconfigblock",
            name="primary_color",
            field=models.CharField(default="#5190efff", max_length=255),
        ),
        migrations.AlterField(
            model_name="colorthemeconfigblock",
            name="secondary_color",
            field=models.CharField(default="#0eaa42ff", max_length=255),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_background_color",
            field=models.CharField(
                blank=True,
                default="#ffffffff",
                help_text="The background color if `style_background` is color.",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_border_bottom_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="Bottom border color",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_border_left_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="Left border color",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_border_right_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="Right border color",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_border_top_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="Top border color.",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="inputthemeconfigblock",
            name="input_background_color",
            field=models.CharField(
                blank=True,
                default="#FFFFFFFF",
                help_text="The background color of the input",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="inputthemeconfigblock",
            name="input_border_color",
            field=models.CharField(
                blank=True,
                default="#000000FF",
                help_text="The color of the input border",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="inputthemeconfigblock",
            name="input_text_color",
            field=models.CharField(
                blank=True,
                default="#070810FF",
                help_text="The text color of the input",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="inputthemeconfigblock",
            name="label_text_color",
            field=models.CharField(
                blank=True,
                default="#070810FF",
                help_text="The text color of the label",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="linkthemeconfigblock",
            name="link_hover_text_color",
            field=models.CharField(
                blank=True,
                default="#96baf6ff",
                help_text="The hover color of links when hovered",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="linkthemeconfigblock",
            name="link_text_color",
            field=models.CharField(
                blank=True,
                default="primary",
                help_text="The text color of links",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="pagethemeconfigblock",
            name="page_background_color",
            field=models.CharField(
                blank=True,
                default="#ffffffff",
                help_text="The background color of the page",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="tablethemeconfigblock",
            name="table_border_color",
            field=models.CharField(
                blank=True,
                default="#000000FF",
                help_text="The color of the table border",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="tablethemeconfigblock",
            name="table_cell_alternate_background_color",
            field=models.CharField(
                blank=True,
                default="transparent",
                help_text="The alternate background color of the table cells",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="tablethemeconfigblock",
            name="table_cell_background_color",
            field=models.CharField(
                blank=True,
                default="transparent",
                help_text="The background color of the table cells",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="tablethemeconfigblock",
            name="table_header_background_color",
            field=models.CharField(
                blank=True,
                default="#edededff",
                help_text="The background color of the table header cells",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="tablethemeconfigblock",
            name="table_header_text_color",
            field=models.CharField(
                blank=True,
                default="#000000ff",
                help_text="The text color of the table header cells",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="tablethemeconfigblock",
            name="table_horizontal_separator_color",
            field=models.CharField(
                blank=True,
                default="#000000FF",
                help_text="The color of the table horizontal separator",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="tablethemeconfigblock",
            name="table_vertical_separator_color",
            field=models.CharField(
                blank=True,
                default="#000000FF",
                help_text="The color of the table vertical separator",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="typographythemeconfigblock",
            name="body_text_color",
            field=models.CharField(default="#070810ff", max_length=255),
        ),
        migrations.AlterField(
            model_name="typographythemeconfigblock",
            name="heading_1_text_color",
            field=models.CharField(default="#070810ff", max_length=255),
        ),
        migrations.AlterField(
            model_name="typographythemeconfigblock",
            name="heading_2_text_color",
            field=models.CharField(default="#070810ff", max_length=255),
        ),
        migrations.AlterField(
            model_name="typographythemeconfigblock",
            name="heading_3_text_color",
            field=models.CharField(default="#070810ff", max_length=255),
        ),
        migrations.AlterField(
            model_name="typographythemeconfigblock",
            name="heading_4_text_color",
            field=models.CharField(default="#070810ff", max_length=255),
        ),
        migrations.AlterField(
            model_name="typographythemeconfigblock",
            name="heading_5_text_color",
            field=models.CharField(default="#070810ff", max_length=255),
        ),
        migrations.AlterField(
            model_name="typographythemeconfigblock",
            name="heading_6_text_color",
            field=models.CharField(default="#202128", max_length=255),
        ),
    ]
