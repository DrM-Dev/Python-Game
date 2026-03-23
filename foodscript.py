from turtle import Turtle
import random

#___________________________________________________________
class Food1(Turtle):
    def __init__(self):
        super().__init__()
        #
        #now time to define how the features of food object as soon as it spawns
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5) #by default any circle spawns as 20x20 pixels, this will half it into 10x10
        self.color("yellow")
        self.speed("fastest")
        self.location_refresh()

    def location_refresh(self):
        #now time to randomize the location
        random_X = random.randint(-280, 280)
        random_Y = random.randint(-280, 280)
        self.goto(random_X,random_Y)


#___________________________________________________________
class Food2(Turtle):
    def __init__(self):
        super().__init__()
        #
        self.penup()
        self.shape("circle")
        #self.shapesize(stretch_wid=0.5,stretch_len=0.5) #by default any circle spawns as 20x20 pixels, this will half it into 10x10
        self.color("red")
        self.speed("fastest")
        #
        self.is_f2_active = False
        self.spawn_f2 = False

    #-------------------------------------------------------
    def location_refresh_f2(self):
        if self.is_f2_active == False and self.spawn_f2 == True:
            self.showturtle()
            #
            #now time to randomize the location
            random_X = random.randint(-280, 280)
            random_Y = random.randint(-280, 280)
            self.goto(random_X,random_Y)
            #
            self.is_f2_active = True


    def remove_food2(self):
        self.goto(700,700)
        self.is_f2_active = False