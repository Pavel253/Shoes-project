# Generated by Django 4.2.6 on 2024-01-20 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0008_alter_shoes_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.gender'),
        ),
    ]
