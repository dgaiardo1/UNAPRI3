# Generated by Django 3.0.14 on 2021-10-22 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0008_auto_20211022_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha',
            name='Observaciones',
        ),
    ]