# Generated by Django 3.2.7 on 2021-09-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/img/listing/%Y/%m/%d'),
        ),
    ]