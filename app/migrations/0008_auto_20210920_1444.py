# Generated by Django 3.2.7 on 2021-09-20 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_listing_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={},
        ),
        migrations.AlterIndexTogether(
            name='listing',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='listing',
            name='city',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='created',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='updated',
        ),
    ]