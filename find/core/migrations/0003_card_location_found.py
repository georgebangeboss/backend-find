# Generated by Django 4.1.1 on 2022-11-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_card_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="location_found",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
