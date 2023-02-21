from pokemon import Pokemon
import csv 

class Arena:
    def __init__(self, *args):
        self.teamlist = []
        self.pokemonlist = []
        self.teamdict = {}
        
        for pokemon in args:
            if isinstance(pokemon, Pokemon):
                self.pokemonlist.append(pokemon)
    
    def __len__(self):
        return len(self.active())
        
    def load_from_file(self, filename: str):
        
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if int(row[1]) > 0:
                    self.pokemonlist.append(Pokemon(row[0]))
                
    def add(self, pokemon: Pokemon):
        if not isinstance(pokemon, Pokemon):
            raise AttributeError
        else:
            self.pokemonlist.append(pokemon)
            
    def active(self) -> list[Pokemon]:
        
        alive_pokemon = []
        for pokemon in self.pokemonlist:
            if pokemon.health > 0:
                alive_pokemon.append(pokemon)
        return alive_pokemon
        
    def make_team(self, level: int):
        return Team(level, self.active())
    
class Team:
    def __init__(self, level, pokemonlist):
        self.level = level
        self.pokemonlist = pokemonlist
    def get_pokemons(self) -> list[Pokemon]:
        alive_pokemon = []
        for pokemon in self.pokemonlist:
            if pokemon.health > 0:
                alive_pokemon.append(pokemon)
        return alive_pokemon