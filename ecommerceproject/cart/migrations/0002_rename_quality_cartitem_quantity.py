# Generated by Django 4.2.8 on 2024-01-02 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quality',
            new_name='quantity',
        ),
    ]
