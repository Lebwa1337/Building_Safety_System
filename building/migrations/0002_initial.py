# Generated by Django 5.0.6 on 2024-07-08 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('building', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entrance',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building.building'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='entrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building.entrance'),
        ),
    ]
