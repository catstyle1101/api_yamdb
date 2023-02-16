import csv
from argparse import RawTextHelpFormatter

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import (
    Categories, Comments, Genre, GenreCategories, Review, Titles)
from core.models.users import User


class Command(BaseCommand):
    help = """Заполняет базу данных из csv файлов в папке data:
    Файлы:
    - category.csv Столбцы: id, name, slug
    - genre.csv Столбцы: id, name, slug
    - titles.csv Столбцы: id, name, year, category
    - users.csv Столбцы: id, username, email, role, bio, first_name, last_name
    - genre_title.csv Столбцы: id, title_id, genre_id
    - review.csv Столбцы: id, title_id, text, author, score, pub_date
    - comments.csv Столбцы: id, review_id, text, author, pub_date
    """
    file_table = (
        ('category.csv', Categories),
        ('genre.csv', Genre),
        ('users.csv', User),
        ('titles.csv', Titles),
        ('genre_title.csv', GenreCategories),
        ('review.csv', Review),
        ('comments.csv', Comments),
    )

    def create_parser(self, *args, **kwargs):
        parser = super(Command, self).create_parser(*args, **kwargs)
        parser.formatter_class = RawTextHelpFormatter
        return parser

    def handle(self, *args, **kwargs):
        if not settings.CSV_FILES_FOLDER.exists():
            raise CommandError("Добавьте папку 'data' с .csv файлами")
        for file_name, class_ in self.file_table:
            file_path = settings.CSV_FILES_FOLDER / file_name
            if not file_path.exists():
                raise CommandError(
                    f"Файл {file_path.name} не найден"
                )
            class_.objects.all().delete()
            class_fields = {field.name: field
                            for field in class_._meta.get_fields()}
            with open(file_path, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for kwargs in reader:
                    instance_kwargs = dict()
                    for key in kwargs:
                        field = class_fields.get(key)
                        if field.is_relation:
                            related_model = (
                                field.related_model.objects.get(
                                    id=kwargs[key]))
                            if not related_model:
                                raise CommandError(
                                    f"Для модели {class_} в поле "
                                    f"{field.name} не найдено связанной "
                                    f"модели {field.related_model} в БД "
                                    f"с ключом {key} = {kwargs[key]}"
                                )
                            instance_kwargs[key] = related_model
                        else:
                            instance_kwargs[key] = kwargs[key]
                    instance = class_(**instance_kwargs)
                    instance.save(force_insert=True)
            self.stdout.write(f'Файл {file_name} обработан.')
        self.stdout.write('\nТестовые данные успешно загружены в БД')
