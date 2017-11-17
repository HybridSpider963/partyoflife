# partyoflifeimport time
import random
import sys

global roll
global p1spot
global p2spot
global p3spot
global p4spot
global p1health
global p2health
global p3health
global p4health

p1spot = 1
p2spot = 1
p3spot = 1
p4spot = 1

p1c = 1

p1health = 100
p2health = 100
p3health = 100
p4health = 100


def mapview():
    print(
        " _____________________________________________________________________________________________________________________________________________________________________")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|       START        _          2         _          3         _         4         _         5          _          6         _         7          _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|-------------------------------------------------------------------------------------------------------------------------------------------------_         8         |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|                    _           14       _           13       _          12       _          11        _         10         _         9          _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|          15        _------------------------------------------------------------------------------------------------------------------------------------------------|")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|                    _          16        _          17        _         18        _         19         _         20         _         21         _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|-------------------------------------------------------------------------------------------------------------------------------------------------_         22        |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|                    _          28        _          27        _         26        _         25         _         24         _         23         _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|          29        _------------------------------------------------------------------------------------------------------------------------------------------------|")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          30        _          31        _         32        _          33        _         34         _         35         _                   |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|-------------------------------------------------------------------------------------------------------------------------------------------------_         36        |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          42        _          41        _         40        _          39        _         38         _         37         _                   |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|          43        _------------------------------------------------------------------------------------------------------------------------------------------------|")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          44        _          45        _         46        _          47        _         48         _         49         _                   |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|-------------------------------------------------------------------------------------------------------------------------------------------------_         50        |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          56        _          55        _         54        _          53        _         52         _          51        _                   |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|          57        _------------------------------------------------------------------------------------------------------------------------------------------------|")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          58        _          59        _         60        _          61        _         62         _          63        _         END       |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|_____________________________________________________________________________________________________________________________________________________________________|")


def diceroll4():
    global p1c
    global p4spot
    print("Player 4 you are on")
    time.sleep(1.75)
    print(p4spot)
    time.sleep(1.75)
    roll = random.randint(1, 6)
    rollinput = input("Type R to roll")
    if rollinput == "r" or not rollinput == "r":
        print("You rolled a........")
        time.sleep(1.75)
        print(roll)
        p4spot = p4spot + roll
        p1c = 4
        p4move()


def diceroll3():
    global p1c
    global p3spot
    print("Player 3 you are on")
    time.sleep(1.75)
    print(p3spot)
    time.sleep(1.75)
    roll = random.randint(1, 6)
    rollinput = input("Type R to roll")
    if rollinput == "r" or not rollinput == "r":
        print("You rolled a........")
        time.sleep(1.75)
        print(roll)
        p3spot = p3spot + roll
        p1c = 3
        p3move()


def diceroll2():
    global p1c
    global p2spot
    print("Player 2 you are on")
    time.sleep(1.75)
    print(p2spot)
    roll = random.randint(1, 6)
    rollinput = input("Type R to roll")
    if rollinput == "r" or not rollinput == "r":
        print("You rolled a........")
        time.sleep(1.75)
        print(roll)
        p2spot = p2spot + roll
        p1c = 2
        p2move()


def diceroll1():
    fightinit = random.randint(1, 10)
    if fightinit >= 6:
        global p1c
        global p1spot
        print("Player 1 you are on ")
        time.sleep(1.75)
        print(p1spot)
        time.sleep(1.75)
        roll = random.randint(1, 6)
        time.sleep(1.75)
        rollinput = input("Type R to roll")
        if rollinput == "r" or not rollinput == "r":
            print("You rolled a........")
            time.sleep(1.75)
            print(roll)
            p1spot = p1spot + roll
            p1c = 1
            p1move()
    else:
        fightmechanicsinit()


def heavyp24():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p2health = p2health - 10
        print("Player 2 Health")
        print(p2health)
        if p2health == 0:
            p2spot = 2
            diceroll1()
        fightmechanics42()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 40
        if p4health <= 1:
            p4spot = 2
            diceroll1()
        fightmechanics42()


def lightp24():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p2health = p2health - 10
        print("Player 2 Health")
        print(p2health)
        fightmechanics42()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 20
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics42()


def heavyp42():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 4 Health")
        print(p4health)
        fightmechanics24()
        if p2health <= 0:
            print("Player 2 has died")
            diceroll1()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 40
        fightmechanics24()


def lightp42():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics24()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics24()


def heavyp43():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p4health = p4health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics34()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 40
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics34()


def lightp43():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p4health = p4health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics34()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 20
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics34()


def heavyp34():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics43()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 40
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics43()


def lightp34():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        fightmechanics43()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 20
        if p4health < 4:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics43()


def heavyp31():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            diceroll1()
        fightmechanics13()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p1health = p1health - 40
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics13()


def lightp31():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            diceroll1()
        fightmechanics13()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics13()


