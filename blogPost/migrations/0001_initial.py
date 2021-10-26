# Generated by Django 3.2.7 on 2021-10-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('tittle', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('content', models.CharField(max_length=20)),
                ('timestamp', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
