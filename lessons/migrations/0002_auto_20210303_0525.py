# Generated by Django 3.1.7 on 2021-03-03 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='lessonsegment',
            name='title',
            field=models.CharField(max_length=127),
        ),
    ]