def heavyp13():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("p1health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            diceroll1()
        fightmechanics31()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 40
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics31()


def lightp13():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics31()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics31()


def heavyp23():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p2health = p2health - 10
        print("Player 2 Health")
        print(p2health)
        if p2health <= 1:
            p2spot = 2
            diceroll1()
        fightmechanics32()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 40
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics23()


def lightp23():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p2health = p2health - 10
        print("Player 2 Health")
        print(p2health)
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics32()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 20
        if p3health <= 1:
            p3spot = 2
            print("Player 3v has died")
            diceroll1()
        fightmechanics32()


def heavyp32():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics23()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 40
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics23()


def lightp32():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics23()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics23()


def heavyp41():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p4health = p4health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics14()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p1health = p1health - 40
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics14()


def lightp41():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p4health = p4health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics14()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p1health = p1health - 20
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics14()


def heavyp14():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics41()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 40
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics41()


def lightp14():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics41()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 20
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics41()


def heavyp31():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics13()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p1health = p1health - 40
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics13()


def lightp31():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics13()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics13()


def heavyp13():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics31()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 40
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics31()


def lightp13():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics31()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            diceroll1()
        fightmechanics31()


def heavyp12():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics21()

    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 40
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics21()


def lightp12():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics21()


def heavyp12():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics21()

    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 40
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics21()


def lightp12():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
        fightmechanics21()

    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
        fightmechanics21()
        p1move()


def fightmechanics12():
    print("Player 1 you are attacking Player 2")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp12()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp12()


def fightmechanics13():
    print("Player 1 you are attacking Player 3")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp13()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp13()


def fightmechanics21():
    print("Player 2 you are attacking Player 1")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp21()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp21()


def fightmechanics14():
    print("Player 1 you are attacking Player 4")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp14()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp14()


def fightmechanics23():
    print("Player 2 you are attacking Player 3")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp13()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp13()


def fightmechanics24():
    print("Player 2 you are attacking Player 4")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp24()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp24()


def fightmechanics34():
    print("Player 3 you are attacking Player 4")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp34()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp34()


def fightmechanics31():
    print("Player 3 you are attacking Player 1")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp31()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp31()


def fightmechanics41():
    print("Player 4 you are attacking Player 1")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp41()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp41()


def fightmechanics32():
    print("Player 2 you are attacking Player 3")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp32()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp32()


def fightmechanics43():
    print("Player 4 you are attacking Player 3")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp43()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp43()


def fightmechanics42():
    print("Player 4 you are attacking Player 2")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp42()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp42()


def fightmechanicsinit():
    global roll
    global p1spot
    global p2spot
    global p3spot
    global p4spot
    global p1health
    global p2health
    global p3health
    global p4health
    roof = random.randint(1, 12)
    if roof == 1:
        fightmechanics12()
    if roof == 2:
        fightmechanics21()
    if roof == 3:
        fightmechanics13()
    if roof == 4:
        fightmechanics31()
    if roof == 5:
        fightmechanics14()
    if roof == 6:
        fightmechanics41()
    if roof == 7:
        fightmechanics23()
    if roof == 8:
        fightmechanics32()
    if roof == 9:
        fightmechanics24()
    if roof == 10:
        fightmechanics42()
    if roof == 11:
        fightmechanics43()
    if roof == 12:
        fightmechanics34()


def p1move():
    global p1spot
    if p1spot == 2:
        time.sleep(1.75)
        square2()
    if p1spot == 3:
        time.sleep(1.75)
        square3()
    if p1spot == 4:
        time.sleep(1.75)
        square4()
    if p1spot == 5:
        time.sleep(1.75)
        square5()
    if p1spot == 6:
        time.sleep(1.75)
        square6()
    if p1spot == 7:
        time.sleep(1.75)
        square7()
    if p1spot == 8:
        time.sleep(1.75)
        square8()
    if p1spot == 9:
        time.sleep(1.75)
        square9()
    if p1spot == 10:
        time.sleep(1.75)
        square10()
    if p1spot == 11:
        time.sleep(1.75)
        square11()
    if p1spot == 12:
        time.sleep(1.75)
        square12()
    if p1spot == 13:
        time.sleep(1.75)
        square13()
    if p1spot == 14:
        time.sleep(1.75)
        square14()
    if p1spot == 15:
        time.sleep(1.75)
        square15()
    if p1spot == 16:
        time.sleep(1.75)
        square16()
    if p1spot == 17:
        time.sleep(1.75)
        square17()
    if p1spot == 18:
        time.sleep(1.75)
        square18()
    if p1spot == 19:
        time.sleep(1.75)
        square19()
    if p1spot == 20:
        time.sleep(1.75)
        square20()
    if p1spot == 21:
        time.sleep(1.75)
        square21()
    if p1spot == 22:
        time.sleep(1.75)
        square22()
    if p1spot == 23:
        time.sleep(1.75)
        square23()
    if p1spot == 24:
        time.sleep(1.75)
        square24()
    if p1spot == 25:
        time.sleep(1.75)
        square25()
    if p1spot == 26:
        time.sleep(1.75)
        square26()
    if p1spot == 27:
        time.sleep(1.75)
        square27()
    if p1spot == 28:
        time.sleep(1.75)
        square28()
    if p1spot == 29:
        time.sleep(1.75)
        square29()
    if p1spot == 30:
        time.sleep(1.75)
        square30()
    if p1spot == 31:
        time.sleep(1.75)
        square31()
    if p1spot == 32:
        time.sleep(1.75)
        square32()
    if p1spot == 33:
        time.sleep(1.75)
        square33()
    if p1spot == 34:
        time.sleep(1.75)
        square34()
    if p1spot == 35:
        time.sleep(1.75)
        square35()
    if p1spot == 36:
        time.sleep(1.75)
        square36()
    if p1spot == 37:
        time.sleep(1.75)
        square37()
    if p1spot == 38:
        time.sleep(1.75)
        square38()
    if p1spot == 39:
        time.sleep(1.75)
        square39()
    if p1spot == 40:
        time.sleep(1.75)
        square40()
    if p1spot == 41:
        time.sleep(1.75)
        square41()
    if p1spot == 42:
        time.sleep(1.75)
        square42()
    if p1spot == 43:
        time.sleep(1.75)
        square43()
    if p1spot == 44:
        time.sleep(1.75)
        square44()
    if p1spot == 45:
        time.sleep(1.75)
        square45()
    if p1spot == 46:
        time.sleep(1.75)
        square46()
    if p1spot == 47:
        time.sleep(1.75)
        square47()
    if p1spot == 48:
        time.sleep(1.75)
        square48()
    if p1spot == 49:
        time.sleep(1.75)
        square49()
    if p1spot == 50:
        time.sleep(1.75)
        square50()
    if p1spot == 51:
        time.sleep(1.75)
        square51()
    if p1spot == 52:
        time.sleep(1.75)
        square52()
    if p1spot == 53:
        time.sleep(1.75)
        square53()
    if p1spot == 54:
        time.sleep(1.75)
        square54()
    if p1spot == 55:
        time.sleep(1.75)
        square55()
    if p1spot == 56:
        time.sleep(1.75)
        square56()
    if p1spot == 57:
        time.sleep(1.75)
        square57()
    if p1spot == 58:
        time.sleep(1.75)
        square58()
    if p1spot == 59:
        time.sleep(1.75)
        square59()
    if p1spot == 60:
        time.sleep(1.75)
        square60()
    if p1spot == 61:
        time.sleep(1.75)
        square61()
    if p1spot == 62:
        time.sleep(1.75)
        square62()
    if p1spot == 63:
        time.sleep(1.75)
        square63()
    if p1spot >= 64:
        time.sleep(1.75)
        square64()


def p2move():
    global p2spot
    if p2spot == 2:
        time.sleep(1.75)
        square2()
    if p2spot == 3:
        time.sleep(1.75)
        square3()
    if p2spot == 4:
        time.sleep(1.75)
        square4()
    if p2spot == 5:
        time.sleep(1.75)
        square5()
    if p2spot == 6:
        time.sleep(1.75)
        square6()
    if p2spot == 7:
        time.sleep(1.75)
        square7()
    if p2spot == 8:
        time.sleep(1.75)
        square8()
    if p2spot == 9:
        time.sleep(1.75)
        square9()
    if p2spot == 10:
        time.sleep(1.75)
        square10()
    if p2spot == 11:
        time.sleep(1.75)
        square11()
    if p2spot == 12:
        time.sleep(1.75)
        square12()
    if p2spot == 13:
        time.sleep(1.75)
        square13()
    if p2spot == 14:
        time.sleep(1.75)
        square14()
    if p2spot == 15:
        time.sleep(1.75)
        square15()
    if p2spot == 16:
        time.sleep(1.75)
        square16()
    if p2spot == 17:
        time.sleep(1.75)
        square17()
    if p2spot == 18:
        time.sleep(1.75)
        square18()
    if p2spot == 19:
        time.sleep(1.75)
        square19()
    if p2spot == 20:
        time.sleep(1.75)
        square20()
    if p2spot == 21:
        time.sleep(1.75)
        square21()
    if p2spot == 22:
        time.sleep(1.75)
        square22()
    if p2spot == 23:
        time.sleep(1.75)
        square23()
    if p2spot == 24:
        time.sleep(1.75)
        square24()
    if p2spot == 25:
        time.sleep(1.75)
        square25()
    if p2spot == 26:
        time.sleep(1.75)
        square26()
    if p2spot == 27:
        time.sleep(1.75)
        square27()
    if p2spot == 28:
        time.sleep(1.75)
        square28()
    if p2spot == 29:
        time.sleep(1.75)
        square29()
    if p2spot == 30:
        time.sleep(1.75)
        square30()
    if p2spot == 31:
        time.sleep(1.75)
        square31()
    if p2spot == 32:
        time.sleep(1.75)
        square32()
    if p2spot == 33:
        time.sleep(1.75)
        square33()
    if p2spot == 34:
        time.sleep(1.75)
        square34()
    if p2spot == 35:
        time.sleep(1.75)
        square35()
    if p2spot == 36:
        time.sleep(1.75)
        square36()
    if p2spot == 37:
        time.sleep(1.75)
        square37()
    if p2spot == 38:
        time.sleep(1.75)
        square38()
    if p2spot == 39:
        time.sleep(1.75)
        square39()
    if p2spot == 40:
        time.sleep(1.75)
        square40()
    if p2spot == 41:
        time.sleep(1.75)
        square41()
    if p2spot == 42:
        time.sleep(1.75)
        square42()
    if p2spot == 43:
        time.sleep(1.75)
        square43()
    if p2spot == 44:
        time.sleep(1.75)
        square44()
    if p2spot == 45:
        time.sleep(1.75)
        square45()
    if p2spot == 46:
        time.sleep(1.75)
        square46()
    if p2spot == 47:
        time.sleep(1.75)
        square47()
    if p2spot == 48:
        time.sleep(1.75)
        square48()
    if p2spot == 49:
        time.sleep(1.75)
        square49()
    if p2spot == 50:
        time.sleep(1.75)
        square50()
    if p2spot == 51:
        time.sleep(1.75)
        square51()
    if p2spot == 52:
        time.sleep(1.75)
        square52()
    if p2spot == 53:
        time.sleep(1.75)
        square53()
    if p2spot == 54:
        time.sleep(1.75)
        square54()
    if p2spot == 55:
        time.sleep(1.75)
        square55()
    if p2spot == 56:
        time.sleep(1.75)
        square56()
    if p2spot == 57:
        time.sleep(1.75)
        square57()
    if p2spot == 58:
        time.sleep(1.75)
        square58()
    if p2spot == 59:
        time.sleep(1.75)
        square59()
    if p2spot == 60:
        time.sleep(1.75)
        square60()
    if p2spot == 61:
        time.sleep(1.75)
        square61()
    if p2spot == 62:
        time.sleep(1.75)
        square62()
    if p2spot == 63:
        time.sleep(1.75)
        square63()
    if p2spot >= 64:
        time.sleep(1.75)
        square64()


def p3move():
    global p3spot
    if p3spot == 2:
        time.sleep(1.75)
        square2()
    if p3spot == 3:
        time.sleep(1.75)
        square3()
    if p3spot == 4:
        time.sleep(1.75)
        square4()
    if p3spot == 5:
        time.sleep(1.75)
        square5()
    if p3spot == 6:
        time.sleep(1.75)
        square6()
    if p3spot == 7:
        time.sleep(1.75)
        square7()
    if p3spot == 8:
        time.sleep(1.75)
        square8()
    if p3spot == 9:
        time.sleep(1.75)
        square9()
    if p3spot == 10:
        time.sleep(1.75)
        square10()
    if p3spot == 11:
        time.sleep(1.75)
        square11()
    if p3spot == 12:
        time.sleep(1.75)
        square12()
    if p3spot == 13:
        time.sleep(1.75)
        square13()
    if p3spot == 14:
        time.sleep(1.75)
        square14()
    if p3spot == 15:
        time.sleep(1.75)
        square15()
    if p3spot == 16:
        time.sleep(1.75)
        square16()
    if p3spot == 17:
        time.sleep(1.75)
        square17()
    if p3spot == 18:
        time.sleep(1.75)
        square18()
    if p3spot == 19:
        time.sleep(1.75)
        square19()
    if p3spot == 20:
        time.sleep(1.75)
        square20()
    if p3spot == 21:
        time.sleep(1.75)
        square21()
    if p3spot == 22:
        time.sleep(1.75)
        square22()
    if p3spot == 23:
        time.sleep(1.75)
        square23()
    if p3spot == 24:
        time.sleep(1.75)
        square24()
    if p3spot == 25:
        time.sleep(1.75)
        square25()
    if p3spot == 26:
        time.sleep(1.75)
        square26()
    if p3spot == 27:
        time.sleep(1.75)
        square27()
    if p3spot == 28:
        time.sleep(1.75)
        square28()
    if p3spot == 29:
        time.sleep(1.75)
        square29()
    if p3spot == 30:
        time.sleep(1.75)
        square30()
    if p3spot == 31:
        time.sleep(1.75)
        square31()
    if p3spot == 32:
        time.sleep(1.75)
        square32()
    if p3spot == 33:
        time.sleep(1.75)
        square33()
    if p3spot == 34:
        time.sleep(1.75)
        square34()
    if p3spot == 35:
        time.sleep(1.75)
        square35()
    if p3spot == 36:
        time.sleep(1.75)
        square36()
    if p3spot == 37:
        time.sleep(1.75)
        square37()
    if p3spot == 38:
        time.sleep(1.75)
        square38()
    if p3spot == 39:
        time.sleep(1.75)
        square39()
    if p3spot == 40:
        time.sleep(1.75)
        square40()
    if p3spot == 41:
        time.sleep(1.75)
        square41()
    if p3spot == 42:
        time.sleep(1.75)
        square42()
    if p3spot == 43:
        time.sleep(1.75)
        square43()
    if p3spot == 44:
        time.sleep(1.75)
        square44()
    if p3spot == 45:
        time.sleep(1.75)
        square45()
    if p3spot == 46:
        time.sleep(1.75)
        square46()
    if p3spot == 47:
        time.sleep(1.75)
        square47()
    if p3spot == 48:
        time.sleep(1.75)
        square48()
    if p3spot == 49:
        time.sleep(1.75)
        square49()
    if p3spot == 50:
        time.sleep(1.75)
        square50()
    if p3spot == 51:
        time.sleep(1.75)
        square51()
    if p3spot == 52:
        time.sleep(1.75)
        square52()
    if p3spot == 53:
        time.sleep(1.75)
        square53()
    if p3spot == 54:
        time.sleep(1.75)
        square54()
    if p3spot == 55:
        time.sleep(1.75)
        square55()
    if p3spot == 56:
        time.sleep(1.75)
        square56()
    if p3spot == 57:
        time.sleep(1.75)
        square57()
    if p3spot == 58:
        time.sleep(1.75)
        square58()
    if p3spot == 59:
        time.sleep(1.75)
        square59()
    if p3spot == 60:
        time.sleep(1.75)
        square60()
    if p3spot == 61:
        time.sleep(1.75)
        square61()
    if p3spot == 62:
        time.sleep(1.75)
        square62()
    if p3spot == 63:
        time.sleep(1.75)
        square63()
    if p3spot >= 64:
        time.sleep(1.75)
        square64()


def p4move():
    global p4spot
    if p4spot == 2:
        square2()
    if p4spot == 3:
        square3()
    if p4spot == 4:
        square4()
    if p4spot == 5:
        square5()
    if p4spot == 6:
        square6()
    if p4spot == 7:
        square7()
    if p4spot == 8:
        square8()
    if p4spot == 9:
        square9()
    if p4spot == 10:
        square10()
    if p4spot == 11:
        square11()
    if p4spot == 12:
        square12()
    if p4spot == 13:
        square13()
    if p4spot == 14:
        square14()
    if p4spot == 15:
        square15()
    if p4spot == 16:
        square16()
    if p4spot == 17:
        square17()
    if p4spot == 18:
        square18()
    if p4spot == 19:
        square19()
    if p4spot == 20:
        square20()
    if p4spot == 21:
        square21()
    if p4spot == 22:
        square22()
    if p4spot == 23:
        square23()
    if p4spot == 24:
        square24()
    if p4spot == 25:
        square25()
    if p4spot == 26:
        square26()
    if p4spot == 27:
        square27()
    if p4spot == 28:
        square28()
    if p4spot == 29:
        square29()
    if p4spot == 30:
        square30()
    if p4spot == 31:
        square31()
    if p4spot == 32:
        square32()
    if p4spot == 33:
        square33()
    if p4spot == 34:
        square34()
    if p4spot == 35:
        square35()
    if p4spot == 36:
        square36()
    if p4spot == 37:
        square37()
    if p4spot == 38:
        square38()
    if p4spot == 39:
        square39()
    if p4spot == 40:
        square40()
    if p4spot == 41:
        square41()
    if p4spot == 42:
        square42()
    if p4spot == 43:
        square43()
    if p4spot == 44:
        square44()
    if p4spot == 45:
        square45()
    if p4spot == 46:
        square46()
    if p4spot == 47:
        square47()
    if p4spot == 48:
        square48()
    if p4spot == 49:
        square49()
    if p4spot == 50:
        square50()
    if p4spot == 51:
        square51()
    if p4spot == 52:
        square52()
    if p4spot == 53:
        square53()
    if p4spot == 54:
        square54()
    if p4spot == 55:
        square55()
    if p4spot == 56:
        square56()
    if p4spot == 57:
        square57()
    if p4spot == 58:
        square58()
    if p4spot == 59:
        square59()
    if p4spot == 60:
        square60()
    if p4spot == 61:
        square61()
    if p4spot == 62:
        square62()
    if p4spot == 63:
        square63()
    if p4spot >= 64:
        square64()


def square1():
    print("Welcome to our totally original board game that wasn't based off of Game of Life or Mario Party...")
    time.sleep(1.75)
    print("*cough cough*")
    time.sleep(1.75)
    print("Anyways, cue introduction!")
    time.sleep(1.75)
    print("PARTY OF LYFE")
    time.sleep(1.75)
    print("Our game is a 4 player, textbased, board-style experience.")
    time.sleep(1.75)
    print("Where the goal is to reach the end of the 64 square board,")
    time.sleep(1.75)
    print("while fighting your fellow players along the way.")
    time.sleep(1.75)
    print("You will all start with 100 health and deal out 10 damage.")
    time.sleep(1.75)
    print("Here is the map")
    time.sleep(1.5)
    mapview()
    print("Now that you guys get the basics, let's start!")
    diceroll1()


def square2():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Oooh, you found a humongous burger.")
    time.sleep(1.75)
    print("*munch munch* You gained 5 health!")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square3():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nothing happens to you...")
    time.sleep(1.75)
    print("Or does it...")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square4():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Ooooh, you found a humongous burger.")
    time.sleep(1.75)
    print("*munch munch* UGHHH, it was a rotten burger.")
    time.sleep(1.75)
    print("You lose 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square5():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You do nothing. What a nerd.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square6():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("A rat found you!")
    time.sleep(1.75)
    print("It bit you, you lose 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square7():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("FoOOOooD, you gain 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square8():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health because of some magical wizard. ")
    time.sleep(1.75)
    print("...")
    time.sleep(1.75)
    print(":/")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square9():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square10():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health because of some drink you found... in a trashcan.")
    time.sleep(1.75)
    print("Don't ask why you drank a drink in a trashcan.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square11():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square12():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You step in some dog poo. You lose some health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square13():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health because you are cool.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square14():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe, since you are lucky you gain 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square15():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square16():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health cause you got too drunk and tripped over random stuff.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square17():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square18():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some woodchips and get splinters. You lose some health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square19():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health cuz magic.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square20():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice, you landed on a safe square. Since you are lucky you gain 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square21():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square22():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print(
        "You lose 5 health cause you ran over a baby, cried yourself to sleep, and didn't eat anything cause you are a massive dissapointment.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square23():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square24():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square25():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square26():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Because you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square27():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square28():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square29():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square30():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square31():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square32():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square33():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square34():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square35():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square36():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square37():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square38():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square.Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square39():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square40():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square41():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square42():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square43():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square44():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square45():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square46():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square47():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square48():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square49():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square50():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square51():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square52():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square53():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square54():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square55():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square56():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square57():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square.Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square58():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square59():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square60():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square61():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square62():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square63():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square64():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You reached the end!")
    if p1c == 1:
        print("Player 1 Wins")
        sys.exit()
    if p1c == 2:
        print("Player 2  Wins")
        sys.exit()
    if p1c == 3:
        print("Player 3 Wins")
        sys.exit()
    if p1c == 4:
        print("Player 4 Wins")
        sys.exit()


square1()
import time
import random
import sys

global roll
global p1spot
global p2spot
global p3spot
global p4spot
global p1health
global p2health
global p3health
global p4health

p1spot = 1
p2spot = 1
p3spot = 1
p4spot = 1

p1c = 1

p1health = 100
p2health = 100
p3health = 100
p4health = 100


def mapview():
    print(
        " _____________________________________________________________________________________________________________________________________________________________________")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|       START        _          2         _          3         _         4         _         5          _          6         _         7          _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|-------------------------------------------------------------------------------------------------------------------------------------------------_         8         |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|                    _           14       _           13       _          12       _          11        _         10         _         9          _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|          15        _------------------------------------------------------------------------------------------------------------------------------------------------|")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|                    _          16        _          17        _         18        _         19         _         20         _         21         _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|-------------------------------------------------------------------------------------------------------------------------------------------------_         22        |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|                    _          28        _          27        _         26        _         25         _         24         _         23         _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    time.sleep(.75)
    print(
        "|          29        _------------------------------------------------------------------------------------------------------------------------------------------------|")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          30        _          31        _         32        _          33        _         34         _         35         _                   |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|-------------------------------------------------------------------------------------------------------------------------------------------------_         36        |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          42        _          41        _         40        _          39        _         38         _         37         _                   |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|          43        _------------------------------------------------------------------------------------------------------------------------------------------------|")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          44        _          45        _         46        _          47        _         48         _         49         _                   |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|-------------------------------------------------------------------------------------------------------------------------------------------------_         50        |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          56        _          55        _         54        _          53        _         52         _          51        _                   |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|          57        _------------------------------------------------------------------------------------------------------------------------------------------------|")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _          58        _          59        _         60        _          61        _         62         _          63        _         END       |")
    time.sleep(.75)
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|                    _                    _                    _                   _                    _                    _                    _                   |")
    print(
        "|_____________________________________________________________________________________________________________________________________________________________________|")


def diceroll4():
    global p1c
    global p4spot
    print("Player 4 you are on")
    time.sleep(1.75)
    print(p4spot)
    time.sleep(1.75)
    roll = random.randint(1, 6)
    rollinput = input("Type R to roll")
    if rollinput == "r" or not rollinput == "r":
        print("You rolled a........")
        time.sleep(1.75)
        print(roll)
        p4spot = p4spot + roll
        p1c = 4
        p4move()


def diceroll3():
    global p1c
    global p3spot
    print("Player 3 you are on")
    time.sleep(1.75)
    print(p3spot)
    time.sleep(1.75)
    roll = random.randint(1, 6)
    rollinput = input("Type R to roll")
    if rollinput == "r" or not rollinput == "r":
        print("You rolled a........")
        time.sleep(1.75)
        print(roll)
        p3spot = p3spot + roll
        p1c = 3
        p3move()


def diceroll2():
    global p1c
    global p2spot
    print("Player 2 you are on")
    time.sleep(1.75)
    print(p2spot)
    roll = random.randint(1, 6)
    rollinput = input("Type R to roll")
    if rollinput == "r" or not rollinput == "r":
        print("You rolled a........")
        time.sleep(1.75)
        print(roll)
        p2spot = p2spot + roll
        p1c = 2
        p2move()


def diceroll1():
    fightinit = random.randint(1, 10)
    if fightinit >= 6:
        global p1c
        global p1spot
        print("Player 1 you are on ")
        time.sleep(1.75)
        print(p1spot)
        time.sleep(1.75)
        roll = random.randint(1, 6)
        time.sleep(1.75)
        rollinput = input("Type R to roll")
        if rollinput == "r" or not rollinput == "r":
            print("You rolled a........")
            time.sleep(1.75)
            print(roll)
            p1spot = p1spot + roll
            p1c = 1
            p1move()
    else:
        fightmechanicsinit()


def heavyp24():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p2health = p2health - 10
        print("Player 2 Health")
        print(p2health)
        if p2health == 0:
            p2spot = 2
            diceroll1()
        fightmechanics42()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 40
        if p4health <= 1:
            p4spot = 2
            diceroll1()
        fightmechanics42()


def lightp24():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p2health = p2health - 10
        print("Player 2 Health")
        print(p2health)
        fightmechanics42()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 20
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics42()


def heavyp42():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 4 Health")
        print(p4health)
        fightmechanics24()
        if p2health <= 0:
            print("Player 2 has died")
            diceroll1()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 40
        fightmechanics24()


def lightp42():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics24()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics24()


def heavyp43():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p4health = p4health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics34()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 40
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics34()


def lightp43():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p4health = p4health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics34()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 20
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics34()


def heavyp34():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics43()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 40
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics43()


def lightp34():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        fightmechanics43()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 20
        if p4health < 4:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics43()


def heavyp31():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            diceroll1()
        fightmechanics13()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p1health = p1health - 40
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics13()


def lightp31():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            diceroll1()
        fightmechanics13()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics13()


def heavyp13():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("p1health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            diceroll1()
        fightmechanics31()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 40
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics31()


def lightp13():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics31()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics31()


def heavyp23():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p2health = p2health - 10
        print("Player 2 Health")
        print(p2health)
        if p2health <= 1:
            p2spot = 2
            diceroll1()
        fightmechanics32()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 40
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics23()


def lightp23():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p2health = p2health - 10
        print("Player 2 Health")
        print(p2health)
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics32()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 20
        if p3health <= 1:
            p3spot = 2
            print("Player 3v has died")
            diceroll1()
        fightmechanics32()


def heavyp32():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics23()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 40
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics23()


def lightp32():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics23()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics23()


def heavyp41():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p4health = p4health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics14()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p1health = p1health - 40
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics14()


def lightp41():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p4health = p4health - 10
        print("Player 4 Health")
        print(p4health)
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics14()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p1health = p1health - 20
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics14()


def heavyp14():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics41()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 40
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics41()


def lightp14():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics41()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p4health = p4health - 20
        if p4health <= 1:
            p4spot = 2
            print("Player 4 has died")
            diceroll1()
        fightmechanics41()


def heavyp31():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics13()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p1health = p1health - 40
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics13()


def lightp31():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics13()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics13()


def heavyp13():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics31()
    else:
        print("Your heavy attack was sucessful!")
        time.sleep(1.75)
        p3health = p3health - 40
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics31()


def lightp13():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p3health = p3health - 10
        print("Player 3 Health")
        print(p3health)
        if p3health <= 1:
            p3spot = 2
            print("Player 3 has died")
            diceroll1()
        fightmechanics31()
    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            diceroll1()
        fightmechanics31()


def heavyp12():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics21()

    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 40
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics21()


def lightp12():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics21()


def heavyp12():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a heavy attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 3.5:
        print("You missed your heavy attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
            diceroll1()
        fightmechanics21()

    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 40
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
            diceroll1()
        fightmechanics21()


def lightp12():
    global p1health
    global p2health
    global p3health
    global p4health
    print("You decide to do a light attack.")
    time.sleep(1.75)
    rheavy1 = random.randint(1, 10)
    if rheavy1 >= 7.5:
        print("You missed your light attack, you were out in the open so you took 10 damage.")
        p1health = p1health - 10
        print("Player 1 Health")
        print(p1health)
        if p1health <= 1:
            p1spot = 2
            print("Player 1 has died")
        fightmechanics21()

    else:
        print("Your light attack was sucessful!")
        time.sleep(1.75)
        p2health = p2health - 20
        if p2health <= 1:
            p2spot = 2
            print("Player 2 has died")
        fightmechanics21()
        p1move()


def fightmechanics12():
    print("Player 1 you are attacking Player 2")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp12()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp12()


def fightmechanics13():
    print("Player 1 you are attacking Player 3")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp13()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp13()


def fightmechanics21():
    print("Player 2 you are attacking Player 1")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp21()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp21()


def fightmechanics14():
    print("Player 1 you are attacking Player 4")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp14()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp14()


def fightmechanics23():
    print("Player 2 you are attacking Player 3")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp13()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp13()


def fightmechanics24():
    print("Player 2 you are attacking Player 4")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp24()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp24()


def fightmechanics34():
    print("Player 3 you are attacking Player 4")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp34()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp34()


def fightmechanics31():
    print("Player 3 you are attacking Player 1")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp31()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp31()


def fightmechanics41():
    print("Player 4 you are attacking Player 1")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp41()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp41()


def fightmechanics32():
    print("Player 2 you are attacking Player 3")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp32()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp32()


def fightmechanics43():
    print("Player 4 you are attacking Player 3")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp43()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp43()


def fightmechanics42():
    print("Player 4 you are attacking Player 2")
    fightop1 = input("How do you want to attack? {Light Attack} or {Heavy Attack}")
    if fightop1 == "Light Attack":  # 85%
        lightp42()
    if fightop1 == "Heavy Attack":  # 65%
        heavyp42()


def fightmechanicsinit():
    global roll
    global p1spot
    global p2spot
    global p3spot
    global p4spot
    global p1health
    global p2health
    global p3health
    global p4health
    roof = random.randint(1, 12)
    if roof == 1:
        fightmechanics12()
    if roof == 2:
        fightmechanics21()
    if roof == 3:
        fightmechanics13()
    if roof == 4:
        fightmechanics31()
    if roof == 5:
        fightmechanics14()
    if roof == 6:
        fightmechanics41()
    if roof == 7:
        fightmechanics23()
    if roof == 8:
        fightmechanics32()
    if roof == 9:
        fightmechanics24()
    if roof == 10:
        fightmechanics42()
    if roof == 11:
        fightmechanics43()
    if roof == 12:
        fightmechanics34()


def p1move():
    global p1spot
    if p1spot == 2:
        time.sleep(1.75)
        square2()
    if p1spot == 3:
        time.sleep(1.75)
        square3()
    if p1spot == 4:
        time.sleep(1.75)
        square4()
    if p1spot == 5:
        time.sleep(1.75)
        square5()
    if p1spot == 6:
        time.sleep(1.75)
        square6()
    if p1spot == 7:
        time.sleep(1.75)
        square7()
    if p1spot == 8:
        time.sleep(1.75)
        square8()
    if p1spot == 9:
        time.sleep(1.75)
        square9()
    if p1spot == 10:
        time.sleep(1.75)
        square10()
    if p1spot == 11:
        time.sleep(1.75)
        square11()
    if p1spot == 12:
        time.sleep(1.75)
        square12()
    if p1spot == 13:
        time.sleep(1.75)
        square13()
    if p1spot == 14:
        time.sleep(1.75)
        square14()
    if p1spot == 15:
        time.sleep(1.75)
        square15()
    if p1spot == 16:
        time.sleep(1.75)
        square16()
    if p1spot == 17:
        time.sleep(1.75)
        square17()
    if p1spot == 18:
        time.sleep(1.75)
        square18()
    if p1spot == 19:
        time.sleep(1.75)
        square19()
    if p1spot == 20:
        time.sleep(1.75)
        square20()
    if p1spot == 21:
        time.sleep(1.75)
        square21()
    if p1spot == 22:
        time.sleep(1.75)
        square22()
    if p1spot == 23:
        time.sleep(1.75)
        square23()
    if p1spot == 24:
        time.sleep(1.75)
        square24()
    if p1spot == 25:
        time.sleep(1.75)
        square25()
    if p1spot == 26:
        time.sleep(1.75)
        square26()
    if p1spot == 27:
        time.sleep(1.75)
        square27()
    if p1spot == 28:
        time.sleep(1.75)
        square28()
    if p1spot == 29:
        time.sleep(1.75)
        square29()
    if p1spot == 30:
        time.sleep(1.75)
        square30()
    if p1spot == 31:
        time.sleep(1.75)
        square31()
    if p1spot == 32:
        time.sleep(1.75)
        square32()
    if p1spot == 33:
        time.sleep(1.75)
        square33()
    if p1spot == 34:
        time.sleep(1.75)
        square34()
    if p1spot == 35:
        time.sleep(1.75)
        square35()
    if p1spot == 36:
        time.sleep(1.75)
        square36()
    if p1spot == 37:
        time.sleep(1.75)
        square37()
    if p1spot == 38:
        time.sleep(1.75)
        square38()
    if p1spot == 39:
        time.sleep(1.75)
        square39()
    if p1spot == 40:
        time.sleep(1.75)
        square40()
    if p1spot == 41:
        time.sleep(1.75)
        square41()
    if p1spot == 42:
        time.sleep(1.75)
        square42()
    if p1spot == 43:
        time.sleep(1.75)
        square43()
    if p1spot == 44:
        time.sleep(1.75)
        square44()
    if p1spot == 45:
        time.sleep(1.75)
        square45()
    if p1spot == 46:
        time.sleep(1.75)
        square46()
    if p1spot == 47:
        time.sleep(1.75)
        square47()
    if p1spot == 48:
        time.sleep(1.75)
        square48()
    if p1spot == 49:
        time.sleep(1.75)
        square49()
    if p1spot == 50:
        time.sleep(1.75)
        square50()
    if p1spot == 51:
        time.sleep(1.75)
        square51()
    if p1spot == 52:
        time.sleep(1.75)
        square52()
    if p1spot == 53:
        time.sleep(1.75)
        square53()
    if p1spot == 54:
        time.sleep(1.75)
        square54()
    if p1spot == 55:
        time.sleep(1.75)
        square55()
    if p1spot == 56:
        time.sleep(1.75)
        square56()
    if p1spot == 57:
        time.sleep(1.75)
        square57()
    if p1spot == 58:
        time.sleep(1.75)
        square58()
    if p1spot == 59:
        time.sleep(1.75)
        square59()
    if p1spot == 60:
        time.sleep(1.75)
        square60()
    if p1spot == 61:
        time.sleep(1.75)
        square61()
    if p1spot == 62:
        time.sleep(1.75)
        square62()
    if p1spot == 63:
        time.sleep(1.75)
        square63()
    if p1spot >= 64:
        time.sleep(1.75)
        square64()


def p2move():
    global p2spot
    if p2spot == 2:
        time.sleep(1.75)
        square2()
    if p2spot == 3:
        time.sleep(1.75)
        square3()
    if p2spot == 4:
        time.sleep(1.75)
        square4()
    if p2spot == 5:
        time.sleep(1.75)
        square5()
    if p2spot == 6:
        time.sleep(1.75)
        square6()
    if p2spot == 7:
        time.sleep(1.75)
        square7()
    if p2spot == 8:
        time.sleep(1.75)
        square8()
    if p2spot == 9:
        time.sleep(1.75)
        square9()
    if p2spot == 10:
        time.sleep(1.75)
        square10()
    if p2spot == 11:
        time.sleep(1.75)
        square11()
    if p2spot == 12:
        time.sleep(1.75)
        square12()
    if p2spot == 13:
        time.sleep(1.75)
        square13()
    if p2spot == 14:
        time.sleep(1.75)
        square14()
    if p2spot == 15:
        time.sleep(1.75)
        square15()
    if p2spot == 16:
        time.sleep(1.75)
        square16()
    if p2spot == 17:
        time.sleep(1.75)
        square17()
    if p2spot == 18:
        time.sleep(1.75)
        square18()
    if p2spot == 19:
        time.sleep(1.75)
        square19()
    if p2spot == 20:
        time.sleep(1.75)
        square20()
    if p2spot == 21:
        time.sleep(1.75)
        square21()
    if p2spot == 22:
        time.sleep(1.75)
        square22()
    if p2spot == 23:
        time.sleep(1.75)
        square23()
    if p2spot == 24:
        time.sleep(1.75)
        square24()
    if p2spot == 25:
        time.sleep(1.75)
        square25()
    if p2spot == 26:
        time.sleep(1.75)
        square26()
    if p2spot == 27:
        time.sleep(1.75)
        square27()
    if p2spot == 28:
        time.sleep(1.75)
        square28()
    if p2spot == 29:
        time.sleep(1.75)
        square29()
    if p2spot == 30:
        time.sleep(1.75)
        square30()
    if p2spot == 31:
        time.sleep(1.75)
        square31()
    if p2spot == 32:
        time.sleep(1.75)
        square32()
    if p2spot == 33:
        time.sleep(1.75)
        square33()
    if p2spot == 34:
        time.sleep(1.75)
        square34()
    if p2spot == 35:
        time.sleep(1.75)
        square35()
    if p2spot == 36:
        time.sleep(1.75)
        square36()
    if p2spot == 37:
        time.sleep(1.75)
        square37()
    if p2spot == 38:
        time.sleep(1.75)
        square38()
    if p2spot == 39:
        time.sleep(1.75)
        square39()
    if p2spot == 40:
        time.sleep(1.75)
        square40()
    if p2spot == 41:
        time.sleep(1.75)
        square41()
    if p2spot == 42:
        time.sleep(1.75)
        square42()
    if p2spot == 43:
        time.sleep(1.75)
        square43()
    if p2spot == 44:
        time.sleep(1.75)
        square44()
    if p2spot == 45:
        time.sleep(1.75)
        square45()
    if p2spot == 46:
        time.sleep(1.75)
        square46()
    if p2spot == 47:
        time.sleep(1.75)
        square47()
    if p2spot == 48:
        time.sleep(1.75)
        square48()
    if p2spot == 49:
        time.sleep(1.75)
        square49()
    if p2spot == 50:
        time.sleep(1.75)
        square50()
    if p2spot == 51:
        time.sleep(1.75)
        square51()
    if p2spot == 52:
        time.sleep(1.75)
        square52()
    if p2spot == 53:
        time.sleep(1.75)
        square53()
    if p2spot == 54:
        time.sleep(1.75)
        square54()
    if p2spot == 55:
        time.sleep(1.75)
        square55()
    if p2spot == 56:
        time.sleep(1.75)
        square56()
    if p2spot == 57:
        time.sleep(1.75)
        square57()
    if p2spot == 58:
        time.sleep(1.75)
        square58()
    if p2spot == 59:
        time.sleep(1.75)
        square59()
    if p2spot == 60:
        time.sleep(1.75)
        square60()
    if p2spot == 61:
        time.sleep(1.75)
        square61()
    if p2spot == 62:
        time.sleep(1.75)
        square62()
    if p2spot == 63:
        time.sleep(1.75)
        square63()
    if p2spot >= 64:
        time.sleep(1.75)
        square64()


def p3move():
    global p3spot
    if p3spot == 2:
        time.sleep(1.75)
        square2()
    if p3spot == 3:
        time.sleep(1.75)
        square3()
    if p3spot == 4:
        time.sleep(1.75)
        square4()
    if p3spot == 5:
        time.sleep(1.75)
        square5()
    if p3spot == 6:
        time.sleep(1.75)
        square6()
    if p3spot == 7:
        time.sleep(1.75)
        square7()
    if p3spot == 8:
        time.sleep(1.75)
        square8()
    if p3spot == 9:
        time.sleep(1.75)
        square9()
    if p3spot == 10:
        time.sleep(1.75)
        square10()
    if p3spot == 11:
        time.sleep(1.75)
        square11()
    if p3spot == 12:
        time.sleep(1.75)
        square12()
    if p3spot == 13:
        time.sleep(1.75)
        square13()
    if p3spot == 14:
        time.sleep(1.75)
        square14()
    if p3spot == 15:
        time.sleep(1.75)
        square15()
    if p3spot == 16:
        time.sleep(1.75)
        square16()
    if p3spot == 17:
        time.sleep(1.75)
        square17()
    if p3spot == 18:
        time.sleep(1.75)
        square18()
    if p3spot == 19:
        time.sleep(1.75)
        square19()
    if p3spot == 20:
        time.sleep(1.75)
        square20()
    if p3spot == 21:
        time.sleep(1.75)
        square21()
    if p3spot == 22:
        time.sleep(1.75)
        square22()
    if p3spot == 23:
        time.sleep(1.75)
        square23()
    if p3spot == 24:
        time.sleep(1.75)
        square24()
    if p3spot == 25:
        time.sleep(1.75)
        square25()
    if p3spot == 26:
        time.sleep(1.75)
        square26()
    if p3spot == 27:
        time.sleep(1.75)
        square27()
    if p3spot == 28:
        time.sleep(1.75)
        square28()
    if p3spot == 29:
        time.sleep(1.75)
        square29()
    if p3spot == 30:
        time.sleep(1.75)
        square30()
    if p3spot == 31:
        time.sleep(1.75)
        square31()
    if p3spot == 32:
        time.sleep(1.75)
        square32()
    if p3spot == 33:
        time.sleep(1.75)
        square33()
    if p3spot == 34:
        time.sleep(1.75)
        square34()
    if p3spot == 35:
        time.sleep(1.75)
        square35()
    if p3spot == 36:
        time.sleep(1.75)
        square36()
    if p3spot == 37:
        time.sleep(1.75)
        square37()
    if p3spot == 38:
        time.sleep(1.75)
        square38()
    if p3spot == 39:
        time.sleep(1.75)
        square39()
    if p3spot == 40:
        time.sleep(1.75)
        square40()
    if p3spot == 41:
        time.sleep(1.75)
        square41()
    if p3spot == 42:
        time.sleep(1.75)
        square42()
    if p3spot == 43:
        time.sleep(1.75)
        square43()
    if p3spot == 44:
        time.sleep(1.75)
        square44()
    if p3spot == 45:
        time.sleep(1.75)
        square45()
    if p3spot == 46:
        time.sleep(1.75)
        square46()
    if p3spot == 47:
        time.sleep(1.75)
        square47()
    if p3spot == 48:
        time.sleep(1.75)
        square48()
    if p3spot == 49:
        time.sleep(1.75)
        square49()
    if p3spot == 50:
        time.sleep(1.75)
        square50()
    if p3spot == 51:
        time.sleep(1.75)
        square51()
    if p3spot == 52:
        time.sleep(1.75)
        square52()
    if p3spot == 53:
        time.sleep(1.75)
        square53()
    if p3spot == 54:
        time.sleep(1.75)
        square54()
    if p3spot == 55:
        time.sleep(1.75)
        square55()
    if p3spot == 56:
        time.sleep(1.75)
        square56()
    if p3spot == 57:
        time.sleep(1.75)
        square57()
    if p3spot == 58:
        time.sleep(1.75)
        square58()
    if p3spot == 59:
        time.sleep(1.75)
        square59()
    if p3spot == 60:
        time.sleep(1.75)
        square60()
    if p3spot == 61:
        time.sleep(1.75)
        square61()
    if p3spot == 62:
        time.sleep(1.75)
        square62()
    if p3spot == 63:
        time.sleep(1.75)
        square63()
    if p3spot >= 64:
        time.sleep(1.75)
        square64()


def p4move():
    global p4spot
    if p4spot == 2:
        square2()
    if p4spot == 3:
        square3()
    if p4spot == 4:
        square4()
    if p4spot == 5:
        square5()
    if p4spot == 6:
        square6()
    if p4spot == 7:
        square7()
    if p4spot == 8:
        square8()
    if p4spot == 9:
        square9()
    if p4spot == 10:
        square10()
    if p4spot == 11:
        square11()
    if p4spot == 12:
        square12()
    if p4spot == 13:
        square13()
    if p4spot == 14:
        square14()
    if p4spot == 15:
        square15()
    if p4spot == 16:
        square16()
    if p4spot == 17:
        square17()
    if p4spot == 18:
        square18()
    if p4spot == 19:
        square19()
    if p4spot == 20:
        square20()
    if p4spot == 21:
        square21()
    if p4spot == 22:
        square22()
    if p4spot == 23:
        square23()
    if p4spot == 24:
        square24()
    if p4spot == 25:
        square25()
    if p4spot == 26:
        square26()
    if p4spot == 27:
        square27()
    if p4spot == 28:
        square28()
    if p4spot == 29:
        square29()
    if p4spot == 30:
        square30()
    if p4spot == 31:
        square31()
    if p4spot == 32:
        square32()
    if p4spot == 33:
        square33()
    if p4spot == 34:
        square34()
    if p4spot == 35:
        square35()
    if p4spot == 36:
        square36()
    if p4spot == 37:
        square37()
    if p4spot == 38:
        square38()
    if p4spot == 39:
        square39()
    if p4spot == 40:
        square40()
    if p4spot == 41:
        square41()
    if p4spot == 42:
        square42()
    if p4spot == 43:
        square43()
    if p4spot == 44:
        square44()
    if p4spot == 45:
        square45()
    if p4spot == 46:
        square46()
    if p4spot == 47:
        square47()
    if p4spot == 48:
        square48()
    if p4spot == 49:
        square49()
    if p4spot == 50:
        square50()
    if p4spot == 51:
        square51()
    if p4spot == 52:
        square52()
    if p4spot == 53:
        square53()
    if p4spot == 54:
        square54()
    if p4spot == 55:
        square55()
    if p4spot == 56:
        square56()
    if p4spot == 57:
        square57()
    if p4spot == 58:
        square58()
    if p4spot == 59:
        square59()
    if p4spot == 60:
        square60()
    if p4spot == 61:
        square61()
    if p4spot == 62:
        square62()
    if p4spot == 63:
        square63()
    if p4spot >= 64:
        square64()


def square1():
    print("Welcome to our totally original board game that wasn't based off of Game of Life or Mario Party...")
    time.sleep(1.75)
    print("*cough cough*")
    time.sleep(1.75)
    print("Anyways, cue introduction!")
    time.sleep(1.75)
    print("PARTY OF LYFE")
    time.sleep(1.75)
    print("Our game is a 4 player, textbased, board-style experience.")
    time.sleep(1.75)
    print("Where the goal is to reach the end of the 64 square board,")
    time.sleep(1.75)
    print("while fighting your fellow players along the way.")
    time.sleep(1.75)
    print("You will all start with 100 health and deal out 10 damage.")
    time.sleep(1.75)
    print("Here is the map")
    time.sleep(1.5)
    mapview()
    print("Now that you guys get the basics, let's start!")
    diceroll1()


def square2():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Oooh, you found a humongous burger.")
    time.sleep(1.75)
    print("*munch munch* You gained 5 health!")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square3():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nothing happens to you...")
    time.sleep(1.75)
    print("Or does it...")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square4():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Ooooh, you found a humongous burger.")
    time.sleep(1.75)
    print("*munch munch* UGHHH, it was a rotten burger.")
    time.sleep(1.75)
    print("You lose 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square5():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You do nothing. What a nerd.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square6():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("A rat found you!")
    time.sleep(1.75)
    print("It bit you, you lose 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square7():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("FoOOOooD, you gain 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square8():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health because of some magical wizard. ")
    time.sleep(1.75)
    print("...")
    time.sleep(1.75)
    print(":/")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square9():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square10():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health because of some drink you found... in a trashcan.")
    time.sleep(1.75)
    print("Don't ask why you drank a drink in a trashcan.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square11():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square12():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You step in some dog poo. You lose some health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square13():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health because you are cool.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square14():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe, since you are lucky you gain 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square15():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square16():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health cause you got too drunk and tripped over random stuff.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square17():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square18():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some woodchips and get splinters. You lose some health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square19():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health cuz magic.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square20():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice, you landed on a safe square. Since you are lucky you gain 5 health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square21():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square22():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print(
        "You lose 5 health cause you ran over a baby, cried yourself to sleep, and didn't eat anything cause you are a massive dissapointment.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square23():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    time.sleep(1.75)
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square24():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    time.sleep(1.75)
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square25():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square26():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Because you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square27():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square28():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square29():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square30():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square31():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square32():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square33():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square34():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square35():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square36():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square37():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square38():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square.Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square39():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square40():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square41():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square42():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square43():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square44():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square45():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square46():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square47():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square48():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square49():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square50():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square51():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square52():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square53():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square54():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square55():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square56():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square57():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square.Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square58():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square59():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You lose 5 health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square60():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You are safe. Nothing happens to you.")
    if p1c == 1:
        diceroll2()
    if p1c == 2:
        diceroll3()
    if p1c == 3:
        diceroll4()
    if p1c == 4:
        diceroll1()


def square61():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You land on some spikes. You lose some health.")
    if p1c == 1:
        p1health = p1health - 5
        diceroll2()
    if p1c == 2:
        p2health = p2health - 5
        diceroll3()
    if p1c == 3:
        p3health = p3health - 5
        diceroll4()
    if p1c == 4:
        p4health = p4health - 5
        diceroll1()


def square62():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square63():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("Nice you landed on a safe square. Since you are lucky you gain 5 health.")
    if p1c == 1:
        p1health = p1health + 5
        diceroll2()
    if p1c == 2:
        p2health = p2health + 5
        diceroll3()
    if p1c == 3:
        p3health = p3health + 5
        diceroll4()
    if p1c == 4:
        p4health = p4health + 5
        diceroll1()


def square64():
    global p1c
    global p1health
    global p2health
    global p3health
    global p4health
    print("You reached the end!")
    if p1c == 1:
        print("Player 1 Wins")
        sys.exit()
    if p1c == 2:
        print("Player 2  Wins")
        sys.exit()
    if p1c == 3:
        print("Player 3 Wins")
        sys.exit()
    if p1c == 4:
        print("Player 4 Wins")
        sys.exit()


square1()
