# Generated by Django 3.2.7 on 2021-10-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0004_auto_20211011_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
