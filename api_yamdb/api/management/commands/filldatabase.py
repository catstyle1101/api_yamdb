import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.dateparse import parse_datetime

from api.models import (
    Categories, Comments, Genre, GenreCategories, Review, Titles)
from core.models.users import User

class Command(BaseCommand):
    help = 'fills database from csvfiles in static folder'
    file_table = {
        'category.csv': Categories,
        'genre.csv': Genre,
        'users.csv': User,
        # 'comments.csv': Comments,
    }

    def handle(self, *args, **kwargs):
        if not settings.CSV_FILES_FOLDER.exists():
            raise CommandError("add 'data' folder with .csv files")

        for file in settings.CSV_FILES_FOLDER.iterdir():
            table_name = file.name
            table_class = self.file_table.get(table_name)
            if not table_class:
                continue
            table_class.objects.all().delete()
            with open(file, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for kwargs in reader:
                    instance = table_class(**kwargs)
                    instance.save(force_insert=True)
        with open(
                settings.CSV_FILES_FOLDER / 'titles.csv',
                mode='r', newline='', encoding='utf-8'
        ) as f:
            reader = csv.DictReader(f)
            Titles.objects.all().delete()
            for row in reader:
                Titles.objects.create(
                    id=row.get('id'),
                    name=row.get('name'),
                    year=row.get('year'),
                    category=Categories.objects.get(id=row.get('category')),
                )
        with open(
            settings.CSV_FILES_FOLDER / 'genre_title.csv',
                mode='r', newline='', encoding='utf-8'
        ) as f:
            reader = csv.DictReader(f)
            GenreCategories.objects.all().delete()
            for row in reader:
                GenreCategories.objects.create(
                    id=row.get('id'),
                    title_id=Titles.objects.get(id=row.get('title_id')),
                    genre_id=Genre.objects.get(id=row.get('genre_id')),
                )
        with open(
                settings.CSV_FILES_FOLDER / 'review.csv',
                mode='r', newline='', encoding='utf-8'
        ) as f:
            reader = csv.DictReader(f)
            Review.objects.all().delete()
            for row in reader:
                Review.objects.create(
                    id=row.get('id'),
                    title_id=Titles.objects.get(id=row.get('title_id')),
                    text=row.get('text'),
                    author=User.objects.get(id=row.get('author')),
                    score=row.get('score'),
                    pub_date=parse_datetime(row.get('pub_date')),
                )
        with open(
                settings.CSV_FILES_FOLDER / 'comments.csv',
                mode='r', newline='', encoding='utf-8'
        ) as f:
            reader = csv.DictReader(f)
            Comments.objects.all().delete()
            for row in reader:
                Comments.objects.create(
                    id=row.get('id'),
                    review_id=Review.objects.get(id=row.get('review_id')),
                    text=row.get('text'),
                    author=User.objects.get(id=row.get('author')),
                    pub_date=parse_datetime(row.get('pub_date')),
                )


