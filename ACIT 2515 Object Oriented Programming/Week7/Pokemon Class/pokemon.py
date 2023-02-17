

class Pokemon:
    """I READ THE TESTS AND INSTRUCTIONS
    I would improve this class by modifying the fight method.
    Although I do think it works fine, I think that the damage taken should depend
    on the element of the Pokemon because as of right now theres nothing being done with the element.
    Similar to the game, depending on the element of the Pokemon a small multiplier could be added 
    if the opponent pokemon is an opposite element like fire and water, then the fire pokemon would take 1.3X more damage.
    """
    def __init__(self, name: str, element: str):
        """Constructs the pokemon
        Args:
        - name (str): The name of the pokemon 
        - element (str): element must be fire, water, grass, or electricity 
        Raises:
        ValueError: if element is not a valid element
        """
        self.name = name
        if element not in ("fire", "water", "grass", "electric"):
            raise ValueError
        self.element = element
        self.health = 100
        self.attack = 0 
        self.armor = 0 
        self.level = 1

    def __str__(self):
        return f"<{self.name} [{self.element}] ({self.health}, {self.attack}, {self.armor})>"
    
    def level_up(self):
        """
        Adds 1 to the level of the pokemon and increases its health to level*100
        """
        self.level += 1
        self.health = self.level*100
    
    def set_health(self, health: int):
        """sets the health of the pokemon to the given value if above 0 

        Args:
            health (int): must be an integer

        Raises:
            ValueError: if health is not an integer
        """
        if not isinstance(health, int):
            raise ValueError
        elif int(health) > 0:
            self.health = health
        else:
            self.health = 0
    
    def is_active(self):
        """If health is above 0 then returns True otherwise returns False

        Returns:
            bool: True if health is above 0
        """
        if self.health > 0:
            return True
        return False
    
    def fight(self, pokemon):
        """
        If opponent (pokemon arg) has an armor lower than the attack of then its health 
        is subtracted by the difference 
        
        If opponent (pokemon arg) has an attack that is greater than both the armor and attack 
        then the pokemon's health is subtracted by the difference of the oppents attack - armor - attack
        """
        
        if not isinstance(pokemon, Pokemon):
            raise ValueError
        if (self.attack - pokemon.armor) < 0:
            pass
        else:
            pokemon.health = pokemon.health - (self.attack - pokemon.armor)
        
        if (pokemon.attack - self.armor - self.attack) < 0:
            pass
        else: 
            self.health = self.health - (pokemon.attack - self.armor - self.attack)
        
        
                #  health=100, attack=0, armor=0, level=1):
        