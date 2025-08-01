# Generated by Django 5.2.4 on 2025-07-27 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='difficulty_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='estimated_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='skill',
            name='hours_spent',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='platform',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='resource_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
