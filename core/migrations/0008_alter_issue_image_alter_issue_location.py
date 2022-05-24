# Generated by Django 4.0.4 on 2022-05-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_issue_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/issues/'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]