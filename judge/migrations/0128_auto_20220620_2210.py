# Generated by Django 2.2.25 on 2022-06-20 15:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0127_auto_20220616_1442"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problem",
            name="memory_limit",
            field=models.PositiveIntegerField(
                help_text="The memory limit for this problem, in kilobytes (e.g. 256mb = 262144 kilobytes).",
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1048576),
                ],
                verbose_name="memory limit",
            ),
        ),
    ]
