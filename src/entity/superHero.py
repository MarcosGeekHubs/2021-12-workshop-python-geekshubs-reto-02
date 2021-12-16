from src.entity.metaHero import metaHero

class superHero(metaclass=metaHero):

    def __init__(self):
        self.name = 'Batman'
        self.power = 1024
        self.secretName = 'Bruce Wayne'
        self.city = 'Gotham'
        self.location = 'Batcave'

    def maxPower(self, power2):
        return self.power + power2