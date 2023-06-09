# Generated by Django 4.2 on 2023-04-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='media')),
                ('discription', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'movie',
                'ordering': ('name', 'age'),
            },
        ),
    ]
