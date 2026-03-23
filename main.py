#x--x--x--x--x--x--x--x--x#
from turtle import Screen
import time
from snake import Snake
#new:
from foodscript import Food1
from foodscript import Food2
#
from score_board import ScoreBoard
#x--x--x--x--x--x--x--x--x#



#PythonSnakeGame_V2 by Dr.M-Dev:
#                                                                                                                                                                                                                   ...::::.      ...::::::::    :.      .:.
#   5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?
#   G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B
#   G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.
#   7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!
#   Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P
#   P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B
#
#
#                                                              !J!:
#                                                               ^G@@&P7:
#                                          .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^
#                                     :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&
#                                 .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...
#                               ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@
#                             ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&
#                           7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J
#                         .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!
#                        :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P
#                       .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G
#                       #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J
#                      !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:
#                      B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G
#                      @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.
#                    .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^
#                    .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~
#                ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.
#             .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:
#           :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~
#         !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?
#      .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.
#      J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:
#       .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:
#         .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.
#            ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~
#              :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.
#                .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!
# ''')




print("******** WELCOME TO PythonSnakeGame_V2 - By: Dr.m DEV *********")
#================================================================================================
#================================================================================================
#==============================================================SETUP
#_________CREATED OBJECT
my_screen = Screen()
#
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.title("SnakeGame - Dr.M-Dev")
#__________Tracer
my_screen.tracer(0) #0 = off   1 = on  (typical 01 logic :)


#__________Forming a SNAKE-Class Object "instance":
user_color = my_screen.textinput(title="Choose A Color For Your Snack :>", prompt="Type here:\n⚠️if it's not available it will be set to default/white")
snake_obj = Snake(chosen_color=user_color)

#__________Forming a FOOD-Class Object:
food_obj = Food1()
food_obj2 = Food2()

#__________Counting the score!
score_screen_obj = ScoreBoard()
score_screen_obj.start_counting()

#__________Collision options
self_collision_isON = True
if self_collision_isON:
    self_collision_choice = my_screen.textinput(title="Pick difficulty", prompt="Do you want self-collision or not? :) [yes/no]").lower()
    if self_collision_choice == "no" or self_collision_choice == "n":
        self_collision_isON = False
    else:
        self_collision_isON = True


#==============================================================MOVEMENT/CONTROLS:
my_screen.listen()
my_screen.onkey(key="d" or "Right", fun=snake_obj.turning_right)
my_screen.onkey(key="w" or "Up", fun=snake_obj.turning_up)
my_screen.onkey(key="a" or "Left", fun=snake_obj.turning_left)
my_screen.onkey(key="s" or "Down", fun=snake_obj.turning_down)
#
my_screen.onkey(key="Right", fun=snake_obj.turning_right)
my_screen.onkey(key="Up", fun=snake_obj.turning_up)
my_screen.onkey(key="Left", fun=snake_obj.turning_left)
my_screen.onkey(key="Down", fun=snake_obj.turning_down)


#==============================================================GAME-OVER SEQUENCE
def game_over():
    score_screen_obj.game_over_screen()






#==============================================================MAIN CODE START HERE:
game_is_on = True

while game_is_on:
    # Updating the tracer:
    my_screen.update()
    time.sleep(0.1)
    #__________________________Movement:
    ##########
    snake_obj.move()
    ##########
    #==============================================================Food collision:
    if score_screen_obj.score % 5 == 0:
        ######################
        food_obj2.spawn_f2 = True
        food_obj2.location_refresh_f2()
    else:
        food_obj2.remove_food2()
    #
    #---------------------------------
    if snake_obj.snake_HEAD.distance(food_obj) < 15:
        ######################
        # print("nom nom nom") #DEBUG
        snake_obj.extend_snake()
        #
        food_obj.location_refresh()
        score_screen_obj.refresh_score(1)

    #---------------------------
    if snake_obj.snake_HEAD.distance(food_obj2) < 20:
        snake_obj.extend_snake()
        snake_obj.extend_snake()
        #
        food_obj2.location_refresh_f2()
        score_screen_obj.refresh_score(2)


    #==============================================================Walls collision:
    #V3-UPDATE
    if snake_obj.snake_HEAD.xcor() > 290 or snake_obj.snake_HEAD.xcor() < -300 or snake_obj.snake_HEAD.ycor() > 300 or snake_obj.snake_HEAD.ycor() < -295:
    #     game_is_on = False
    #     game_over()
        #________________________
        score_screen_obj.reset_score()
        snake_obj.reset()

    #==============================================================Self-Collision
    # V3-UPDATE
    for seg_collider in snake_obj.snake_body[1:]:
        if snake_obj.snake_HEAD.distance(seg_collider) < 15 and self_collision_isON == True:
            # print("OUCH!!") #DEBUG
            # game_is_on = False
            # game_over()
            # ________________________
            score_screen_obj.reset_score()
            snake_obj.reset()




#==============================================================
my_screen.exitonclick()
