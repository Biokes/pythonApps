class User:

    def __init_subclass__(self, name: str):
        self.name = name
