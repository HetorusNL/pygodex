import json


class UserDex(object):
    """The user dex containing the user specific information about pokemon"""

    def __init__(self, pokedex_file, base_dex):
        self.base_path = "pygodex/pokedexes/"
        self.pokedex_file = pokedex_file
        # copy the reference to the base dex'es pokemon to this class
        self.pokemon = base_dex.pokemon

    def load(self, user_dex_json):
        user_dex_json = self.initialize_dex(user_dex_json)
        for name, information in user_dex_json.items():
            pokemon = self.pokemon.get(name)
            if not pokemon:
                raise Exception(f"Pokemon {name} not found in the pokedex!")

            pokemon.set_user_dex(name, information)

    def unload(self):
        for pokemon in self.pokemon:
            if self.pokemon[pokemon].user_dex:
                self.pokemon[pokemon].user_dex = None

    def initialize_dex(self, user_dex_json):
        """Function to make sure that all pokemon exist in the user dex"""
        should_save = False
        if not user_dex_json:
            user_dex_json = {}

        for pokemon, pokemon_obj in self.pokemon.items():
            if not user_dex_json.get(pokemon):
                user_dex_json[pokemon] = self.generate_pokemon(pokemon)
                should_save = True

        if should_save:
            self.save_dex(user_dex_json)

        return user_dex_json

    def generate_pokemon(self, pokemon):
        return {"pokemon": pokemon, "candies": 0, "num_owned": 0}

    def save_dex(self, user_dex_json=None):
        if not user_dex_json:
            # construct the user_dex_json based on the pokemon data
            pass

        with open(f"{self.base_path}{self.pokedex_file}", "w") as f:
            f.write(json.dumps(user_dex_json))
