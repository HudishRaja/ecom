from ecom_app.models import Category
from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command inserts base data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Category.objects.all().delete()

        # List of base names to insert
        base_names = [
            'furniture', 'interior'

        ]

        # Create Base objects
        for name in base_names:
            Category.objects.create(name=name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Base data!"))