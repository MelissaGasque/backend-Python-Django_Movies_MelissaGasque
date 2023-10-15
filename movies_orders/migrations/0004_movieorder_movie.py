# Generated by Django 4.2.6 on 2023-10-15 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_initial'),
        ('movies_orders', '0003_remove_movieorder_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieorder',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movie_orders', to='movies.movie'),
            preserve_default=False,
        ),
    ]
