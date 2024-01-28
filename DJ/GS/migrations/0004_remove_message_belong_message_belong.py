# Generated by Django 5.0.1 on 2024-01-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("GS", "0003_alter_group_options_alter_message_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="belong",
        ),
        migrations.AddField(
            model_name="message",
            name="belong",
            field=models.ManyToManyField(related_name="belong", to="GS.group"),
        ),
    ]