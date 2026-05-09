from django.core.management.base import BaseCommand
from kanban.models import Column


class Command(BaseCommand):
    help = 'Creates the default Todo, In Progress, and Done columns'

    def handle(self, *args, **options):
        defaults = [('Todo', 0), ('In Progress', 1), ('Done', 2)]
        for name, order in defaults:
            col, created = Column.objects.get_or_create(name=name, defaults={'order': order})
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'{status}: {name}')
