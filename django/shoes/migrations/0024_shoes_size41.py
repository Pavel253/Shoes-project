# Generated by Django 4.2.6 on 2024-01-31 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0023_remove_shoes_size41'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='size41',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
