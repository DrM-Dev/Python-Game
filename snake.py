from turtle import Turtle
#________________________
# Global Constant\\
CHOSEN_COLOR_SET = ""
#________________________
colors_extended = [
    "white", "black", "red", "green", "blue", "cyan", "yellow", "magenta",
    "gray", "grey", "lightgray", "lightgrey", "darkgray", "darkgrey",
    "orange", "pink", "purple", "brown", "gold", "silver",
    "navy", "skyblue", "turquoise", "violet", "indigo",
    "maroon", "olive", "lime", "teal", "coral", "salmon",
    "khaki", "plum", "orchid", "beige", "ivory", "tan",
    "aliceblue", "antiquewhite", "aqua", "aquamarine",
    "azure", "beige", "bisque", "blanchedalmond",
    "blueviolet", "burlywood", "cadetblue",
    "chartreuse", "chocolate", "coral", "cornflowerblue",
    "cornsilk", "crimson", "darkcyan", "darkgoldenrod",
    "darkgray", "darkkhaki", "darkmagenta", "darkorange",
    "darkorchid", "darksalmon", "darkseagreen",
    "darkslateblue", "darkturquoise", "deeppink",
    "deepskyblue", "dodgerblue", "firebrick",
    "floralwhite", "forestgreen", "gainsboro",
    "ghostwhite", "honeydew", "hotpink",
    "indianred", "indigo", "ivory", "khaki",
    "lavender", "lawngreen", "lemonchiffon",
    "lightcoral", "lightcyan", "lightgoldenrodyellow",
    "lightgray", "lightsalmon", "lightseagreen",
    "lightskyblue", "lightslategray", "lightsteelblue",
    "lightyellow", "limegreen", "linen",
    "mediumaquamarine", "mediumorchid",
    "mediumpurple", "mediumseagreen",
    "mediumslateblue", "mediumspringgreen",
    "mediumturquoise", "mediumvioletred",
    "mintcream", "mistyrose", "moccasin",
    "navajowhite", "oldlace", "olivedrab",
    "orangered", "palegoldenrod", "palegreen",
    "paleturquoise", "palevioletred",
    "papayawhip", "peachpuff", "peru",
    "powderblue", "rosybrown", "royalblue",
    "saddlebrown", "seagreen", "seashell",
    "sienna", "silver", "slateblue",
    "slategray", "snow", "springgreen",
    "steelblue", "tan", "thistle",
    "wheat", "whitesmoke", "yellowgreen"
]



