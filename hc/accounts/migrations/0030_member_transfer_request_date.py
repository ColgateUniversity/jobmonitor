# Generated by Django 3.0.4 on 2020-04-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0029_remove_profile_current_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="transfer_request_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
