import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import (
    Categories, Comments, Genre, GenreCategories, Review, Titles)
from core.models.users import User


class Command(BaseCommand):
    help = 'fills database from csvfiles in static folder'
    file_table = (
        ('category.csv', Categories),
        ('genre.csv', Genre),
        ('users.csv', User),
        ('titles.csv', Titles),
        ('genre_title.csv', GenreCategories),
        ('review.csv', Review),
        ('comments.csv', Comments),
    )

    def handle(self, *args, **kwargs):
        if not settings.CSV_FILES_FOLDER.exists():
            raise CommandError("add 'data' folder with .csv files")
        for file_name, table_class in self.file_table:
            file = settings.CSV_FILES_FOLDER / file_name
            table_class.objects.all().delete()
            fields_dict = {field.name: field
                           for field in table_class._meta.get_fields()}
            with open(file, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for kwargs in reader:
                    instance_kwargs = dict()
                    for key in kwargs:
                        field = fields_dict.get(key)
                        if field.is_relation:
                            instance_kwargs[key] = (
                                field.related_model.objects.get(id=kwargs[key])
                            )
                        else:
                            instance_kwargs[key] = kwargs[key]
                    instance = table_class(**instance_kwargs)
                    instance.save(force_insert=True)
