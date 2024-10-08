# Generated by Django 4.2.15 on 2024-08-12 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weekapp', '0003_alter_author_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(59)]),
        ),
    ]
