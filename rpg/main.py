from magic import Spell
from item import Item

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
 