#==============================================================
class Snake:
    def __init__(self, chosen_color):
        global CHOSEN_COLOR_SET
        #____________
        #default values
        # self.snake_color = "white"
        self.modified_turn = None
        self.TURN_DIRECTION = 0  #DON'T YOU EVER MAKE IT "none" you need it to be int or float!!
        self.SNAKE_HEAD_Direction = None
        self.picked_color = False
        ############
        for colors in colors_extended:
            if chosen_color in colors_extended:
                self.snake_color = chosen_color
                self.picked_color = True
                #XXXXX
                CHOSEN_COLOR_SET = self.snake_color
                break
            ############
            elif chosen_color == "" and self.picked_color == False:
                self.snake_color = "white"
                #XXXXX
                CHOSEN_COLOR_SET = self.snake_color
                break

        #___________Body:
        #default body parts HEAD / BELLY / TAIL
        snake_HEAD = Turtle()
        snake_part1 = Turtle()
        snake_part2 = Turtle()
        ###############
        self.snake_body = [snake_HEAD, snake_part1, snake_part2]
        ###############
        #default setup:
        for parts in self.snake_body:
            parts.penup()
            parts.shape("square")
            parts.color(self.snake_color)
            # parts.shapesize(2) #NEW UPDATE

        #Most important part of the SNUCC, I mean snake:
        #BUT you need to confirm this HEAD being accessable to every part/method across this class by using .self for it and confirm it's place
        self.snake_HEAD = self.snake_body[0]

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++ROTATIONS:
    def turning_right(self):
        if self.SNAKE_HEAD_Direction != "LEFT":
            self.TURN_DIRECTION = 0
            self.snake_HEAD.setheading(self.TURN_DIRECTION)
            #___#
            self.SNAKE_HEAD_Direction = "RIGHT"
            #___#
            print(self.TURN_DIRECTION)  # DEBUG

    def turning_up(self):
        if self.SNAKE_HEAD_Direction != "DOWN":
            self.TURN_DIRECTION = 90
            self.snake_HEAD.setheading(self.TURN_DIRECTION)
            #___#
            self.SNAKE_HEAD_Direction = "UP"
            #___#
            print(self.TURN_DIRECTION)  # DEBUG

    def turning_left(self):
        if self.SNAKE_HEAD_Direction != "RIGHT":
            self.TURN_DIRECTION = 180
            self.snake_HEAD.setheading(self.TURN_DIRECTION)
            #___#
            self.SNAKE_HEAD_Direction = "LEFT"
            #___#
            print(self.TURN_DIRECTION)  # DEBUG

    def turning_down(self):
        if self.SNAKE_HEAD_Direction != "UP":
            self.TURN_DIRECTION = 270
            self.snake_HEAD.setheading(self.TURN_DIRECTION)
            #___#
            self.SNAKE_HEAD_Direction = "DOWN"
            #___#
            print(self.TURN_DIRECTION)  # DEBUG


    #========================================================
    # snake_HEAD.pos() -----> this is the spear-heading part ofc (for now it's location is 0,0)
    def move(self):

        ####################################################
        for seg_num in range(len(self.snake_body) -1 , 0, -1):  #the reason for "" len(snake_body) -1""
            #____________
            new_x = self.snake_body[seg_num - 1].xcor()                      #because the head is movable by the player
            new_y = self.snake_body[seg_num - 1].ycor()                      #and we don't want to move it
            self.snake_body[seg_num].goto(new_x, new_y)                      #we move the tail segments first, so it can have a
            #____________                                                              #refereance to follow


        # _____________________Turning_Check:
        #AND AFTER THE FOR-LOOP IS DONE now the head can move forward
        #so...
        self.snake_HEAD.setheading(self.TURN_DIRECTION)
        self.snake_HEAD.forward(20) #"20 because it's the dimensions of each segment"


    # ========================================================
    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color(self.snake_color)
        # new_seg.shapesize(2) #NEW UPDATE
        new_seg.goto(position)
        #
        self.snake_body.append(new_seg)

    # ========================================================V3 Update:
    def re_create_snake(self):
        global CHOSEN_COLOR_SET
        chosen_color = CHOSEN_COLOR_SET
        #------------------
        self.modified_turn = None
        self.TURN_DIRECTION = 0  # DON'T YOU EVER MAKE IT "none" you need it to be int or float!!
        self.SNAKE_HEAD_Direction = None
        self.picked_color = False
        ############
        if chosen_color == "white" or chosen_color == "blue" or chosen_color == "red" or chosen_color == "green" or chosen_color == "purple" or chosen_color == "yellow" or chosen_color == "pink":
            self.snake_color = chosen_color
            self.picked_color = True
        ############
        elif chosen_color == "" and self.picked_color == False:
            self.snake_color = "white"

        # ___________Body:
        # default body parts HEAD / BELLY / TAIL
        snake_HEAD = Turtle()
        snake_part1 = Turtle()
        snake_part2 = Turtle()
        ###############
        self.snake_body = [snake_HEAD, snake_part1, snake_part2]
        ###############
        # default setup:
        for parts in self.snake_body:
            parts.penup()
            parts.shape("square")
            parts.color(self.snake_color)
            # parts.shapesize(2) #NEW UPDATE
        #---------------
        self.snake_HEAD = self.snake_body[0]

    #___________________________________________-
    def reset(self):
        for seg in self.snake_body:
            seg.goto(900,900)
            seg.hideturtle()
        #---------------
        #clear all snake Segments
        self.snake_body.clear()
        self.re_create_snake()
        self.snake_HEAD = self.snake_body[0] #JUST MAKING SURE ;)

    # ===========================================================
    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())
