import unittest
import pytest
from src.entity.superHero import superHero
from src.entity.metaHero import metaHero

class TestSuperHero(unittest.TestCase):

    def setUp(self):
        self.s1 = superHero()

    def test_existClass(self):
        self.assertTrue(self.s1)

    def test_hasName(self):
        self.assertEqual(self.s1.name, 'Batman', 'Wrong superhero choosed.')

    def test_hasPower(self):
        self.assertGreaterEqual(self.s1.power, 1024)

    def test_secretName(self):
        self.assertEqual(self.s1.secretName, 'Bruce Wayne', 'Wrong person.')

    def test_hasCity(self):
        self.assertEqual(self.s1.city, 'Gotham', 'Are you sure?.')

    def test_hasLocation(self):
        self.assertEqual(self.s1.location, 'Batcave', 'I not agree.')

    def test_maxPower(self):
        self.s1.maxPower(8000)
        self.assertGreaterEqual(self.s1.power, 1024)

    def test_metaClass(self):
        m = metaHero
        self.assertTrue(m)

    def test_instance(self):
        s2 = superHero()
        self.assertEqual(id(self.s1), id(s2), 'Singleton failed, variables contain different superheroes')

        if id(self.s1) == id(s2):
            print(f'Singleton works, both variables contain the same superhero "{self.s1.name}".')
        else:
            print(f'Singleton failed, variables contain different superheroes, only one "{self.s1.name}" can exist.')


if __name__ == '__main__':
   unittest.main()