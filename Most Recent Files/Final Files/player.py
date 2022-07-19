from items import *
from map import *

inventory = [items_lighter]

# Start game at the reception
current_room = rooms["Lobby"]

player = {
    "item": "squirt",
    "health": 100,
    "Dodge": 50,
    "attack": 5,
}
