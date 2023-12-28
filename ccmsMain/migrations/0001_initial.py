# Generated by Django 4.1.5 on 2023-10-26 09:41

import ccmsMain.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bank_Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=10000)),
                ("Account_Number", models.CharField(max_length=10000)),
                ("Bank", models.CharField(max_length=1000)),
                ("Swift_Code", models.CharField(max_length=1000)),
                ("Mail", models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name="Purpose",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="WebsiteResources",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Admin_Name",
                    models.CharField(default="CarewCouture", max_length=100),
                ),
                ("Name", models.CharField(max_length=100)),
                (
                    "Site_Upload",
                    models.FileField(
                        blank=True,
                        upload_to="sitesIMGS/%y",
                        validators=[ccmsMain.validators.file_size],
                    ),
                ),
                ("Document_Description", models.TextField(max_length=1000000)),
                (
                    "Purpose",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ccmsMain.purpose",
                    ),
                ),
            ],
        ),
    ]
