# Generated by Django 2.2.13 on 2020-06-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20200626_1139"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="boolean",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
