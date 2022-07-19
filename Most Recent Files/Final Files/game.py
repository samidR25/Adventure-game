#!/usr/bin/python3
import random
from time import sleep 
from map import rooms
from player import *
from items import *
from gameparser import *
from puzzle import *
from Enemies import *
import sys
#--------------------------------------------------------------------------------

def list_of_items(items):

    comma_list = []
    for item in items:
        comma_list.append(item["name"])
    return(", ".join(comma_list))


def print_room_items(room):


    if room["items"] == []:
        return 
    else:
        print("There is", list_of_items(room["items"]), "here.")
        print()
                   



def print_inventory_items(items):

    print("You have",list_of_items(inventory)+".")
    print()
    

def print_room(room):

    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()

   
    print_room_items(room)
    

def exit_leads_to(exits, direction):

        return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):

        print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print("TAKE", item["id"].upper(), "to take", item["name"])

    for item in inv_items:
        print("DROP", item["id"].upper(), "to drop", item["name"])

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):

    return chosen_exit in exits


def execute_go(direction):

    global current_room
    
    if direction in current_room["exits"]:
        new_room = current_room["exits"][direction]
        print(new_room)
        current_room = rooms[new_room]
    else:
        print("You cannot go there.")


def calc_mass(inventory, item):

    mass = 0
    
    for i in inventory:
        mass = mass + i["mass"]

    if mass + item["mass"] > 3:
        print("There is no more room in your bag to carry this item.")
        return False
    else:
        return True


def execute_take(item_id):


    global current_room
    y = False


    for i in current_room["items"]:
        if i["id"] == item_id:
            items = i
            
           # if calc_mass(inventory, items):
            current_room["items"].remove(items)
            inventory.append(items)
            y = True

    if y == False:
        print("You cannot take that")



def execute_drop(item_id):


    global current_room
    x = False


    for i in inventory:
        if i["id"] == item_id:
            item = i
            inventory.remove(item)
            current_room["items"].append(item)
            x = True
            
    if x == False:
        print("You cannot drop that")

#---------------------------------------------------------------------------------
#PUZZLEROOM CODE

        
def print_intro(intro): #print the intro
    print(intro["story"])


def print_chemicals(chemicals): #funtion to print the chemicals option
    chemicals_order = collections.OrderedDict(chemicals) #put the chemicals in order
    print("Use these chemicals to make hydrofluoric acid!!!")
    
    for element in chemicals_order:
        print(element, ":", chemicals[element])



def mix_chemicals(possible_answer, user_input): # mix the chemicals and give out the result
    for key in possible_answer:
        if user_input == key:
            result = possible_answer[key]
            print("You have created", result)

       
       
def valid_answer(possible_answer, user_input): #check whether the user input is valid
    if user_input in possible_answer:
        return mix_chemicals(possible_answer,user_input)
    else:
        print("Invalid input.")


def menu2(possible_answer):
    #read player's input
    user_input = input ("> ")

    #normalised user input????

    #check whether the input is valid
    valid_answer(possible_answer, user_input)


    return valid_answer

def puzzleroom():
    print_intro(intro)
    print_chemicals(chemicals)


    user_input = input("> ")
    user_input = ''.join(user_input.split())
    
    x = False
    
    while x == False:
        
        if user_input != "1+2":
            valid_answer(possible_answer, user_input)
            user_input = input("> ")
            user_input = ''.join(user_input.split())
            
        elif user_input == "1+2":
            x = True
            

    else:
        print("Well done!! Chemicals have been added to your inventory")
        inventory.append(items_chemicals)
        #return
       
    
#-------------------------------------------------------------------------------
def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):


    # Next room to go to
    return rooms[exits[direction]]

#---------------------------------------------------------------------------------------

def check_inventory():
    
    have_chemicals = False
           
    for i in inventory:
        if i["id"] == "chemicals":
            have_chemicals = True
        
    if have_chemicals == False:
        puzzleroom()



def check_inventory2():

     have_bomb = False

     for i in inventory:
         if i["id"] == "bomb":
             have_bomb = True


     if have_bomb == False:
         print("""
You venture down the twisted stairs to Gates’ cellar, in the distance you hear glass smashing,
your approach tense with fear, getting closer the air fills with what sound like the mumbling of a madman chanting lies about affordable private healthcare and free school meals.
Rounding the corner you see Boris Johnson another key character in this conspiracy downing bottles of expensive wine.
He catches your eye, approaching I what is more of a drunk stumble than a walk you have no option but to fight.""")
         Start_combat()

def check_inventory3():

    have_bomb = False

    for i in inventory:
         if i["id"] == "bomb":
             have_bomb = True


    if have_bomb == True:
        print("""
You open the ominous door ahead of you, it leads to a long corridor, draped in modern art you can only assume is being used to avoid tax,
moving to the end of the corridor you approach a large oak door, you push it open to see your sworn enemy Bill sat at his desk.
“Well done you’ve got this far but now you must face my 5g powers!”
Floating into the air gates starts to crackle with 5G energy. You ready your trust squirty bottle once more and prepare for the final battle.""")
        Start_combat()

    

