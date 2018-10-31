# Generated by Django 2.1.2 on 2018-10-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrado',
            name='numero',
        ),
        migrations.AddField(
            model_name='registrado',
            name='numero_calle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrado',
            name='calle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrado',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
    ]