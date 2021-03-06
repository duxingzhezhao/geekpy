# Generated by Django 2.0 on 2018-02-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('icon', models.ImageField(upload_to='')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
            ],
        ),
    ]
