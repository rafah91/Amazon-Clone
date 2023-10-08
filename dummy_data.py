import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from products.models import Product , Brand , Review

def add_Brands(n):
    fake = Faker()
    images = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
    for x in range(n):
        Brand.objects.create(
            name = fake.name() ,
            image = f"brands/{images[random.randint(0,9)]}"
        )
    print(f'(n) brand was created successfully')

def add_products(n):
    pass

add_Brands(294)