def squirtybottle():

    have_chemicals = False
    have_bottle = False
    have_shovel = False

    for i in inventory:
        if i["id"] == "chemicals":
            have_chemicals = True

    for i in inventory:
        if i["id"] == "bottle":
            have_bottle = True

    for i in inventory:
        if i["id"] == "shovel":
            have_shovel = True

    if have_chemicals == True and have_bottle == True:
        inventory.append(items_squirty_with_chemicals)
        inventory.remove(items_squirty_bottle)
        inventory.remove(items_chemicals)
        print("You have put the chemicals into your squirty bottle!")

            
    if have_chemicals == True:
        player["attack"] = player["attack"] + 5
        print("Your attack stats have increased by 5!")
        print_player()


def pufferjacket():

    have_puffer = False

    for i in inventory:
        if i["id"] == "puffer":
            have_puffer = True
            inventory.remove(items_northface_puffer)

    if have_puffer == True:
        player["Dodge"] = 70
        print("Your dodge stats have increased by 20!")
        print_player()

def crystals():

    have_crystals = False

    for i in inventory:
        if i["id"] == "crystals":
            have_crystals = True

    if have_crystals == True:
        player["health"] = player["health"] + 50
        print("Your health has increased by 50!")
        inventory.remove(items_crystals)
        print_player()

def shovel():

    have_shovel = False
    have_squirtychemicals = False

    for i in inventory:
        if i["id"] == "shovel":
            have_shovel = True
            inventory.remove(items_shovel)


    if have_shovel == True:
        player["attack"] = player["attack"] + 2
        print("Your attack stats have increased slightly!")
        print_player()

    


#--------------------------------------------------------------------------
#COMBAT CODE

turn_counter = 0
dodge_value = 0
def Start_combat():
    global enemy
    global current_room
    if current_room["name"] == "Cellar":
        enemy = "Bojo"
        Turn_timer(enemy)
    elif current_room["name"] == "Study":
        enemy= "Gates"
        Turn_timer(enemy)
    else:
        print(current_room["name"])

    print_player()
    

def print_player():
    print()
    print("Player Stats:")
    print("health: "+ str(player["health"]), "Dodge: "+ str(player["Dodge"]), "attack: "+ str(player["attack"]))
    print()

def print_enemy(enemy):
    Current_fighter = enemies[enemy]
    print(print("health: "+ str(Current_fighter["health"]), "attack: "+ str(Current_fighter["attack"])))

def Turn_timer(enemy):
    global turn_counter
    if turn_counter == 0:
        enemy_damage(enemy)
    else:
        player_damage(enemy)


def player_damage(enemy):
    global turn_counter
    global dodge_value
    Current_fighter = enemies[enemy]
    fighter_damage = Current_fighter["attack"] + random.randint( 0, 15)
    if dodge_value == 0:
        hit_chance = random.randint(0,2)
        if hit_chance >= 1:
            player_take_damage(fighter_damage)
            
        elif hit_chance < 1:
            print("The enemy swings and miss'")
            print("-----------------------------")
            change_turn()
    else:
        hit_chance = random.randint(0,8)
        if hit_chance > 7:
            print("Even with you fast dodge you couldn't avoid the attack")
            print("-----------------------------")
            player_take_damage(fighter_damage)
            
        else:
            print("your dexterity allows you narrowly avoid the an attack")
            print("-----------------------------")
            print_player()
            change_turn()


def change_turn():
    global enemy
    global turn_counter
    if turn_counter == 0:
        turn_counter = 1
        Turn_timer(enemy)
    else:
        turn_counter = 0
        Turn_timer(enemy)

def player_take_damage(fighter_damage):
    player["health"] = player["health"] - fighter_damage
    if player["health"] > 0:
        print("You get caught with an attack")
        print("-----------------------------")
        print_player()
        change_turn()
    else:
        player_death()
        
def player_death():
    print("Taking the brunt of the damage from this last hit you know")
    print("no ammount of essential oils or incense could fix these wounds,")
    print("you collapse, a valiant but futile effort, too little to late.")
    print("Gates has won and will continue to lead his zombie army.")
    sys.exit()

