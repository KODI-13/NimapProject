# Generated by Django 5.0.2 on 2024-02-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_client_uniqueid_alter_client_client_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
