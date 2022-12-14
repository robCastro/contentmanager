# Generated by Django 4.1 on 2022-08-27 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'sistema',
                'verbose_name_plural': 'sistemas',
            },
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('file', models.FileField(upload_to='archivos/', verbose_name='Archivo')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='content.sistema')),
            ],
            options={
                'verbose_name': 'archivo',
                'verbose_name_plural': 'archivos',
            },
        ),
    ]
