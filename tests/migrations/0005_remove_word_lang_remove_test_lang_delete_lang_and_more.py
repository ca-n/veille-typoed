# Generated by Django 4.2.6 on 2023-11-06 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_alter_test_wpm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='test',
            name='lang',
        ),
        migrations.DeleteModel(
            name='Lang',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
