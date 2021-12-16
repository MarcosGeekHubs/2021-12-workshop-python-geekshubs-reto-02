from entity.metaHero import metaHero

class superHero(metaclass=metaHero):
    """
    Any singleton should define some business logic, which can be
    executed on its instance.
    """

    def __init__(self, name, power, secretName, city, location):
        self.name = name
        self.power = power
        self.secretName
        self.city
        self.location

    def maxPower(self, power):
        if (power > 1024):
            self.power = 1024
        else:
            self.power = power





