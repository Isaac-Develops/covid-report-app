# Generated by Django 3.2.8 on 2021-10-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='default_movie.png', upload_to='assets'),
        ),
    ]