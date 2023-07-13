from django_seed import Seed
from django.contrib.auth.hashers import make_password
from .models import Profile, ContactInfo, Category

def run():
    seeder = Seed.seeder()
    seeder.add_entity(Profile, 1, {
        'username': 'admin1',
        'password': make_password('1234'),
        'email': 'admin1@example.com',
        'first_name': 'Admin',
        'last_name': 'Role',
        'role': Profile.Role.ADMIN
    })

    seeder.add_entity(Profile, 1, {
        'username': 'web1',
        'password': make_password('1234'),
        'email': 'web1@example.com',
        'first_name': 'Web',
        'last_name': 'Role',
        'role': Profile.Role.WEB
    })

    seeder.add_entity(Profile, 1, {
        'username': 'stock1',
        'password': make_password('1234'),
        'email': 'stock1@example.com',
        'first_name': 'Stock',
        'last_name': 'Role',
        'role': Profile.Role.STOCK
    })

    seeder.add_entity(Profile, 1, {
        'username': 'membre1',
        'password': make_password('1234'),
        'email': 'membre1@example.com',
        'first_name': 'Membre',
        'last_name': 'Role',
        'role': Profile.Role.MEMBRE
    })

    inserted_pks = seeder.execute()
    print(inserted_pks)



def seed_contact_info():
    location = "Wonder Street, USA, New York"
    phone = "+01 321 654 214"
    email = "hello@xton.com"
    fax = "+123456789"
    contact_info, _ = ContactInfo.objects.get_or_create(
        defaults={'location': location, 'phone': phone, 'email': email, 'fax': fax}
    )

    print("Contact Info seeded.")

# Appelez cette fonction dans votre méthode seed_database()
seed_contact_info()

def seed_categories():
    seeder = Seed.seeder()

    # Seed for men category
    seeder.add_entity(Category, 1, {'name': 'men'})

    # Seed for women category
    seeder.add_entity(Category, 1, {'name': 'women'})

    # Seed for clothing category
    seeder.add_entity(Category, 1, {'name': 'clothing'})

    # Seed for shoes category
    seeder.add_entity(Category, 1, {'name': 'shoes'})

    seeder.execute()
    print("Categories seeded.")

# Call this function to seed the categories
seed_categories()


