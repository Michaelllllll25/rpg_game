import random

class Character:
    def __init__(self, name: str, hp: int, vb: int, atk: int, magic: list, items: list, wallet: int) -> None:
        self.name = name
        # Current HP
        self.hp = hp
        # Max hp
        self.max_hp = hp
        # VB (cost for items)
        self.vb = vb
        self.max_vb = vb
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
   
    def get_vb(self) -> int:
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

    def choose_magic(self) -> None:
        i = 1 
        
        print("\n""     MAGIC:")
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
       
    def choose_items(self) -> None:
        i = 1 
        
        print("\n""     ITEMS:")
        
        # This prints out the items available in the items dictionary:
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
        i += 1
    
   # These are utility classes to get HP and MP information to calculate remaining MP and HP points  
    
    def heal(self, dmg) -> None:
        self.hp += dmg
        # This makes sure you don't heal above your max hp 
        if self.hp > self.maxhp:
            self.hp = self.maxhp 
   
    def reduce_vb(self, cost) -> None:
        self.vb -= cost

    def get_stats(self) -> None:        
        hp = ""
        hp_ticks = (self.hp / self.max_hp) * 100 / 4
        
        mp_bar = ""
        mp_ticks = (self.vb / self.max_vb) * 100 / 10

    def choose_action(self) -> None:
        i = 1 
        print("\n" + "    " + self.name)
        print("    ACTIONS")
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1 

    def choose_target(self, enemies: list) -> None:
        i = 1    
        print("\n""    TARGET:")
        # This prints the enemies on screen, and then lets the player decide which enemy to attack
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1 
            choice = int(input("    Choose target:")) - 1 
            return choice

