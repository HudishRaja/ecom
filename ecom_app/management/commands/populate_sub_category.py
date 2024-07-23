from ecom_app.models import SubCategory,Category
from typing import Any
from django.core.management.base import BaseCommand
import os
from django.core.files import File


class Command(BaseCommand):
    help = "This comment inserts post data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        SubCategory.objects.all().delete()

        name = ['steel_almirah', 'steel_cots', 'steel_office_tables', 'steel_rack', 'steel_chairs', 'wooden_cot', 'sofa',
                'living_room', 'bed_room', 'kitchen', 'bathroom', 'office']
        # image = [
        #     'https://www.godrejinterio.com/imagestore/B2C/30161803SD01011/30161803SD01011_A2_500x500.jpg',
        #     'https://sparkenzy.com/cdn/shop/products/steelbed_500x500.jpg?v=1651588825',
        #     'https://image.made-in-china.com/2f0j00gUpqOAuWlmkK/Dining-Table-Set-Stainless-Steel-Table-Set-for-Hotel-Restaurant-Dining-Room.webp',
        #     'https://shop.gkwretail.com/cdn/shop/products/KitchenRacks39.4_SteelStandardKitchenRack_2.jpg?v=1649333266&width=1445',
        #     'https://www.starrynight.co.in/cdn/shop/products/Untitleddesign_1200x.jpg?v=1619675706',
        #     'https://m.media-amazon.com/images/I/71xJcws6-6L._AC_UF894,1000_QL80_.jpg',
        #     'https://pelicanessentials.com/cdn/shop/products/3a.jpg?v=1679067264&width=2048',
        #
        #     'https://images.pexels.com/photos/20952757/pexels-photo-20952757/free-photo-of-living-room-in-house.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        #     'https://images.pexels.com/photos/16951262/pexels-photo-16951262/free-photo-of-bed-in-bedroom.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        #     'https://images.pexels.com/photos/5556176/pexels-photo-5556176.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        #     'https://images.pexels.com/photos/14345209/pexels-photo-14345209.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        #     'https://images.pexels.com/photos/3143791/pexels-photo-3143791.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        #
        # ]

        # Base names to determine which base should be associated with each category
        image = [
            'steel_almirah.jpg', 'steel_cot.jpg', 'steel_office_table.jpg', 'steel_rack.jpg', 'steel_chair.jpg', 'wooden_cot.jpg', 'sofa.jpg', 'living_room.jpg', 'bed_room.jpg', 'kitchen.jpg', 'bathroom.jpg', 'office.jpg'
        ]
        furniture_base_names = ['steel_almirah', 'steel_cots', 'steel_office_tables', 'steel_rack', 'steel_chairs',
                                'wooden_cot', 'sofa']
        # Directory where your local images are stored
        photos_dir = os.path.join('media', 'image')

        # Fetch the Base objects
        furniture_base = Category.objects.get(name='furniture')
        interior_base = Category.objects.get(name='interior')
        # Create Category objects with the base foreign key
        for name, image in zip(name, image):
            category = furniture_base if name in furniture_base_names else interior_base
            file_path = os.path.join(photos_dir, image)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    sub_category = SubCategory(name=name, category=category)
                    sub_category.image.save(image, File(f), save=False)
                    sub_category.save()
            else:
                self.stdout.write(self.style.ERROR(f"File {file_path} does not exist"))

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))


