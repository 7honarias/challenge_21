#!/usr/bin/python3

class Hero:
    def __init__(self, name="", race="", gender="", level=0, exp_for_next_level=1000, current_exp=0):
        self.name = name
        self.race = race
        self.gender = gender
        self.level = level
        self.exp_for_next_level = exp_for_next_level
        self.current_exp = current_exp
    

    def death(self):
        self.current_exp = self.current_exp/2
        print("{} died".format(self.name))


    def sayHello(self):
        print("Hello my name is {} of race {}".format(self.name, self.race))
