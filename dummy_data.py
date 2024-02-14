import os , django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django.setup()



from faker import Faker
import random
from products.models import Product , Brand , Review
from django.contrib.auth.models import User


def add_users(n):
    for x in range(n):
        fake = Faker()
        User.objects.create(
            username = f"user_{x}",
            email = fake.email(),
            password = '12345'
        )


def add_brands(n):
    fake = Faker()
    images = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
    
    for x in range(n):
        Brand.objects.create(
            name = fake.name() , 
            image = f"brands/{images[random.randint(0,9)]}"
        )
    
    print(f'{n} Brands was created successfully')
    
    
def add_products(n):
    fake = Faker()
    images = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
    flags = ['Sale','New','Feature']
    brands = Brand.objects.all()
    
    for x in range(n):
        Product.objects.create(
            name = fake.name() , 
            name_ar = f'product-{x}',
            name_en = fake.name() , 
            subtitle = fake.text(max_nb_chars = 300) , 
            description = fake.text(max_nb_chars = 4000) , 
            image = f"products/{images[random.randint(0,9)]}",
            price = round(random.uniform(20.99,99.99),2) , 
            flag = flags[random.randint(0,2)] , 
            brand = random.choice(brands),
            sku = random.randint(1000,1000000) , 
            quantity = random.randint(5,100) , 
        ) 

    print(f'{n} Products was created successfully')




def add_reviews(n):
    fake = Faker()
    users = User.objects.all()
    products = Product.objects.all()
    
    for x in range(n):
        Review.objects.create(
            user = random.choice(users),
            product =  random.choice(products), 
            rate = random.randint(1,5) , 
            feedback = fake.text(max_nb_chars=200)
        )
        
    print(f'{n} Reviews was created successfully')


add_users(10)
add_brands(20)
add_products(100)
add_reviews(100)