# Generated by Django 4.2 on 2023-05-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0003_alter_movie_discription_alter_movie_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='discription',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
