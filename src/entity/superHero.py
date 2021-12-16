from entity.metaHero import metaHero

class superHero(metaclass=metaHero):

    def __init__(self, name, power, secretName, city, location):
        self.name = name
        self.power = power
        self.secretName = secretName
        self.city = city
        self.location = location

    def maxPower(self, power2):
        return self.power + power2