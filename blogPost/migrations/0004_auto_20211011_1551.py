# Generated by Django 3.2.7 on 2021-10-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
