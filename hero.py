#!/usr/bin/python3

class Hero:
    def __init__(self, name="", race="", gender="", level=0, exp_for_next_level=1000, current_exp=0):
        self.name = name
        self.race = race
        self.gender = gender
        self.level = level
        self.exp_for_next_level = exp_for_next_level
        self.current_exp = current_exp
    

    def updateExp(self):
        self.current_exp += 3
        if exp_for_next_level == current_exp:
            self.level += 1
            exp_for_next_level = self.level * 1000
            print("level up -> {}".format(self.level))

    def death(self):
        self.current_exp = self.current_exp/2
        print("{} died".format(self.name))


    def sayHello(self):
        print("Hello my name is {} of race {}".format(self.name, self.race))

    def to_json(self, attrs=None):
        """function return dict"""
        dir1 = vars(self)
        if attrs is not None:
            dir2 = {}
            for i in attrs:
                if i in self.__dict__:
                    dir2[i] = dir1[i]
            return(dir2)
        else:
            return(dir1)

    def reload_from_json(self, json):
        dir1 = vars(self)
        dir2 = json
        for x in json:
            dir1[x] = dir2[x]

class Paladin(Hero):
    def __init__(self, atk=10, defense=0, armor=200, hp=100):
        self.atk

        