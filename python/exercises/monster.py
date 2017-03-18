import random


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


class Monster:
    COLORS = ['yellow', 'red', 'blue', 'green']

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

    def battlecry(self):
        return self.sound.upper()
