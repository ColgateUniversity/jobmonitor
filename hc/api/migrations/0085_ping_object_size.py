# Generated by Django 4.0.2 on 2022-02-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0084_ping_body_raw"),
    ]

    operations = [
        migrations.AddField(
            model_name="ping",
            name="object_size",
            field=models.IntegerField(null=True),
        ),
    ]
