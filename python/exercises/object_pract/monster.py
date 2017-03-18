import random

from combat import Combat

# Use two spaces before class definition: PEP8 rule.
# class Monster:
#     __init__
#     hit_points = 1
#     color = 'yellow'
#     weapon = 'sword'
#     sound = 'roar'

#     def battlecry(self):
#        return self.sound.upper()


# class Monster:
#     def __init__(self, hit_points=100, weapon='ax', color='green', sound='grrrrr'):
#         self.hit_points = hit_points
#         self.weapon = weapon
#         self.color = color
#         self.sound = sound

#     def battlecry(self):
#        return self.sound.upper() + '!' * 5


# class Monster:
#     def __init__(self, **kwargs):
#         self.hit_points = kwargs.get('hit_points', 1)
#         self.weapon = kwargs.get('weapon', 'sword')
#         self.color = kwargs.get('color', 'yellow')
#         self.sound = kwargs.get('sound', 'grrrr')

#     def battlecry(self):
#        return self.sound.upper() + '!' * 5


class Monster(Combat):
    COLORS = ['black', 'blue', 'green', 'purple']

    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(self.COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)
    
    # __str__ special method that controls what happens to a string from an object
    
    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                            self.__class__.__name__,
                                            self.hit_points,
                                            self.experience)

    def battlecry(self):
        return self.sound.upper()

## Normally, you only want one class per file. However, since everything in this file can be considered a "monster," it's permissible.


class Goblin(Monster): # By inserting Monster into Goblin, we are saying, "Hey, Goblin is a subclass of Monster, which is the parent."
    #pass # pass keyword tells Python, "I am inheriting from Monster class, so keep going until I get new information."

    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl'


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaaaaaaaaar'


###### Miscellaneous Notes

# Technically, all classes, including Monster, inherit from their parent, the object class. 
