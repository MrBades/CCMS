# Generated by Django 4.1.5 on 2023-11-10 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Inventories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="update_Date",
            field=models.DateField(default=datetime.date(2023, 11, 10), null=True),
        ),
    ]
