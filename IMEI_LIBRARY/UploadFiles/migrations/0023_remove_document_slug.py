# Generated by Django 2.1.7 on 2020-09-03 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFiles', '0022_document_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='slug',
        ),
    ]
