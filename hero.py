
class SuperHero:
    people='people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def hero_name(self):
        return f'My name is {self.name}'

    def increase_health(self):
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return f'Nickname: {self.nickname}, Superpower: {self.superpower}, Health points: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


a_hero = SuperHero('aleks', 'cool boy', 'super strong', 10, 'be fair')
print(a_hero.people)
print(a_hero.hero_name())
print(a_hero.increase_health())
print(a_hero)
print(len(a_hero))
