# Generated by Django 4.1.5 on 2024-02-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0013_admessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admessage',
            name='adId',
            field=models.CharField(max_length=200000000000000000000000000),
        ),
    ]
