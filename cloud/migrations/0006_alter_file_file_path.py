# Generated by Django 4.2.7 on 2023-12-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cloud", "0005_remove_user_pass_to_store_user_path_to_store"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file_path",
            field=models.CharField(max_length=500),
        ),
    ]
