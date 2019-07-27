import re


class RegexParser(object):
    """The regex parser that parses the user's commands"""

    def __init__(self):
        self.commands = self._load_commands()

    def parse(self, raw_input):
        for command in self.commands:
            match = re.match(command["regex"], raw_input)
            if match:
                return {"command": command["command"], **match.groupdict()}

        # no matching command, return the input
        return {"command": raw_input}

    def _load_commands(self):
        return [
            {
                "name": "help",
                "description": "displays help information about Pygodex",
                "usage": "help",
                "regex": r"\s*help\s*",
                "command": "help",
            },
            {
                "name": "load pokedex",
                "description": "loads the pokedex specified",
                "usage": "load pokedex <name>(.json)",
                "regex": r"load\s+pokedex\s+(?P<pokedex>[a-zA-Z0-9_\.\-]+)$",
                "command": "load_pokedex",
            },
            {
                "name": "create pokedex",
                "description": "creates the pokedex specified",
                "usage": "create pokedex <name>(.json)",
                "regex": r"create\s+pokedex\s+(?P<pokedex>[a-zA-Z0-9_\.\-]+)$",
                "command": "create_pokedex",
            },
        ]
