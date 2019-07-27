from pygodex.pygodex import Pygodex
from pygodex.regex_parser import RegexParser


class Interpreter(object):
    """The frontend / user facing class, interpreting the user's commands"""

    def __init__(self):
        print("Welcome to pygodex, the Python Pokemon Go Pokedex!")
        self.pygodex = Pygodex()
        self.regex_parser = RegexParser()

        print(f"pygodex version {self.pygodex.version} initialized")
        print('type your commands, or "help" for usage information')

    def run(self):
        while True:
            try:
                raw_input = input(">>> ")
            except (EOFError, KeyboardInterrupt):
                print()  # add a newline after the most recent prompt
                return  # stop the program if EOF (Ctrl+D) / Ctrl+C is received
            command = self.regex_parser.parse(raw_input)
            if command:
                self.run_command(command)

    def run_command(self, command):
        if command["command"] == "help":
            self.print_help()
        elif command["command"] == "load_pokedex":
            self.pygodex.load(command["pokedex"])
        elif command["command"] == "create_pokedex":
            self.pygodex.create(command["pokedex"])
        else:
            print(f'unknown command: "{command["command"]}"')

    def print_help(self):
        # command header
        print("=" * 80)
        print("the following commands are available in Pygodex:")

        # get maximum command length
        max_len = max([len(c["name"]) for c in self.regex_parser.commands])

        # commands themselves
        for command in self.regex_parser.commands:
            num = max_len - len(command["name"])
            print(f'{command["name"]} {" " * num} => {command["description"]}')
            print(f'{" " * (max_len + 4)} usage: {command["usage"]}')
        print()

        # syntax header
        print("=" * 80)
        print("the following syntax should be used:")

        # syntax lines themselves
        print("parameter   => should be typed literaly")
        print("(parameter) => can be typed, and can be skipped")
        print("<parameter> => user supplied parameter")
