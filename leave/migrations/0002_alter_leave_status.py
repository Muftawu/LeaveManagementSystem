# Generated by Django 4.1.4 on 2023-01-17 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.BooleanField(choices=[('True', 'True'), ('False', 'False'), ('Pending', 'Pending')], default=False),
        ),
    ]