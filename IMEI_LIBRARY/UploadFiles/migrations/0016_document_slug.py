# Generated by Django 2.1.7 on 2020-09-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFiles', '0015_auto_20200810_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]