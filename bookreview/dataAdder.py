# File: dataAdder.py
# Author: Nicholas Reis (nreisny@bu.edu)
# Description:
# Deletes all existing Book Review data and reseeds the database
# with test users, profiles, books, characters, and comments.

# Fully AI generated for adding data

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
    username__in=["alice","mike","sarah","chris","emma"]
).delete()

# ---------------------------------------------------
# Users
# ---------------------------------------------------

alice_user = User.objects.create_user(username="alice", password="password123")
mike_user = User.objects.create_user(username="mike", password="password123")
sarah_user = User.objects.create_user(username="sarah", password="password123")
chris_user = User.objects.create_user(username="chris", password="password123")
emma_user = User.objects.create_user(username="emma", password="password123")

PROFILE_IMAGES = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLWqw_gHoOBrmRe6ZcZnwq_u1tRRF-F3OB06Fju-g_SUOpwAOeqWhEjejV&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTVoQDQGiBS3IEJQrXv4taMG-2-ISbs07ryUxkL3dtGc25couOnIU52RpR&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9c-FOGYuKyHP41hU8O-6R_GYczmSwnR4lcGlWoUkT7fSx0iCelN0X1l8&s=10",
    "https://preview.redd.it/who-is-this-man-and-why-is-he-everyones-profile-pic-v0-qzaf0v7wt8kd1.jpeg?auto=webp&s=3a43bf337f4d1e1ea55f152c5221ed33733fccca",
    "https://images.unsplash.com/photo-1628563694622-5a76957fd09c?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW5zdGFncmFtJTIwcHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D"
]

alice = Profile.objects.create(user=alice_user, username="bookworm_alice", profile_image_url=PROFILE_IMAGES[0], bio_text="Fantasy enthusiast who enjoys long immersive adventures.")
mike = Profile.objects.create(user=mike_user, username="mystery_mike", profile_image_url=PROFILE_IMAGES[1], bio_text="Always looking for the next great mystery novel.")
sarah = Profile.objects.create(user=sarah_user, username="scifi_sarah", profile_image_url=PROFILE_IMAGES[2], bio_text="Science fiction fan fascinated by epic worldbuilding.")
chris = Profile.objects.create(user=chris_user, username="classic_chris", profile_image_url=PROFILE_IMAGES[3], bio_text="Collector and reader of literary classics.")
emma = Profile.objects.create(user=emma_user, username="romance_reader", profile_image_url=PROFILE_IMAGES[4], bio_text="Reads everything from romance to historical fiction.")

# ---------------------------------------------------
# Books
# ---------------------------------------------------

