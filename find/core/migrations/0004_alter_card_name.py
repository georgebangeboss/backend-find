# Generated by Django 4.1.1 on 2022-11-16 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_card_college_name_alter_card_department_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
