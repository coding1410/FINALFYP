from app import db  # import the database instance from the app module
from models import Product  # import the Product model from models

def init_db():
    db.drop_all()  # drop all tables from the database to start fresh
    db.create_all()  # create all tables based on the models defined

    # Sample products to populate the database
    products = [
        Product(name='Colorful Dog Collar', price=15.99, image='static/images/dog_collar.jpg', category='Accessories'),
        Product(name='Plush Dog Toy', price=9.99, image='static/images/dog_toy.jpg', category='Toys'),
        Product(name='Premium Dog Food', price=22.50, image='static/images/dog_food.jpg', category='Food'),
        Product(name='Dog Shampoo', price=8.45, image='static/images/dog_shampoo.jpg', category='Grooming')
    ]

    # Adding these products to the database session
    db.session.bulk_save_objects(products)
    db.session.commit()  # commit all changes to the database

if __name__ == "__main__":
    init_db()  # run the init_db function if the script is executed directly
