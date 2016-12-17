import turtle  # импортировали черепашку
import math
import random

coords = []
turtle.speed(0)


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def circle_c(x, y, r):  # рисует окружность с центром в точке x,y и радиусом R
    gotoxy(x, y-r)
    turtle.circle(r)


def patr(number, radius):  # патроны(количество патронов, радиус барабана)
    for i in range(0, number):
        R = radius/(1 + math.sin(phi/2))  # радиус патронов
        X = R * math.cos(phi * i)
        Y = R * math.sin(phi * i)
        coords.append([X+x, Y+y])
        circle_c(X+x, Y+y, gun_radius)
# создать список центров патронов и их радиуса


def krutim():
    x = random.randint(7, 50)
    for i in range(0, x):
        turtle.fillcolor("red")
        turtle.begin_fill()
        circle_c(coords[i % number][0], coords[i % number][1], gun_radius)
        turtle.end_fill()
        if i != x-1:
            turtle.fillcolor("white")
            turtle.begin_fill()
            circle_c(coords[i % number][0], coords[i % number][1], gun_radius)
            turtle.end_fill()
        else:
            pass

ans = ""
while ans != "N":
    ans = turtle.textinput("рисуем?", "y,n")
    if ans == "Y" or ans == "y":
        coords = []
        x = int(turtle.textinput("введите координаты центра", "X"))
        y = int(turtle.textinput("введите координаты центра", "Y"))
        radius = int(turtle.textinput("введите радиус", "R"))
        number = int(turtle.textinput(
            "введите количество патронов в барабане", "N"))
        phi = 2*math.pi/number
        gun_radius = radius*math.sin(phi/2)/(1+math.sin(phi/2))
        gotoxy(x, y)
        turtle.circle(1)
        turtle.write("Center", True)
        turtle.write((x, y), True)
        circle_c(x, y, radius)
        gotoxy(x, y+radius)
        turtle.circle(5)
        patr(number, radius)
        krutim()

    elif ans == "N" or ans == "n":
        break
    else:
        print("unknown answer")
