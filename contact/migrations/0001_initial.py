# Generated by Django 3.0.5 on 2020-04-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollForDemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=124, null=True)),
                ('last_name', models.CharField(max_length=124, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('father_name', models.CharField(max_length=255, null=True)),
                ('mobile_number', models.CharField(max_length=10, null=True)),
                ('student', models.CharField(choices=[('school', 'School Student'), ('college', 'College Student'), ('self', 'Self Learner'), ('working', 'Working Person'), ('other', 'Other')], default='school', max_length=124, null=True)),
                ('about', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Enrollment for Demo',
                'verbose_name_plural': 'Enrollements for Demo',
                'ordering': ['first_name', 'last_name', 'father_name'],
            },
        ),
    ]