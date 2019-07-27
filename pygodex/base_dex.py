from pygodex.pokemon import Pokemon


class BaseDex(object):
    """The base dex containing the general information about pokemon"""

    def __init__(self):
        self.pokemon = {}

    def load(self, base_dex_json):
        for name, information in base_dex_json.items():
            self.pokemon[name] = Pokemon(name, information)
