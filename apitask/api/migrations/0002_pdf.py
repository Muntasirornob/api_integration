# Generated by Django 3.0.11 on 2020-12-14 18:52

import api.formatChecker
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', api.formatChecker.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
