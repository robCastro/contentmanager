# Generated by Django 4.1 on 2022-08-28 21:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_archivo_sistema_archivo_sistemas'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistema',
            name='api_key',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Api Key'),
        ),
    ]
