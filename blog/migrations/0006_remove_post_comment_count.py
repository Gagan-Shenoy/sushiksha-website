# Generated by Django 3.1.1 on 2020-09-29 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200927_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]