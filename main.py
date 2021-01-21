#!/usr/bin/python3
import json

Hero = __import__('hero').Hero
Paladin = __import__('paladin').Paladin

session = int(input("1 for new user: \n2 for login: "))
if session == 1:
    name = input("input name: ")
    race = int(input("select a race 1: Human 2: Elf 3: Hobbit 4: Orc  "))
    champion = int(input("choice a champion 1 paladin 2 Mago..."))
    if race == 1 and champion == 1:
        user = Paladin()       

    gender = input("input gender: ")
    user.name = name
    user.race = race
    user.gender = gender
    user.level = 0
    user.exp_for_next_level = 1000
    user.current_exp = 0
    user.sayHello()

    with open("herosfile.txt", mode="a", encoding="utf-8") as my_file:
        if session == 1:
            obj_save = user.to_json()
            obj_save = json.dumps(obj_save)
            my_file.write(obj_save)
            my_file.write("\n")

if session == 2:
    user = Paladin()
    name = input("input your name: ")
    with open("herosfile.txt", mode="r", encoding="utf-8") as my_file:
        lines = my_file.readlines()
        for line in lines:
            if name in line:
                new_user = json.loads(line)
                user.reload_from_json(new_user)
                break

    user.sayHello()
state = 0
while True:
    if state == 0:
        print("--- start fight-----")
        print("your status...")
        machine = Paladin()
        Ename = "enemy" + str(user.level)
        with open("herosfile.txt", mode="r", encoding="utf-8") as my_file:
            lines = my_file.readlines()
            for line in lines:
                if Ename in line:
                    new_user = json.loads(line)
                    machine.reload_from_json(new_user)
                    break

        print("{} atk, {} armor, {} defense, {} level".format(user.atk, user.armor, user.defense, user.level))
        print("Enemi status...")
        print("{} atk, {} armor, {} defense, {} level".format(machine.atk, machine.armor, machine.defense, machine.level))

    if state % 2:
        print("you atk")
        rest = user.atak1()
        alive = machine.hurt(rest)
        print("enemy hp ->")
        if not alive:
            print("you win")
            break
    else:
        print("enemy atk")
        rest = machine.atak1()
        alive = user.hurt(rest)
        print("hp -> {}".format(user.hp))
        if not alive:
            print("you lose")
            break

    state += 1
