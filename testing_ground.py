# class inheritance\\
# you can make a new class inherit the "Variables"-Attributes (features)
# and also the "Functions"-Methods (abilities and skills)
# from another class
# that you already worked on!!
#
# by just adding THE NAME OF THE PARENT-CLASS inside the parentheses "()" of the new class!!
#
# parent class\\  "parent = SUPER class"
# Class ParentClass:
# 	def __init__(self):
#
# -----------------------------NOW to inherit do this:
#
# child class\\   "child = SUB class"
# Class ChildClass(ParentClass):<----------------------added the parent class name inside () that's enough to inherit the FUNCTIONS
# 	def __init__(self):		    \                                                                       BUT.. it's better to use super().__init__
# 		super().__init__()        <------------------This line will be the DNA                                  to inherit the ATTRIBUTES!!!
# 							that they inherited from the parent!!!
#


#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
# EXAMPLE:
#############################################################################################
class Animal:
    def __init__(self):
        self.eyes = 2
        self.head = 1

    def breathing(self):
        print("inhale..\nexhale..")

#______________________________________________MAKING NEW CLASS:
class Fih(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("swimming noises")

#____________________________________________________________________________NOTE2:
# you can also pic a specific function to be "inherited" and add something on top of it! using the super(). function
#                                                                                                  ^^^^^^^^^^^^^^^^^
    def breath_underwater(self): #this breathing method is different..it's for FISH class not ANIMAL class..
                     #now
                     #it will inherit everything from the ANIMAL class BUT it will add 1 small thingy to that breathing function and it is:
        super().breathing()
        print("underwater")


#______________________________________________
#Creating Object from the NEW CLASS
A_silly_fish = Fih()
#
A_silly_fish.breathing()
print(f"{A_silly_fish.eyes}")
#
A_silly_fish.breath_underwater()



