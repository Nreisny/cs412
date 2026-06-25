# File: dataAdder.py
# Author: Nicholas Reis (nreisny@bu.edu)
# Description:
# Deletes all existing Book Review data and reseeds the database
# with test users, profiles, books, characters, and comments.

from django.contrib.auth.models import User
from bookreview.models import *

# ---------------------------------------------------
# Delete Existing Data
# ---------------------------------------------------

CharacterComment.objects.all().delete()
BookCommment.objects.all().delete()
Character.objects.all().delete()
Book.objects.all().delete()
Profile.objects.all().delete()

User.objects.filter(
    username__in=[
        "alice",
        "mike",
        "sarah",
        "chris",
    ]
).delete()

# ---------------------------------------------------
# Create Test Users
# Password for every account: password123
# ---------------------------------------------------

alice_user = User.objects.create_user(
    username="alice",
    password="password123",
)

mike_user = User.objects.create_user(
    username="mike",
    password="password123",
)

sarah_user = User.objects.create_user(
    username="sarah",
    password="password123",
)

chris_user = User.objects.create_user(
    username="chris",
    password="password123",
)

# ---------------------------------------------------
# Profiles
# ---------------------------------------------------

alice = Profile.objects.create(
    user=alice_user,
    username="bookworm_alice",
    profile_image_url="https://picsum.photos/300?random=201",
    bio_text="Fantasy lover who always has another book on the shelf.",
)

mike = Profile.objects.create(
    user=mike_user,
    username="mystery_mike",
    profile_image_url="https://picsum.photos/300?random=202",
    bio_text="Detective novels are my favorite.",
)

sarah = Profile.objects.create(
    user=sarah_user,
    username="scifi_sarah",
    profile_image_url="https://picsum.photos/300?random=203",
    bio_text="Exploring galaxies one novel at a time.",
)

chris = Profile.objects.create(
    user=chris_user,
    username="classic_chris",
    profile_image_url="https://picsum.photos/300?random=204",
    bio_text="Collector of timeless literary classics.",
)

# ---------------------------------------------------
# Books
# ---------------------------------------------------

hobbit = Book.objects.create(
    name="The Hobbit",
    book_image_url="https://covers.openlibrary.org/b/id/14622863-L.jpg",
    synopsis="Bilbo Baggins embarks on an unexpected adventure with thirteen dwarves and Gandalf.",
    author="J.R.R. Tolkien",
    rating=9.5,
    numrating=2,
)

dune = Book.objects.create(
    name="Dune",
    book_image_url="https://covers.openlibrary.org/b/id/14352341-L.jpg",
    synopsis="Paul Atreides becomes the center of a struggle for the desert planet Arrakis.",
    author="Frank Herbert",
    rating=9.8,
    numrating=2,
)

sherlock = Book.objects.create(
    name="The Adventures of Sherlock Holmes",
    book_image_url="https://covers.openlibrary.org/b/id/8221256-L.jpg",
    synopsis="A collection of Sherlock Holmes' most famous investigations.",
    author="Arthur Conan Doyle",
    rating=9.2,
    numrating=2,
)

# ---------------------------------------------------
# Characters
# ---------------------------------------------------

bilbo = Character.objects.create(
    book=hobbit,
    name="Bilbo Baggins",
    character_image_url="https://picsum.photos/300?random=301",
    rating=10,
    numrating=1,
)

gandalf = Character.objects.create(
    book=hobbit,
    name="Gandalf",
    character_image_url="https://picsum.photos/300?random=302",
    rating=10,
    numrating=1,
)

thorin = Character.objects.create(
    book=hobbit,
    name="Thorin Oakenshield",
    character_image_url="https://picsum.photos/300?random=303",
    rating=9,
    numrating=1,
)

paul = Character.objects.create(
    book=dune,
    name="Paul Atreides",
    character_image_url="https://picsum.photos/300?random=304",
    rating=10,
    numrating=1,
)

chani = Character.objects.create(
    book=dune,
    name="Chani",
    character_image_url="https://picsum.photos/300?random=305",
    rating=9,
    numrating=1,
)

jessica = Character.objects.create(
    book=dune,
    name="Lady Jessica",
    character_image_url="https://picsum.photos/300?random=306",
    rating=9,
    numrating=1,
)

holmes = Character.objects.create(
    book=sherlock,
    name="Sherlock Holmes",
    character_image_url="https://picsum.photos/300?random=307",
    rating=10,
    numrating=1,
)

watson = Character.objects.create(
    book=sherlock,
    name="Dr. Watson",
    character_image_url="https://picsum.photos/300?random=308",
    rating=9,
    numrating=1,
)

moriarty = Character.objects.create(
    book=sherlock,
    name="Professor Moriarty",
    character_image_url="https://picsum.photos/300?random=309",
    rating=9,
    numrating=1,
)

# ---------------------------------------------------
# Book Comments
# ---------------------------------------------------

BookCommment.objects.create(
    profile=alice,
    book=hobbit,
    rating=10,
    text="A perfect adventure story that never gets old.",
)

BookCommment.objects.create(
    profile=mike,
    book=sherlock,
    rating=9,
    text="Every mystery is brilliantly written.",
)

BookCommment.objects.create(
    profile=sarah,
    book=dune,
    rating=10,
    text="The greatest science fiction novel I've ever read.",
)

BookCommment.objects.create(
    profile=chris,
    book=hobbit,
    rating=9,
    text="A classic that deserves every bit of its reputation.",
)

BookCommment.objects.create(
    profile=alice,
    book=dune,
    rating=9,
    text="Fantastic world building with unforgettable characters.",
)

# ---------------------------------------------------
# Character Comments
# ---------------------------------------------------

CharacterComment.objects.create(
    profile=alice,
    character=bilbo,
    rating=10,
    text="One of the best heroes in fantasy.",
)

CharacterComment.objects.create(
    profile=alice,
    character=gandalf,
    rating=10,
    text="Wise, powerful, and iconic.",
)

CharacterComment.objects.create(
    profile=mike,
    character=holmes,
    rating=10,
    text="The greatest detective ever written.",
)

CharacterComment.objects.create(
    profile=mike,
    character=moriarty,
    rating=9,
    text="A fantastic villain.",
)

CharacterComment.objects.create(
    profile=sarah,
    character=paul,
    rating=10,
    text="An incredibly complex protagonist.",
)

CharacterComment.objects.create(
    profile=sarah,
    character=chani,
    rating=9,
    text="A strong and memorable character.",
)

CharacterComment.objects.create(
    profile=chris,
    character=watson,
    rating=9,
    text="Often overlooked, but essential to the stories.",
)

CharacterComment.objects.create(
    profile=chris,
    character=thorin,
    rating=9,
    text="A proud king with an unforgettable journey.",
)

print("=" * 60)
print("Book Review database successfully reseeded!")
print()
print("Test Accounts")
print("-------------------------------")
print("Username: alice    Password: password123")
print("Username: mike     Password: password123")
print("Username: sarah    Password: password123")
print("Username: chris    Password: password123")
print("=" * 60)