books = [
(
    "Shadow Slave",
    "https://m.media-amazon.com/images/I/515fsT6ty4L._UF1000,1000_QL80_.jpg",
    "Guiltythree",
    """Born without privilege in a ruined future where humanity survives behind fortified cities, Sunny is forced into the deadly Nightmare Spell that grants supernatural abilities at a terrible cost. As he enters mysterious dream realms filled with ancient horrors, forgotten civilizations, and impossible monsters, he must rely on intelligence, caution, and ruthless determination to survive. Every victory uncovers new secrets about the Spell itself, transforming an unwilling survivor into one of the world's most dangerous Awakened while blurring the line between hero and monster."""
),
(
    "Lord of the Mysteries",
    "https://m.media-amazon.com/images/M/MV5BMWE1ZWYwZGUtZjRmOS00NzUzLTlkZmUtMTEwMjNhNTVmNDIwXkEyXkFqcGc@._V1_.jpg",
    "Cuttlefish That Loves Diving",
    """After awakening in the body of a recently deceased history graduate named Klein Moretti, an ordinary man finds himself trapped in a Victorian-inspired world filled with secret organizations, eldritch horrors, and mystical pathways to godlike power. As Klein uncovers hidden conspiracies and ancient beings that influence the fate of civilization, he carefully climbs the ranks of the supernatural while trying to preserve his humanity in a world where forbidden knowledge comes with unimaginable consequences."""
),
(
    "House of Leaves",
    "https://m.media-amazon.com/images/I/61yArGR8YkL._AC_UF1000,1000_QL80_.jpg",
    "Mark Z. Danielewski",
    """A young tattoo artist discovers a strange manuscript analyzing a documentary that may never have existed. The story gradually unfolds into an unsettling labyrinth where a family's home becomes impossibly larger on the inside than the outside, revealing endless corridors and shifting darkness. Blending horror, experimental typography, and multiple unreliable narrators, the novel explores obsession, fear, and the psychological effects of confronting the unknowable."""
),
(
    "Don Quixote",
    "https://images3.penguinrandomhouse.com/cover/9781101525371",
    "Miguel de Cervantes",
    """Inspired by tales of chivalry, an aging nobleman abandons his ordinary life and reinvents himself as the knight Don Quixote. Accompanied by his practical squire Sancho Panza, he embarks on a series of adventures where imagination constantly clashes with reality. Through humor, satire, and heartfelt moments, the novel examines idealism, friendship, and the enduring power of dreams despite an often indifferent world."""
),
(
    "Paradise Lost",
    "https://m.media-amazon.com/images/I/81c0iKCXgFL._UF1000,1000_QL80_.jpg",
    "John Milton",
    """This epic poem recounts the rebellion of Satan against Heaven, the creation of humanity, and the tragic fall of Adam and Eve. Through grand poetic language and philosophical reflection, Milton explores themes of free will, temptation, justice, redemption, and the consequences of pride. The work remains one of the most influential pieces of English literature for its rich symbolism and ambitious scope."""
),
(
    "Berserk Deluxe Volume 42",
    "https://preview.redd.it/volume-42-cover-v0-fti2eq2bz6mb1.jpg?auto=webp&s=576f1c296e49dbe07115cf63c2402380f7ae0986",
    "Kentaro Miura & Studio Gaga",
    """Following the devastating events that leave his companions shattered, the Black Swordsman Guts continues his relentless struggle against overwhelming darkness. Volume 42 carries forward Kentaro Miura's legendary story through the work of Studio Gaga, balancing breathtaking action with emotional character moments as the series moves toward its long-awaited conclusion while honoring Miura's vision."""
),
(
    "The Strange House",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRt0bnofmr8FilWBG2gILYdJPzzsGtvWTlhLmZo29pgs4ouAimzT-6vkMY&s=10",
    "Uketsu",
    """What begins as an investigation into an oddly designed house gradually transforms into a chilling mystery involving hidden rooms, disturbing architectural choices, and unexplained disappearances. As more clues emerge, seemingly unrelated events reveal a terrifying pattern that forces the investigators to question every assumption they have made about the building and the people connected to it."""
),
(
    "Alice's Adventures in Wonderland",
    "https://i0.wp.com/thebookhaze.com/wp-content/uploads/2026/01/image-22.png?resize=544%2C750&ssl=1",
    "Lewis Carroll",
    """After following a hurried white rabbit down an unexpected path, Alice finds herself in a fantastical world governed by dreamlike logic and eccentric inhabitants. As she encounters curious creatures, impossible riddles, and bizarre adventures, Alice learns to navigate a constantly changing landscape where imagination triumphs over ordinary rules and childhood curiosity is endlessly rewarded."""
),
(
    "The Cursed Bunny",
    "https://d3525k1ryd2155.cloudfront.net/h/892/956/1247956892.0.x.jpg",
    "Bora Chung",
    """Blending horror, fantasy, and social commentary, this collection of interconnected stories explores revenge, greed, isolation, and the darker aspects of modern society. Ordinary people encounter supernatural events that expose hidden fears and uncomfortable truths, creating unsettling tales that balance emotional depth with disturbing imagery and unforgettable twists."""
),
]

book_objs=[]
for title,img,author,synopsis in books:
    book_objs.append(Book.objects.create(
        name=title,
        book_image_url=img,
        synopsis=synopsis,
        author=author,
        rating=0,
        numrating=0
    ))

