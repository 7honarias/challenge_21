#!/usr/bin/python3
import json

Hero = __import__('hero').Hero

session = int(input("press 1 for regis or 2 for login: "))
if session == 1:
    name = input("input name: ")
    race = input("select a race 1: Human 2: Elf 3: Hobbit 4: Orc  ")
    gender = input("input gender: ")
    user = Hero(name, race, gender)
    user.sayHello()

    with open("herosfile.txt", mode="a", encoding="utf-8") as my_file:
        if session == 1:
            obj_save = user.to_json()
            obj_save = json.dumps(obj_save)
            my_file.write(obj_save)

if session == 2:
    user = Hero()
    name = input("input your name: ")
    with open("herosfile.txt", mode="r", encoding="utf-8") as my_file:
        lines = my_file.readlines()
        for line in lines:
            if name in line:
                new_user = json.loads(line)
                user.reload_from_json(new_user)
                break

    user.sayHello()


