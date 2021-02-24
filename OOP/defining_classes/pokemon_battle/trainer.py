# from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        pokemon_to_remove = [pok for pok in self.pokemon if pok.name == pokemon_name]
        if not pokemon_to_remove:
            return "Pokemon is not caught"
        removed_name = pokemon_to_remove[0].name
        self.pokemon.remove(pokemon_to_remove[0])
        return f"You have released {removed_name}"

    def trainer_data(self):
        output = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for pok in self.pokemon:
            output += f"- {pok.pokemon_details()}\n"
        return output




#
# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
