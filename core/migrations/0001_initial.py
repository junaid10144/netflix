# Generated by Django 4.2.6 on 2023-11-19 07:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('rating', models.FloatField()),
                ('length', models.PositiveIntegerField()),
                ('image_card', models.ImageField(upload_to='movies_images/')),
                ('image_cover', models.ImageField(upload_to='movies_images/')),
                ('video', models.FileField(upload_to='movies_videos/')),
                ('movie_views', models.PositiveIntegerField(default=0)),
                ('genre', models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('horror', 'Horror'), ('romance', 'Romance'), ('thriller', 'Thriller')], max_length=50)),
            ],
        ),
    ]