def enemy_damage(enemy):
                             
    global dodge_value
    global turn_counter
    Current_fighter = enemies[enemy]
    player_choice = int(input("input 1 to fight or 2 to dodge: " ))
    print()
    if player_choice == 1:
        hit_chance = random.randint(1,6)
        if hit_chance > 1:
            Current_fighter["health"] = Current_fighter["health"] - player["attack"]
            print("-----------------------------")
            enemy_health_state(enemy)
            print()
            if Current_fighter["health"] < 0:
                if enemy == "Gates":
                    have_lighter = False
                    have_fuel = False       
                    for i in inventory:
                        if i["id"] == "lighter":
                            have_lighter = True
                        if i["id"] == "fuel":
                             have_fuel = True
                             
                    if have_lighter == True and have_fuel == True:
                        
                        print("---------------------------------------------------")
                        print("Landing this final blow you watch as gates falls to his knees,")
                        print("you've done it, you've put an end to his reign, and destroyed hi 5g tower,")
                        print("5G will no longer be working in conjunction with the covid")
                        print("vaccine to turn people into zombies, you've saved the day!!!!")
                        print("You douse the room with the fule you found earlier, as you leave you drop the lighter")
                        print("at you feet setting a blaze to the study burning the sacred tomes of forbidden knowledge,")
                        print("ensuring that this kind of disatster will never happpen again")
                        print("---------------------------------------------------")
                        sys.exit()

                    else:
                        print("---------------------------------------------------")
                        print("Landing this final blow you watch as gates falls to his knees,")
                        print("you've done it, you've put an end to his reign, and destroyed hi 5g tower,")
                        print("5G will no longer be working in conjunction with the covid")
                        print("vaccine to turn people into zombies, you've saved the day!!!!")
                        print("---------------------------------------------------")
                        sys.exit()
                
                
                else:    
                    print("---------------------------------------------------")
                    print("---landing the final blow "+ enemy +" finally falls---")
                    print("---------------------------------------------------")
                    print("")
                    print("----------------------------------------------------")
                    print("-------Bojo has dropped an explosive device.------")
                    print("---This could possibly take down a small structure...---")
                    print("--------------------------------------------------------")
                    inventory.append(items_key)
                             #------------insert main() to loop back to rooms
            else:
                change_turn()
        elif hit_chance == 6:
            print("a critical stike!!")
            Current_fighter["health"] = Current_fighter["health"] - (player["attack"])
            change_turn()
        else:
            print("-----------------------------")
            print("swing and a miss")
            print()
            change_turn()
    else:
        a = player["Dodge"]*round(random.uniform(1,4),3)
        if a > 70:
            print("-----------------------------")
            print("you dive out of the way")
            print()
            dodge_value = 1
            change_turn()
        else:
            print("-----------------------------")
            print("you try and dodge but trip in the process")
            print()
            dodge_value = 0
            change_turn()

def enemy_health_state(enemy):
    if enemies[enemy]["health"] > (enemies[enemy]["max_health"]* 0.75):
        print("You use your",  player["item"], "to land the first hit against the enemy" )
    elif  enemies[enemy]["health"] < (enemies[enemy]["max_health"]* 0.75) and enemies[enemy]["health"] > (enemies[enemy]["max_health"]* 0.50):
        print("attacking this time " + enemy + " starts to show signs of damage but stands stong")
    elif enemies[enemy]["health"] < (enemies[enemy]["max_health"]* 0.50) and enemies[enemy]["health"] > (enemies[enemy]["max_health"]* 0.25):
        if enemy == "Gates":
            print("you watch as Gates body fires up with 5G energy")
        else:
            print("upon dealing this blow you notice " + enemy + " starts to look weak")
    
    elif enemies[enemy]["health"] < (enemies[enemy]["max_health"]* 0.25) and enemies[enemy]["health"] >  0:
        print("this stike seems to be one of the last the enemy seems very weak")
    elif enemies[enemy]["health"] < 0:
        return 0

#----------------------------------------------------------------------------------

    #This is the entry point of our program
def main():
    from map import room_lobby
    print("""
            .___________..______       __    __  .___________. __    __          _______. _______  _______  __  ___  _______ .______          _______.
            |           ||   _  \     |  |  |  | |           ||  |  |  |        /       ||   ____||   ____||  |/  / |   ____||   _  \        /       |
            `---|  |----`|  |_)  |    |  |  |  | `---|  |----`|  |__|  |       |   (----`|  |__   |  |__   |  '  /  |  |__   |  |_)  |      |   (----`
                |  |     |      /     |  |  |  |     |  |     |   __   |        \   \    |   __|  |   __|  |    <   |   __|  |      /        \   \    
                |  |     |  |\  \----.|  `--'  |     |  |     |  |  |  |    .----)   |   |  |____ |  |____ |  .  \  |  |____ |  |\  \----.----)   |   
                |__|     | _| `._____| \______/      |__|     |__|  |__|    |_______/    |_______||_______||__|\__\ |_______|| _| `._____|_______/
                """)

    print("")
    print("""
The year is 2022
The evil covid vaccine has turned the population to zombies.
you and your band of antivaxxers have been preaching of this fortune and no one listened.
the creator of the vaccine is obvious, Bill gates.
storm his mansion avoiding the zombies and his 5G powers.""")
          

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)

        
        print_room(current_room)
        print_inventory_items(inventory)
    

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        if current_room["name"] == "Kitchen":
            check_inventory()


        elif current_room["name"] == "Cellar":
            check_inventory2()

        elif current_room["name"] == "Study":
            check_inventory3()


        squirtybottle()
        pufferjacket()
        crystals()
        shovel()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
