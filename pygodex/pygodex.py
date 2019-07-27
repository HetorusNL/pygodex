import json
import os.path

from pygodex.base_dex import BaseDex
from pygodex.user_dex import UserDex


class Pygodex(object):
    """Python Pokemon Go Pokedex interpreter usable through natural language"""

    def __init__(self):
        """Load the base pokedex with all pokemon, evolutions, candies, etc"""
        self.version = 0.1  # version parameter, usage TBD
        self.base_path = "pygodex/pokedexes/"

        with open(f"{self.base_path}pygodex_base_dex.json") as f:
            base_dex_json = json.load(f)
        self.base_dex = BaseDex()
        self.base_dex.load(base_dex_json)
        self.user_dex = None

    def load(self, pokedex_file):
        """Load the pokedex_file (from the pokedexes folder)
        auto-appended with .json if not present"""
        if not pokedex_file.endswith(".json"):
            pokedex_file += ".json"

        try:
            with open(f"{self.base_path}{pokedex_file}") as f:
                user_dex_json = json.load(f)
        except BaseException:
            print(f'failed to load pokedex "{pokedex_file}"!')
            return

        self.user_dex = UserDex(pokedex_file, self.base_dex)
        self.user_dex.load(user_dex_json)

        print(f"successfully loaded pokedex {pokedex_file}")

    def create(self, pokedex_file):
        """Create the pokedex_file (from the pokedexes folder)
        auto-appended with .json if not present"""
        if not pokedex_file.endswith(".json"):
            pokedex_file += ".json"

        if os.path.isfile(f"{self.base_path}{pokedex_file}"):
            raise Exception("pokedex {pokedex_file} already exists!")

        # pokedex doesn't exist (yet), initialize empty user_dex and create
        self.user_dex = UserDex(pokedex_file, self.base_dex)
        self.user_dex.load(None)
