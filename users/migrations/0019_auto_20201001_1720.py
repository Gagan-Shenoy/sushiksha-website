# Generated by Django 3.1.1 on 2020-10-01 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20201001_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='members',
        ),
        migrations.DeleteModel(
            name='House',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
    ]