# Generated by Django 3.1 on 2020-09-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=80, verbose_name='Description')),
                ('done', models.BooleanField(default=False, verbose_name='Done?')),
            ],
        ),
    ]
