# Generated by Django 4.2 on 2023-04-16 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("disks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="track",
            old_name="albums",
            new_name="album",
        ),
    ]
