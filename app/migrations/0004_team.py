# Generated by Django 3.2.7 on 2021-09-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=None)),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=100)),
            ],
        ),
    ]
