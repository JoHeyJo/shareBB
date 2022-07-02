"""Seed file to make sample data for User & Listing db."""

from models import User, Listing, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Listing.query.delete()

###### User data ######
u1 = User(
    username="user1",
    password="testing1",
    first_name="fn1",
    last_name="ln1",
    email="test1@test1.com"
)

u2 = User(
    username="user2",
    password="testing2",
    first_name="fn2",
    last_name="ln2",
    email="test2@test2.com"
)

u3 = User(
    username="user3",
    password="testing3",
    first_name="fn3",
    last_name="ln3",
    email="test3@test3.com"
)

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)



###### Listing data ######

l1 = Listing(
    details="Wonderfully relaxing ice cold pool, water is harvested directly from the sierras",
    host_username="user1",
    image_url="http://first-bucket-r25.s3.amazonaws.com/pool.jpeg",
    listing_type="pool",
    location="Sierra Mountains",
    name="Alpine pool",
    price=10000.00

)

l2 = Listing(
    details="Tree house built right into one of the rarest and oldest tree in Yosemite, absolute beauty!",
    host_username="user2",
    image_url="http://first-bucket-r25.s3.amazonaws.com/treehouse.jpeg",
    listing_type="Balling Treehouse",
    location="Deep in the Yosemite National forest",
    name="Old Redwood Treehouse",
    price=100000.00

)

l3 = Listing(
    details="Lounge inside San Francisco's most luxuries box for two!",
    host_username="user3",
    image_url="http://first-bucket-r25.s3.amazonaws.com/box.jpeg",
    listing_type="Luxury Box",
    location="In the heart of beautiful San Francisco!",
    name="Luxury Box",
    price=10000000.00
)

l4 = Listing(
    details="The Presidio offers this modern construction of a bench, built with aesthetics in mind!",
    host_username="user3",
    image_url="http://first-bucket-r25.s3.amazonaws.com/bench.jpeg",
    listing_type="Opulent Bench",
    location="Nested in the Presidio",
    name="Modern Luxury Bench",
    price=100.00
)

l5 = Listing(
    details="Want to get away from the city? Want to feel like a kid again? Lounge on this TifBlair centipede grass lawn just like when you were a kid",
    host_username="user1",
    image_url="http://first-bucket-r25.s3.amazonaws.com/lawn.jpeg",
    listing_type="Luxurious Lawn",
    location="Danville",
    name="TifBlair Centipede Lawn",
    price=1000000.00
)

db.session.add(l1)
db.session.add(l2)
db.session.add(l3)
db.session.add(l4)
db.session.add(l5)

db.session.commit()
