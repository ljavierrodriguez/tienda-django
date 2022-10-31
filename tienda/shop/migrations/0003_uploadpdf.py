# Generated by Django 4.1 on 2022-10-31 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumes', models.FileField(blank=True, null=True, upload_to='resumes/')),
            ],
            options={
                'db_table': 'resumes',
            },
        ),
    ]
