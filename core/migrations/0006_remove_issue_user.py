# Generated by Django 4.0 on 2022-05-17 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_issue_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='user',
        ),
    ]
