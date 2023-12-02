from django.core.management.base import BaseCommand
from myproject.myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', password='secret', age=25)
        user = User(name='Alexander', email='john@example.com', password='secret', age=35)
        user = User(name='Ivan', email='john@example.com', password='secret', age=45)
        user = User(name='Elena', email='john@example.com', password='secret', age=24)
        user.save()
        self.stdout.write(f'{user}')



