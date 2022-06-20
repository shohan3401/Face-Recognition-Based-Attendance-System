# Generated by Django 4.0.4 on 2022-05-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_remove_studentdatamodel_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('roll', models.PositiveIntegerField(null=True)),
                ('course', models.CharField(max_length=150, null=True)),
                ('stream', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('year', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentDataModel',
        ),
    ]
