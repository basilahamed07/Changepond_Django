# Generated by Django 3.2.19 on 2024-08-28 05:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_app_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author_app.author')),
            ],
        ),
    ]
