# Generated by Django 2.1.7 on 2020-08-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFiles', '0013_auto_20200810_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
