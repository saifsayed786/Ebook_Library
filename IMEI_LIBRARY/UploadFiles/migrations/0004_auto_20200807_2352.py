# Generated by Django 2.1.7 on 2020-08-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFiles', '0003_document_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='subcategory',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
