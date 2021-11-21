from magic import Spell
from item import Item
from character import Character
import random

# Create magic
#                  name | dmg | cost (vb)
thunder = Spell("Thunder", 500, 60)
lightning = Spell("Lightning", 600, 75)
fire = Spell("Fire", 400, 50)
earthquake = Spell("Earthquake", 400, 50)
 
# Create Some Items
#                              name | type | description | value
black_potion = Item("Black Potion", "potion", "Heals 50 HP", 50)
blue_potion = Item("Blue Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Full restores HP/VB", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)
 
enemy_spells = [fire]
player_spells = [fire, thunder, fire, earthquake]
player_items = [{"item": black_potion, "quantity": 15}, {"item": blue_potion, "quantity": 5}, 
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5}, 
                {"item": grenade, "quantity": 5}]


player1 = Character("Player:", 20000, 500, 1500, player_spells, player_items, 500)

enemy1 = Character("Demon", 12000, 1, 400, enemy_spells, [], 0)
enemy2 = Character("Dragon", 11000, 1, 300, enemy_spells, [], 0)
enemy3 = Character("Ghost", 10000, 1, 200, enemy_spells, [], 0)
 
enemies = [enemy1, enemy2, enemy3]
 
players = [player1]

game = True
while game == True:
    print("===================")
    
    print("\n\n")
        
    for player in players:
        player.get_stats()

    for enemy in enemies:
        enemy.get_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose Action: ")
        # Index is a variable that takes the value of choice and subtracts it by 1 to give the program the correct index value for each of the lists
        # This is because computers start counting lists from position "0"
        index = int(choice) - 1 
        

