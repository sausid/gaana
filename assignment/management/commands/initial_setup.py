import json
from django.core.management.base import BaseCommand
from assignment.models import Location


class Command(BaseCommand):
    help = 'Import JSON data into the Location model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

                for key, value in data.items():
                    Location.objects.update_or_create(
                        key=value.get('unlocs', [])[0],
                        defaults={
                            'name': value.get('name', ''),
                            'city': value.get('city', ''),
                            'country': value.get('country', ''),
                            'alias': value.get('alias', []),
                            'regions': value.get('regions', []),
                            'coordinates': value.get('coordinates', []),
                            'province': value.get('province', ''),
                            'timezone': value.get('timezone', ''),
                            'unlocs': value.get('unlocs', []),
                            'code': value.get('code', ''),
                        }
                    )

                self.stdout.write(self.style.SUCCESS('Data imported successfully.'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {json_file}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format.'))
