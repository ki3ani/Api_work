# Generated by Django 4.1 on 2022-09-07 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField(verbose_name=range(1, 11))),
                ('genre', models.ManyToManyField(related_name='movies', to='lets_rate.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField(verbose_name=range(1, 11))),
                ('genre', models.ManyToManyField(related_name='series', to='lets_rate.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Series_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('series_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='lets_rate.series')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('movie_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='lets_rate.movie')),
            ],
        ),
    ]
