from items import *

room_lobby = {
    "name": "Lobby",

    "description" :
    """You are in the lobby of Bill Gates' house. 
On the wall to your right is a 6-foot-wide limestone fire place, 
on the other wall you will find a 22-foot-wide video screen.
There are corridors leading north to the study, south to the garden, west to the kitche and a 
stairwell heading east to the cellar.
""",
    "exits" : {"north": "Study", "east": "Cellar", "south": "Garden", "west": "Kitchen"},

    "enemies" : "",
    
    "items": [items_crystals, items_northface_puffer]

}

room_garden = {     #Outside
    "name" : "Garden",

    "description" : """You are in the garden. Around you are several exotic plants and 
a maple tree that Bill Gates planted 40 years ago.You can go north to the lobby, east to the pond or west to the boathouse""",

    "exits" : {"north" : "Lobby", "east" : "Pond", "west" : "Boathouse"},
    
    "items": [items_shovel],
    
    "enemies" : ""
            
}

room_boathouse = {      #Connected to garden
    "name" : "Boathouse",

    "description" : """You are in the boathouse. Inside is fishing equipment and 
    pictures of Bill Gates and Warren Buffet out on a fishing trip.
    You can go east to the garden.

""",

    "exits" : {"east" : "Garden"},

    "items": [items_fuel_can],
    
    "enemies" : ""

}

room_pond = {           #Connected to garden
    "name" : "Pond",

    "description" : """You are at the pond.
There is duckweed and frogbit floating on the surface of 
the muddy water. You can go west to the Garden.
""",

    "exits" : {"west" : "Garden"},

    "enemies" : "",

    "items": [items_squirty_bottle]

}

room_kitchen = {        #Puzzle room
    "name" : "Kitchen",

    "description" : """You are in the kitchen.
Inside you see the cupboards open without anything in them.
You can go east to the lobby.
""",

    "exits" : {"east" : "Lobby"},

    "enemies" : "",

    "items": []

}

room_cellar = {         #Boris Johnson fight
    "name" : "Cellar",

    "description" : """You are in the cellar. Inside
you find a fine selection of wines.
You can go west to the lobby.
""",

    "exits" : {"west" : "Lobby"},

    "enemies" : "Bojo",

    "items": [items_key]


}

room_study = {          #Bill Gates fight
    "name" : "Study",

    "description" : """You are in the study room. 
Around you are several books on vaccines and plans to take 
over the world. You can go south to the lobby.
""",

    "exits" : {"south" : "Lobby"},

    "items": [],

    "enemies" : "Gates"

}


rooms = {
    "Lobby" : room_lobby,
    "Garden" : room_garden,
    "Boathouse" : room_boathouse,
    "Pond" : room_pond,
    "Kitchen" : room_kitchen,
    "Cellar" : room_cellar,
    "Study" : room_study

}
