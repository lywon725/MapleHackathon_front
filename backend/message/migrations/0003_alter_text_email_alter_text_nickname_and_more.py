# Generated by Django 4.1.3 on 2022-11-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_remove_text_created_at_alter_text_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='nickname',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
