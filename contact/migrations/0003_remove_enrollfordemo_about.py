# Generated by Django 3.0.5 on 2020-04-04 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_enrollfordemo_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollfordemo',
            name='about',
        ),
    ]
