# Generated by Django 2.1.7 on 2020-08-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFiles', '0011_auto_20200808_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='UploadFiles/%Y/%m/%d'),
        ),
    ]
