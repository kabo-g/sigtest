# Generated by Django 4.0.5 on 2022-10-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_signature_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='images_sig/'),
        ),
    ]
