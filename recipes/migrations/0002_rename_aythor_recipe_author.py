# Generated by Django 5.1.4 on 2025-01-06 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='aythor',
            new_name='author',
        ),
    ]