print("Books created:", len(book_objs))
print("Continue by adding Character.objects.create(...) and comments as desired.")
# ---------------------------------------------------
# Characters
# ---------------------------------------------------

# Shadow Slave
sunny = Character.objects.create(
    book=book_objs[0],
    name="Sunny",
    rating=0,
    numrating=0,
)

nephis = Character.objects.create(
    book=book_objs[0],
    name="Nephis",
    rating=0,
    numrating=0,
)

cassie = Character.objects.create(
    book=book_objs[0],
    name="Cassie",
    rating=0,
    numrating=0,
)

# Lord of the Mysteries
klein = Character.objects.create(
    book=book_objs[1],
    name="Klein Moretti",
    rating=0,
    numrating=0,
)

audrey = Character.objects.create(
    book=book_objs[1],
    name="Audrey Hall",
    rating=0,
    numrating=0,
)

leonard = Character.objects.create(
    book=book_objs[1],
    name="Leonard Mitchell",
    rating=0,
    numrating=0,
)

# House of Leaves
johnny = Character.objects.create(
    book=book_objs[2],
    name="Johnny Truant",
    rating=0,
    numrating=0,
)

zampano = Character.objects.create(
    book=book_objs[2],
    name="Zampanò",
    rating=0,
    numrating=0,
)

navidson = Character.objects.create(
    book=book_objs[2],
    name="Will Navidson",
    rating=0,
    numrating=0,
)

# Don Quixote
don = Character.objects.create(
    book=book_objs[3],
    name="Don Quixote",
    rating=0,
    numrating=0,
)

sancho = Character.objects.create(
    book=book_objs[3],
    name="Sancho Panza",
    rating=0,
    numrating=0,
)

dulcinea = Character.objects.create(
    book=book_objs[3],
    name="Dulcinea del Toboso",
    rating=0,
    numrating=0,
)

# Paradise Lost
satan = Character.objects.create(
    book=book_objs[4],
    name="Satan",
    rating=0,
    numrating=0,
)

adam = Character.objects.create(
    book=book_objs[4],
    name="Adam",
    rating=0,
    numrating=0,
)

eve = Character.objects.create(
    book=book_objs[4],
    name="Eve",
    rating=0,
    numrating=0,
)

# Berserk Deluxe Volume 42
guts = Character.objects.create(
    book=book_objs[5],
    name="Guts",
    rating=0,
    numrating=0,
)

casca = Character.objects.create(
    book=book_objs[5],
    name="Casca",
    rating=0,
    numrating=0,
)

griffith = Character.objects.create(
    book=book_objs[5],
    name="Griffith",
    rating=0,
    numrating=0,
)

# The Strange House
amemiya = Character.objects.create(
    book=book_objs[6],
    name="Amemiya",
    rating=0,
    numrating=0,
)

kurihara = Character.objects.create(
    book=book_objs[6],
    name="Kurihara",
    rating=0,
    numrating=0,
)

yuzuki = Character.objects.create(
    book=book_objs[6],
    name="Yuzuki",
    rating=0,
    numrating=0,
)

# Alice's Adventures in Wonderland
alice = Character.objects.create(
    book=book_objs[7],
    name="Alice",
    rating=0,
    numrating=0,
)

mad_hatter = Character.objects.create(
    book=book_objs[7],
    name="The Mad Hatter",
    rating=0,
    numrating=0,
)

cheshire = Character.objects.create(
    book=book_objs[7],
    name="The Cheshire Cat",
    rating=0,
    numrating=0,
)

# The Cursed Bunny
bunny = Character.objects.create(
    book=book_objs[8],
    name="The Cursed Bunny",
    rating=0,
    numrating=0,
)

grandmother = Character.objects.create(
    book=book_objs[8],
    name="The Grandmother",
    rating=0,
    numrating=0,
)

fox = Character.objects.create(
    book=book_objs[8],
    name="The Fox Spirit",
    rating=0,
    numrating=0,
)