class Hero:
    """Represents a hero with a name, damage, health, and max health.

    Attributes:
        name (str): The name of the hero.
        damage (int): The amount of damage the hero can deal.
        health (int): The current health of the hero.
        max_health (int): The maximum health the hero can have.
    """

    def __init__(self, name: str, damage: int, health: int = 100, max_health: int = 100):
        """Initializes a hero with given attributes.

        Args:
            name (str): The name of the hero.
            damage (int): The starting damage value of the hero.
            health (int, optional): The starting health of the hero (default is 100).
            max_health (int, optional): The maximum health of the hero (default is 100).
        """
        self.name = name
        self.damage = damage
        self.health = health
        self.max_health = max_health

    def hit(self, target: 'Hero'):
        """Attacks another hero and reduces their health.

        Args:
            target (Hero): The hero that will take damage.
        """
        target.health -= self.damage
        print(f"{target.name} damaged by {self.name}")
        print(f"{target.name} health after damage: {target.health}")

        # Prevents health from going below zero
        if target.health <= 0:
            target.health = 0
            print(f"{self.name} killed {target.name}")

    def set_damage(self, value: int):
        """Changes the hero's damage value.

        Args:
            value (int): The new damage value (must be greater than 0).
        """
        if value > 0:
            self.damage = value
        print(f"Modify {self.name} damage: {self.damage}")

    def magic_spell_upg(self):
        """Increases the hero's damage by 5."""
        self.damage += 5
        print(f"{self.name} upgraded damage by 5 points, now it is {self.damage}")

    def heal(self, value: int):
        """Heals the hero without exceeding max health.

        Args:
            value (int): The amount of health to recover.
        """
        self.health = min(self.health + value, self.max_health)
        print(f"{self.name} recovered {value} health points")
        print(f"{self.name} health after recovery: {self.health}")


# Create two heroes
hero1 = Hero("Minthara", 10)
hero2 = Hero("ShadowHeart", 8)

# Print initial hero names and health
print(hero1.name)
print(hero1.health)
print(hero2.name)
print(hero2.health)

hero1.hit(hero2)# Hero1 attacks Hero2
hero2.set_damage(15)# Hero2 changes damage value
hero2.hit(hero1)# Hero2 attacks Hero1
hero1.heal(8)# Hero1 heals
hero1.magic_spell_upg()# Hero1 upgrades damage using magic spell

# Print final health after the fight
print("After fighting:")
print(hero1.name)
print(hero1.health)
print(hero2.name)
print(hero2.health)
