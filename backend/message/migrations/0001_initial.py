# Generated by Django 4.1.3 on 2022-11-19 02:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(default=datetime.date.today, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.category')),
            ],
        ),
    ]
