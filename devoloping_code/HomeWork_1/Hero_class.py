class Hero:
    # Create a hero with  name, damage, health, and max health.
    def __init__(self, name: str, damage: int, health: int=100,max_health: int =100):
        self.name = name
        self.damage = damage
        self.health = health
        self.max_health = max_health
    
    # Attack another hero and reduce their health.
    def hit(self,target:'Hero'):
        target.health-=self.damage
        
        print(f"{target.name} damaged by {self.name}")
        print(f"{target.name} health after damage:{target.health}")
    # small check to make sure hero health dont go below zero.    
        if target.health <= 0:
            target.health = 0
    # if health below zero program say hero killed .
            print(f"{self.name} killed {target.name}")
    # Change the hero damage value.
    def set_damage(self,value: int):
        if value > 0:
            self.damage = value
        print(f"Modify {self.name} damage : {self.damage}")

  

    def magic_spell_upg(self):
        self.damage+= 5

        print(f"{self.name} upgrade hit 5 points and now hit equal {self.damage}")

    # Heal the hero .
    def heal(self,value:int):
        self.health=min(self.health + value,self.max_health) # without exceeding max health.
        print(f"{self.name} recovery health point : {value}")
        print(f"{self.name} health after recovory :{self.health}")

# Create two heroes(implying that i'm a BG3 fan)

hero1 = Hero("Minthara", 10)
hero2 = Hero("ShadowHeart", 8)

# Print before fihght hero names and health

print(hero1.name)
print(hero1.health)
print(hero2.name)
print(hero2.health)

hero1.hit(hero2) # Hero1 attack Hero2
hero2.set_damage(15) # Hero2 changes damage value
hero2.hit(hero1) # Hero2 attack Hero1
hero1.heal(8) # Hero1 heals
hero1.magic_spell_upg()

# Print final health after fight

print("After fighting :")

print(hero1.name)
print(hero1.health)
print(hero2.name)
print(hero2.health)
