# AI GENERATED DATA FILE
# File: dataAdder.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/20/26
# Description: This is simply a page to add data to the backend

from bookreview.models import *

# Delete everything before reseeding

CharacterComment.objects.all().delete()
BookCommment.objects.all().delete()
Character.objects.all().delete()
Book.objects.all().delete()
Profile.objects.all().delete()

# Profiles

profiles = [
    Profile.objects.create(
        username="bookworm_alice",
        profile_image_url="https://images.unsplash.com/photo-1494790108377-be9c29b29330",
        bio_text="Fantasy lover and avid reader."
    ),
    Profile.objects.create(
        username="mystery_mike",
        profile_image_url="https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
        bio_text="Always looking for the next great mystery."
    ),
    Profile.objects.create(
        username="scifi_sarah",
        profile_image_url="https://images.unsplash.com/photo-1438761681033-6461ffad8d80",
        bio_text="Science fiction enthusiast."
    ),
    Profile.objects.create(
        username="classic_chris",
        profile_image_url="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d",
        bio_text="Collector of literary classics."
    ),
]

# Books

hobbit = Book.objects.create(
    name="The Hobbit",
    book_image_url="https://covers.openlibrary.org/b/id/14622863-L.jpg",
    synopsis="Bilbo Baggins joins a company of dwarves on an unexpected journey to reclaim treasure from a dragon.",
    author="J.R.R. Tolkien",
    rating=9,
    numrating=2,
)

dune = Book.objects.create(
    name="Dune",
    book_image_url="https://covers.openlibrary.org/b/id/14352341-L.jpg",
    synopsis="Paul Atreides becomes caught in a struggle for control of the desert planet Arrakis.",
    author="Frank Herbert",
    rating=10,
    numrating=1,
)

sherlock = Book.objects.create(
    name="The Adventures of Sherlock Holmes",
    book_image_url="https://covers.openlibrary.org/b/id/8221256-L.jpg",
    synopsis="Twelve classic detective stories featuring Sherlock Holmes and Dr. Watson.",
    author="Arthur Conan Doyle",
    rating=8,
    numrating=1,
)

# Characters

bilbo = Character.objects.create(
    book=hobbit,
    name="Bilbo Baggins",
    character_image_url="https://picsum.photos/300?random=101",
    rating=10,
    numrating=1,
)

gandalf = Character.objects.create(
    book=hobbit,
    name="Gandalf",
    character_image_url="https://picsum.photos/300?random=102",
    rating=10,
    numrating=1,
)

thorin = Character.objects.create(
    book=hobbit,
    name="Thorin Oakenshield",
    character_image_url="https://picsum.photos/300?random=103",
    rating=8,
    numrating=0,
)

paul = Character.objects.create(
    book=dune,
    name="Paul Atreides",
    character_image_url="https://picsum.photos/300?random=104",
    rating=10,
    numrating=1,
)

chani = Character.objects.create(
    book=dune,
    name="Chani",
    character_image_url="https://picsum.photos/300?random=105",
    rating=8,
    numrating=1,
)

jessica = Character.objects.create(
    book=dune,
    name="Lady Jessica",
    character_image_url="https://picsum.photos/300?random=106",
    rating=9,
    numrating=0,
)

holmes = Character.objects.create(
    book=sherlock,
    name="Sherlock Holmes",
    character_image_url="https://picsum.photos/300?random=107",
    rating=10,
    numrating=1,
)

watson = Character.objects.create(
    book=sherlock,
    name="Dr. Watson",
    character_image_url="https://picsum.photos/300?random=108",
    rating=9,
    numrating=0,
)

moriarty = Character.objects.create(
    book=sherlock,
    name="Professor Moriarty",
    character_image_url="https://picsum.photos/300?random=109",
    rating=9,
    numrating=1,
)

# Book Comments

BookCommment.objects.create(
    profile=profiles[0],
    book=hobbit,
    rating=9,
    text="One of the best fantasy adventures ever written."
)

BookCommment.objects.create(
    profile=profiles[1],
    book=sherlock,
    rating=8,
    text="The mysteries still hold up over a century later."
)

BookCommment.objects.create(
    profile=profiles[2],
    book=dune,
    rating=10,
    text="Amazing world-building and political intrigue."
)

BookCommment.objects.create(
    profile=profiles[3],
    book=hobbit,
    rating=9,
    text="A timeless classic that inspired generations."
)

# Character Comments

CharacterComment.objects.create(
    profile=profiles[0],
    character=bilbo,
    rating=10,
    text="Bilbo grows so much throughout the story."
)

CharacterComment.objects.create(
    profile=profiles[1],
    character=holmes,
    rating=10,
    text="The greatest fictional detective."
)

CharacterComment.objects.create(
    profile=profiles[2],
    character=paul,
    rating=10,
    text="One of the most complex protagonists in science fiction."
)

CharacterComment.objects.create(
    profile=profiles[3],
    character=gandalf,
    rating=10,
    text="Wise, mysterious, and always entertaining."
)

CharacterComment.objects.create(
    profile=profiles[0],
    character=chani,
    rating=8,
    text="A strong and memorable character."
)

CharacterComment.objects.create(
    profile=profiles[1],
    character=moriarty,
    rating=9,
    text="A perfect villain for Sherlock Holmes."
)

print("Database reset and reseeded successfully!")