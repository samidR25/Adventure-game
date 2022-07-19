import random
from Enemies import *
from player import *
from game import *
from map import *

#import time so functions dont print in one go

turn_counter = 0
dodge_value = 0
def Start_combat():
    global enemy
    #global current_room
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
            change_turn()
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
            change_turn()
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
    else:
        print("you have died")
        main()         #------------insert main() to loop back to rooms

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
                    print("---------------------------------------------------")
                    print("Landing this final blow you watch as gates falls to his knees,")
                    print("you've done it, you've put an end to his reign his,")
                    print("5G will no longer be working in conjunction the covid")
                    print("vaccine to turn people into zombies, you've saved the day!!!!")
                    print("---------------------------------------------------")
                else:    
                    print("---------------------------------------------------")
                    print("---landing the final blow "+ enemy +" finally falls---")
                    print("---------------------------------------------------")
                    inventory.append(items_key)
                    main()          #------------insert main() to loop back to rooms
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
