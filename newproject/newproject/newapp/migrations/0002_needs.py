# Generated by Django 4.2.4 on 2023-09-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='needs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_name', models.CharField(max_length=250)),
                ('n_img', models.ImageField(upload_to='pics')),
                ('n_desc', models.TextField()),
            ],
        ),
    ]
