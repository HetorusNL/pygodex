class Pokemon(object):
    """The Pokemon class which holds some convenient functions for Pokemons"""

    def __init__(self, pokemon, base_dex_input):
        self.pokemon = pokemon
        self.base_dex = base_dex_input
        self.user_dex = None

    def set_user_dex(self, pokemon, user_dex_input):
        # ensure that the pokemon is the same
        if pokemon != self.pokemon:
            raise Exception("Can't set user dex on other Pokemon!")

        self.user_dex = user_dex_input

    def validate_data(func):
        """Validate the data, making sure that the function can only be
        executed if all necessary data is present, note this function must
        specified before the decorator can be used"""

        def func_wrapper(self, *args, **kwargs):
            if not (self.base_dex and self.user_dex):
                return  # both dexes aren't available
            if self.pokemon != self.user_dex["pokemon"]:
                return  # names aren't equal

            return func(*args, **kwargs)

        return func_wrapper

    @validate_data
    def can_evolve(self, candies_override=None):
        needed_candies = self.base_dex.get("evolve_candies")
        if candies_override:
            needed_candies = candies_override

        # if self.base_dex.get("evolve_item"):
        #    pass  # not implemented yet

        if self.user_dex.get("candies", 0) >= needed_candies:
            return True

        return False
