# Generated by Django 3.1.7 on 2021-03-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210304_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descriptions', models.CharField(max_length=800)),
                ('descriptions_details', models.CharField(max_length=1000)),
                ('admin', models.CharField(max_length=50)),
                ('comment', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('like', models.IntegerField()),
                ('tag', models.IntegerField()),
                ('productLink', models.CharField(max_length=500)),
            ],
        ),
    ]
