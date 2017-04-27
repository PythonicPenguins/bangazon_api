from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Loads content data.'

    def handle(self, **options):
        call_command('loaddata', 'customers.json')
        call_command('loaddata', 'paymenttypes.json')
        call_command('loaddata', 'orders.json')
        call_command('loaddata', 'producttype.json')
        call_command('loaddata', 'products.json')
        call_command('loaddata', 'orderproduct.json')
        call_command('loaddata', 'customerissues.json')
        call_command('loaddata', 'departments.json')
        call_command('loaddata', 'computers.json')
        call_command('loaddata', 'employees.json')
        call_command('loaddata', 'training.json')
        call_command('loaddata', 'trainingsessions.json')
