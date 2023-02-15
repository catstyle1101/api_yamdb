# Generated by Django 3.2 on 2023-02-14 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва'),
        ),
        migrations.AddField(
            model_name='review',
            name='title_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='api.titles', verbose_name='Отзыв'),
        ),
        migrations.AddField(
            model_name='genrecategories',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.genre'),
        ),
        migrations.AddField(
            model_name='genrecategories',
            name='title_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.titles'),
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AddField(
            model_name='comments',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.review', verbose_name='Коментарии'),
        ),
        migrations.AddConstraint(
            model_name='genrecategories',
            constraint=models.UniqueConstraint(fields=('title_id', 'genre_id'), name='unique_title_genre'),
        ),
    ]