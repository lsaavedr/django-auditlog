# Generated by Django 3.2.12 on 2022-02-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auditlog", "0009_alter_logentry_additional_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="additional_data",
            field=models.JSONField(
                blank=True, null=True, verbose_name="additional data"
            ),
        ),
    ]
