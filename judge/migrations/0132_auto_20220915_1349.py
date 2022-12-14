# Generated by Django 2.2.25 on 2022-09-15 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0131_auto_20220905_0027"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contestproblem",
            name="max_submissions",
            field=models.IntegerField(
                default=0,
                help_text="Maximum number of submissions for this problem, or 0 for no limit.",
                validators=[
                    django.core.validators.MinValueValidator(
                        0, "Why include a problem you can't submit to?"
                    )
                ],
                verbose_name="max submissions",
            ),
        ),
    ]
