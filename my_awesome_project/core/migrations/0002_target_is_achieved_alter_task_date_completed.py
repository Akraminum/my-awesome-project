# Generated by Django 4.2.8 on 2024-01-02 20:59

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="target",
            name="is_achieved",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="date_completed",
            field=model_utils.fields.MonitorField(
                default=django.utils.timezone.now, monitor="is_completed", null=True, when={True}
            ),
        ),
    ]
