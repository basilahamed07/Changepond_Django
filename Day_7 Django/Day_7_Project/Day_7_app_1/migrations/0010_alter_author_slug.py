# Generated by Django 4.2.15 on 2024-08-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Day_7_app_1', '0009_author_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(editable=False, null=True),
        ),
    ]
