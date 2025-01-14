# Generated by Django 3.2.2 on 2023-09-19 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('pais', models.CharField(blank=True, max_length=100)),
                ('provincia', models.CharField(blank=True, max_length=120)),
                ('ciudad', models.CharField(blank=True, max_length=100)),
                ('codigo_postal', models.PositiveIntegerField(blank=True)),
                ('telefono', models.CharField(blank=True, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
