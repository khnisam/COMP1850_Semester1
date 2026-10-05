# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

Deftones = ["White Pony", "Around the Fur", "Adrenaline"]
Kreator = ["Coma of Souls", "Extreme Aggression", "Terrible Certainty"]
Metallica = ["Ride the Lightning", "Master of Puppets", "The Black Album"]

musicDatabase = {
   "Deftones": Deftones,
   "Kreator": Kreator,
   "Metallica": Metallica
}


# Pretty-print the data structure

pprint(musicDatabase)

# Display details of one album recorded by a specific artist

album = musicDatabase.get("Deftones")
print(album)
print(album[0])

