import turtle
import random
import time

wordsDef = {"capacity": ("someone's ability to do something", "Ali has the capacity to think in an original way"),
         "motto": ("a short sentence or phrase giving a rule on how to behave,\n which expresses the aims or beliefs of"
                  + " a person, school or institution", "\"Live in the moment\" is Ahmad's father motto"),
         "gregarious": ("friendly and preferring to be with other people", "Arash is gregarious"),
         "obscure": ("not well known", "The existence of UFOs is obscure so far"),
         "conviction": ("a very strong belief or opinion", "Ali has some weird convictions on politics"),
         "mind-set": ("someone's general attitude, and the way in which they think about things and make decisions"
                      , "Our family and friends have great impact on our mind-set"),
         "philanthropy": ("the practice of giving money and help to people who are poor or in trouble"
                          , "one of Ali's philanthropies is constructing many schools"),
         "initial": ("happening at the beginning", "the initial game we wanted to make was hangman"),
         "eradicating": ("completely getting rid of something such as disease or a social problem", "there is still"
                                                                        " not a certain cure for eradicating cancer"),
         "scale": ("the size or level of something, or the amount that something is happening", "we may never ba able"
                                                                                  " to estimate the scale of universe")}
words = list(wordsDef.keys())

screen = turtle.Screen()

w = turtle.Turtle()
t = turtle.Turtle()
answer = turtle.Turtle()
definition = turtle.Turtle()
ex = turtle.Turtle()
rec = turtle.Turtle()
erase = turtle.Turtle()
bgcolor = ["#90d900", "#19a450", "#ff1040", "#0ff0f0"]
bgr = random.choice(bgcolor)
screen.bgcolor(bgr)

t.speed(3)
t.hideturtle()
t.penup()

w.speed(3)
w.hideturtle()
w.penup()

answer.speed(3)
answer.hideturtle()
answer.penup()

definition.speed(3)
definition.hideturtle()
definition.penup()

ex.speed(3)
ex.hideturtle()
ex.penup()

rec.speed(25)
rec.hideturtle()
rec.penup()

erase.speed(10)
erase.hideturtle()
erase.penup()

t.goto(0, 0)

answer.goto(-50, -110)

definition.goto(0, -180)

ex.goto(0, -220)

w.goto(-40, -50)

rec.goto(250, 80)
rec.pendown()
rec.forward(110)
rec.right(90)
rec.forward(60)
rec.right(90)
rec.forward(110)
rec.right(90)
rec.forward(60)
rec.right(90)
rec.penup()

erase.goto(305, 40)
erase.write("Erase", align="center", font=("arial", 20))

pos = (0, 0)

Lanswer = []


def choose(x):
    for i in range(0, len(Lpos)):
        if x[0] - 25 < Lpos[i][0] < x[0] + 25 and x[1] - 40 < Lpos[i][1] < x[1] + 40:
            global output
            global Lanswer
            global L
            global randomWord

            answer.write(L[i], align="left", font=("arial", 20))
            Lanswer.append(L[i])
            if L[i] in ["i", "t", "l", "r"]:
                answer.forward(15)
            elif L[i] == "m":
                answer.forward(22)
            else:
                answer.forward(20)
            if len(L) == len(Lanswer):
                if ''.join(Lanswer) == randomWord:
                    praise = ["Good Job!", "Well Done!", "Excellent!", "Perfect!"]
                    time.sleep(0.5)
                    answer.clear()
                    t.clear()
                    Lanswer = []
                    answer.goto(0, -110)

                    answer.write(random.choice(praise), align="center", font=("arial", 30))
                    time.sleep(1)
                    answer.clear()
                    answer.goto(0, -110)
                    answer.write(randomWord, align="center", font=("arial", 20))
                    time.sleep(1)
                    definition.write("Definition: " + wordsDef.get(randomWord)[0], align="center", font=("arial", 20))
                    time.sleep(3)
                    ex.write("Example: " + wordsDef.get(randomWord)[1], align="center", font=("arial", 20))
                    time.sleep(8)
                    answer.clear()
                    answer.goto(-50, -110)
                    definition.clear()
                    definition.goto(0, -180)
                    ex.clear()
                    ex.goto(0, -220)
                    w.clear()
                    w.goto(-40, -50)
                    screen.bgcolor(random.choice(bgcolor))
                    randomWord = random.choice(words)
                    L = list(randomWord)
                    random.shuffle(L)
                    words.pop(words.index(randomWord))
                    Lpos.clear()
                    for a in range(0, len(L)):
                        w.forward(75)
                        w.left(360 / len(L))
                        w.write(L[a], align="Left", font=("arial", 20))

                        pos = w.pos()
                        Lpos.append(pos)
                        if len(L) - 1 == a:
                            screen.onscreenclick(Rclick, 3)
                            screen.onscreenclick(Lclick, 1)
                            screen.listen()

                else:
                    answer.clear()
                    answer.goto(-10, -150)
                    answer.write("Try again!", align="center", font=("arial", 30))
                    time.sleep(1)
                    answer.clear()
                    answer.goto(-50, -110)
                    t.clear()
                    Lanswer = []
        elif 250 < x[0] < 350 and 20 < x[1] < 80:
            t.clear()
            answer.clear()
            Lanswer.clear()
            answer.goto(-50, -110)


def Lclick(z, y):
    t.pendown()
    t.goto(z, y)
    choose(t.pos())


def Rclick(z, y):
    t.penup()
    t.goto(z, y)
    choose(t.pos())


Lpos = []

while words:

    randomWord = random.choice(words)
    L = list(randomWord)
    random.shuffle(L)
    words.pop(words.index(randomWord))
    answer.goto(-len(L)*10, -110)
    for i in range(0, len(L)):

        w.forward(75)
        w.left(360/len(L))
        w.write(L[i], align="Left", font=("arial", 20))

        pos = w.pos()
        Lpos.append(pos)

        if len(L)-1 == i:

            screen.onscreenclick(Rclick, 3)
            screen.onscreenclick(Lclick, 1)
            screen.listen()

    break

screen.mainloop()




