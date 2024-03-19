import random
from Parameters import *


class Player():
    def __init__(self, age, name, gender, trick, speech, surname="", life=True, choice=None):
        self.surname = surname
        self.name = name
        self.age = age
        self.gender = gender
        self.trick = trick
        self.speech = speech
        self.life = life
        self.choice = choice
        self.icon = pygame.image.load("player.jpg")

    def D20(self):
        return random.randint(1, 20)

    def roll(self):
        a = round(self.speech // 10)
        return random.randint(a, 12)

    def choose(self, end):
        self.choice = random.randint(0, end - 1)
        return self.choice

    def __repr__(self):
        return "[{}, {}, {}, {}, {}, {}, life = {}]".format(self.name, self.age, self.gender, self.trick, self.speech,
                                                            self.surname, self.life)


class Mafia(Player):
    def __init__(self, other):
        super().__init__(other.age, other.name, other.gender, other.trick, other.speech, surname="Mafia")


class Doctor(Player):
    def __init__(self, other):
        super().__init__(other.age, other.name, other.gender, other.trick, other.speech, surname="Doctor")


class Peaceful_citizen(Player):
    def __init__(self, other):
        self.maf_choose = None
        super().__init__(other.age, other.name, other.gender, other.trick, other.speech, surname="Citizen")



class Leader(Player):
    def __init__(self, age=None, name="Saimon", gender="machine", trick=100, speech=100,
                 icon=pygame.image.load("icon.jpg")):
        super().__init__(age, name, gender, trick, speech)
        self.dead_list = []
        self.heal_list = []
        self.x = 360
        self.y = 5
        self.icon = pygame.image.load("lead.jpg")

    def maf_target(self, target):
        if self.dead_list.count(target) == 0:
            self.dead_list.append(target)

    def kick(self, dead):
        if dead != 0:
            print("Players kicked", dead.name)
            dead.life = False

    def doctor_target(self, target):
        self.heal_list.append(target)

    def results_night(self):
        res = ""
        print("--Results of this night--")

        if len(self.heal_list) > 0 and self.dead_list[0] == self.heal_list[0]:
            res = "The Mafia wanted to kill " + str(self.dead_list[0].name) + " but the doctor cured him"
        else:
            res = "Mafia killed " + str(self.dead_list[0].name)
            res += ".  " + " Sleep well " + str(self.dead_list[0].name)
            self.dead_list[0].life = False

        self.clear_target()
        return res

    def info(self):
        print(self.dead_list)
        print(self.heal_list)

    def clear_target(self):
        self.dead_list = []
        self.heal_list = []


