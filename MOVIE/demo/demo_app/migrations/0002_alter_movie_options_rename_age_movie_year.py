# Generated by Django 4.2 on 2023-04-26 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('name', 'year'), 'verbose_name_plural': 'movie'},
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='age',
            new_name='year',
        ),
    ]