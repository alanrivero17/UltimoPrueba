# Generated by Django 2.1.2 on 2018-10-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_registrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='')),
                ('raza', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]