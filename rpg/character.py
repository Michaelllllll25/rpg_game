import random
import pprint

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

class Character:
    def __init__(self, name: str, hp: int, vb: int, atk: int, magic: str, items: str, wallet: int) -> None:
        self.name = name
        # Current HP
        self.hp = hp
        # Max hp
        self.max_hp = hp
        # VB (cost for items)
        self.vb = vb
        self.max_mp = vb
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        # Wallet contains 500 vb
        self.wallet = 500

    def get_hp(self) -> int:
        return self.hp
     
    def get_max_hp(self) -> int:
        return self.max_hp 
   
    def vb(self) -> int:
        return self.vb
     
    def get_max_vb(self) -> int:
        return self.max_vb 

    def generate_damage(self) -> int:
        return random.randrange(self.atk_low, self.atk_high)
       
    def take_damage(self, dmg: int) -> int:
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0 
        return self.hp 

    def choose_magic(self):
        i = 1 
        
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "     MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
       
    def choose_items(self):
        i = 1 
        
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "     ITEMS:" + bcolors.ENDC)
        
        # This prints out the items available in the items dictionary:
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
        i += 1
    
   # These are utility classes to get HP and MP information to calculate remaining MP and HP points  
    
    def heal(self, dmg):
        self.hp += dmg
        # This makes sure you don't heal above your max hp 
        if self.hp > self.maxhp:
            self.hp = self.maxhp 
    

   
    def reduce_mp(self, cost):
        self.mp -= cost
       
# players = Character['mm', '1000', '500']
# for player in players
