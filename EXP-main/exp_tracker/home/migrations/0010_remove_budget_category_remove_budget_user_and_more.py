# Generated by Django 5.0.2 on 2024-03-04 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_category_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='category',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
    ]
