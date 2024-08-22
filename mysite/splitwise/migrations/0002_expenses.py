# Generated by Django 5.1 on 2024-08-22 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitwise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='splitwise.events')),
            ],
        ),
    ]
