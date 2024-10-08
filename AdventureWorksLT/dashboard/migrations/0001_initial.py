# Generated by Django 4.1 on 2024-03-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "customerid",
                    models.AutoField(
                        db_column="CustomerID", primary_key=True, serialize=False
                    ),
                ),
                ("namestyle", models.BooleanField(db_column="NameStyle")),
                (
                    "title",
                    models.CharField(
                        blank=True, db_column="Title", max_length=8, null=True
                    ),
                ),
                ("firstname", models.CharField(db_column="FirstName", max_length=50)),
                (
                    "middlename",
                    models.CharField(
                        blank=True, db_column="MiddleName", max_length=50, null=True
                    ),
                ),
                ("lastname", models.CharField(db_column="LastName", max_length=50)),
                (
                    "suffix",
                    models.CharField(
                        blank=True, db_column="Suffix", max_length=10, null=True
                    ),
                ),
                (
                    "companyname",
                    models.CharField(
                        blank=True, db_column="CompanyName", max_length=128, null=True
                    ),
                ),
                (
                    "salesperson",
                    models.CharField(
                        blank=True, db_column="SalesPerson", max_length=256, null=True
                    ),
                ),
                (
                    "emailaddress",
                    models.CharField(
                        blank=True, db_column="EmailAddress", max_length=50, null=True
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, db_column="Phone", max_length=25, null=True
                    ),
                ),
                (
                    "passwordhash",
                    models.CharField(db_column="PasswordHash", max_length=128),
                ),
                (
                    "passwordsalt",
                    models.CharField(db_column="PasswordSalt", max_length=10),
                ),
                ("rowguid", models.CharField(db_column="rowguid", max_length=36)),
                ("modifieddate", models.DateTimeField(db_column="ModifiedDate")),
            ],
            options={
                "db_table": "SalesLT].[Customer",
            },
        ),
    ]
