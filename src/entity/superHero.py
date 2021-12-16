from entity.metaHero import metaHero

class superHero(metaclass=metaHero):
    """
    Any singleton should define some business logic, which can be
    executed on its instance.
    """
    def __init__(self):
        self.name = 'Batman'
        self.power = 1024
        self.secretName = 'Bruce Wayne'
        self.city = 'Gotham'
        self.location = 'Batcave'

    def maxPower(self, newPower):
        if newPower < 1024:
            print('maxPower has to be >= 1024')
        else:
            self.power = newPower
        