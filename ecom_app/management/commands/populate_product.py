from ecom_app.models import Products, Category
from typing import Any
from django.core.management.base import BaseCommand
import os
from django.core.files import File


class Command(BaseCommand):
    help = "This comment inserts post data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Products.objects.all().delete()

        id_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        image = [
            'almirah01.jpg', 'almirah02.jpg', 'almirah03.jpg',
            'cot01.jpg', 'cot02.jpg', 'cot03.jpg',
            'table01.jpg', 'table02.jpg', 'table03.jpg',
            'rack01.jpg', 'rack02.jpg', 'rack03.jpg',
            'chair01.jpg', 'chair02.jpg', 'chair03.jpg',
            'wooden_cot01.jpg', 'wooden_cot02.jpg', 'wooden_cot03.jpg',
            'sofa01.jpg', 'sofa02.jpg', 'sofa03.jpg'



        ]
        sub_category = [
            'steel_almirah', 'steel_almirah', 'steel_almirah',
            'steel_cots', 'steel_cots', 'steel_cots',
            'steel_office_tables', 'steel_office_tables', 'steel_office_tables',
            'steel_rack', 'steel_rack', 'steel_rack',
            'steel_chairs', 'steel_chairs', 'steel_chairs',
            'wooden_cot', 'wooden_cot', 'wooden_cot',
            'sofa', 'sofa', 'sofa'

        ]
        name = ['ALMIRAH 01', 'ALMIRAH 02', 'ALMIRAH 03',
                'STEEL COT 01', 'STEEL COT 02', 'STEEL COT 03',
                'OFFICE TABLE 01', 'OFFICE TABLE 02', 'OFFICE TABLE 03',
                'RACK 01', 'RACK 02', 'RACK 03',
                'CHAIR 01', 'CHAIR 02', 'CHAIR 03',
                'WOODEN COT 01', 'WOODEN COT 02', 'WOODEN COT 03',
                'SOFA 01', 'SOFA 02', 'SOFA 03'
                ]
        specification = [
            {'Material': 'Steel', 'Dimensions': '180 cm x 90 cm x 45 cm', 'Color': 'Various',
             'Features': 'Lockable, Adjustable shelves'},
            {'Material': 'Steel', 'Dimensions': '180 cm x 90 cm x 45 cm', 'Color': 'Various',
             'Features': 'Lockable, Adjustable shelves'},
            {'Material': 'Steel', 'Dimensions': '180 cm x 90 cm x 45 cm', 'Color': 'Various',
             'Features': 'Lockable, Adjustable shelves'},
            {'Material': 'Steel', 'Dimensions': '200 cm x 90 cm x 45 cm', 'Color': 'Various',
             'Features': 'Durable, Powder-coated'},
            {'Material': 'Steel', 'Dimensions': '200 cm x 90 cm x 45 cm', 'Color': 'Various',
             'Features': 'Durable, Powder-coated'},
            {'Material': 'Steel', 'Dimensions': '200 cm x 90 cm x 45 cm', 'Color': 'Various',
             'Features': 'Durable, Powder-coated'},
            {'Material': 'Steel with plywood top', 'Dimensions': '120 cm x 60 cm x 75 cm', 'Color': 'Various',
             'Features': 'Drawer included, Rust-resistant'},
            {'Material': 'Steel with plywood top', 'Dimensions': '120 cm x 60 cm x 75 cm', 'Color': 'Various',
             'Features': 'Drawer included, Rust-resistant'},
            {'Material': 'Steel with plywood top', 'Dimensions': '120 cm x 60 cm x 75 cm', 'Color': 'Various',
             'Features': 'Drawer included, Rust-resistant'},
            {'Material': 'Steel', 'Dimensions': '150 cm x 75 cm x 30 cm', 'Color': 'Various',
             'Features': 'Adjustable shelves, High load capacity'},
            {'Material': 'Steel', 'Dimensions': '150 cm x 75 cm x 30 cm', 'Color': 'Various',
             'Features': 'Adjustable shelves, High load capacity'},
            {'Material': 'Steel', 'Dimensions': '150 cm x 75 cm x 30 cm', 'Color': 'Various',
             'Features': 'Adjustable shelves, High load capacity'},
            {'Material': 'Steel', 'Dimensions': '45 cm x 45 cm x 90 cm', 'Color': 'Various',
             'Features': 'Stackable, Comfortable'},
            {'Material': 'Steel', 'Dimensions': '45 cm x 45 cm x 90 cm', 'Color': 'Various',
             'Features': 'Stackable, Comfortable'},
            {'Material': 'Steel', 'Dimensions': '45 cm x 45 cm x 90 cm', 'Color': 'Various',
             'Features': 'Stackable, Comfortable'},
            {'Material': 'Wood', 'Dimensions': '200 cm x 150 cm x 45 cm', 'Color': 'Various',
             'Features': 'Durable, Classic design'},
            {'Material': 'Wood', 'Dimensions': '200 cm x 150 cm x 45 cm', 'Color': 'Various',
             'Features': 'Durable, Classic design'},
            {'Material': 'Wood', 'Dimensions': '200 cm x 150 cm x 45 cm', 'Color': 'Various',
             'Features': 'Durable, Classic design'},
            {'Material': 'Fabric/Leather with wooden frame', 'Dimensions': '200 cm x 90 cm x 85 cm', 'Color': 'Various',
             'Features': 'Comfortable, Modern design'},
            {'Material': 'Fabric/Leather with wooden frame', 'Dimensions': '200 cm x 90 cm x 85 cm', 'Color': 'Various',
             'Features': 'Comfortable, Modern design'},
            {'Material': 'Fabric/Leather with wooden frame', 'Dimensions': '200 cm x 90 cm x 85 cm', 'Color': 'Various',
             'Features': 'Comfortable, Modern design'},


        ]
        price = [
            15000,  # steel_almirah
            18000,  # steel_almirah
            16000,  # steel_almirah
            20000,  # steel_cots
            22000,  # steel_cots
            21000,  # steel_cots
            8000,  # steel_office_tables
            8500,  # steel_office_tables
            8200,  # steel_office_tables
            6000,  # steel_rack
            6500,  # steel_rack
            6200,  # steel_rack
            3000,  # steel_chairs
            3200,  # steel_chairs
            3100,  # steel_chairs
            25000,  # wooden_cot
            26000,  # wooden_cot
            25500,  # wooden_cot
            35000,  # sofa
            36000,  # sofa
            35500,  # sofa


        ]

        photos_dir = os.path.join('media', 'image')
        # Fetch the Base objects
        # furniture_base = Category.objects.get(name='furniture')
        # interior_base = Category.objects.get(name='interior')
        for id_num, image, sub_category, name, specification, price in zip(id_num, image, sub_category, name, specification, price):
            # base = furniture_base if sub_category in furniture_base_names else interior_base
            file_path = os.path.join(photos_dir, image)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    product = Products(id_num=id_num, image=image, sub_category=sub_category, name=name, specification=specification, price=price)
                    product.image.save(image, File(f), save=False)
                    product.save()
            # Products.objects.create(id_num=id_num, img_url=img_url, sub_category=sub_category, name=name, specification=specification, price=price)
            else:
                self.stdout.write(self.style.ERROR(f"File {file_path} does not exist"))

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
