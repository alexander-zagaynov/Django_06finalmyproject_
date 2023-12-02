from django.core.management.base import BaseCommand
from myproject.myapp2.models import User


class Command(BaseCommand):
    help = "Get all users."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')

