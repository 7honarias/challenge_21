#!/usr/bin/python3
Hero = __import__('hero').Hero

class Paladin(Hero):
    def __init__(self, atk=10, defense=0, armor=200, hp=100):
        self.atk = atk
        self.defense = defense
        self.armor = armor
        self.hp = hp
        super().__init__()

    def updateExp(self):
        self.current_exp += 3
        if exp_for_next_level == current_exp:
            self.level += 1
            exp_for_next_level = self.level * 1000
            self.update_level()
            print("level up -> {}".format(self.level))

    def update_level(self):
        self.atk = self.atk * self.level/3
        self.defense = self.defense * self.level/2
        self.armor = self.armor * self.level
        self.hp = self.armor

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
        
    def atak1(self):
        return (self.atk)

    def hurt(self, damage):
        self.hp -= damage - self.defense
        if self.hp <= 0:
            return False
