# 2021-12-workshop-python-reto-02

![image](https://user-images.githubusercontent.com/16636086/144272202-b607b039-55ab-433e-902f-29ce08469110.png)

## SuperHeroe Generator

Welcome to the ***SuperHeroe Generator***. The objective of this challenge is to create a superhero object. In this city there can only be one superhero and therefore this object must be unique.

Therefore, you must define a superHero class that includes the following properties:

- `name`
- `power`
- `secretName`
- `city`
- `location`

On the other hand, this object must have the ability to increase its power at certain times, if the situation requires it, by calling the maxPower function. Remember that there can only be one superhero.

You can find clues to solve the challenge in the same repository.

## The requirement

Feel free to make any changes to the `superHero` and` metaHero` classes. You should add any necessary code, as long as everything follows the requirements outlined. However, *** do not alter the `main.py` class or its properties *** as this lets us know if the code is working correctly.

## Final notes

To clarify: a candidate can never have a "power" less than "1024". All attributes and methods created must be public. It is recommended to use the meclass to apply the singleton pattern.

## Help

- pip install -e .
- pip install pytest
- python3 -m pytest test/TestSuperHero.py

