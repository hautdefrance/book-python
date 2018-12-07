from django.core.management.base import BaseCommand
from ksiazkaadresowa.models import Person


class Command(BaseCommand):
    help = 'Moj tekst pomocy'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            dest='file',
            nargs='?',
            help='Log File',
        )

        parser.add_argument(
            '--format',
            nargs='?',
            dest='format',
            help='Log File Format',
        )

    def handle(self, *args, **options):
        filename = options['file']
        format = options['format']
        content = []

        with open(filename) as file:
            for line in file:
                line = self.parse_line(line)
                content.append(line)

        print('\n'.join(content))
        return

        for p in Person.objects.all():
            p.first_name = p.first_name.title()
            p.last_name = p.last_name.title()
            p.save()

    def parse_line(self, line):
        return line.upper()
