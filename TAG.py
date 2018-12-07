def dead():
    print("Sorry, you died and can never return home. :(")
    exit(0)


def invalid():
    print("That isn't an option! Try again!")



# start with introduction
print("You've been magically transported to the World of Oz." )
print("You must find the ruby shoes and help out some others in order to return home but if you die you're stuck in this world forever")
#road = int(input("Enter left for the worn down path or 2 for the nicer path: "))

def road():
    print("You walk along the golden brick road and see that it divides into two paths.")
    print("The path on the left looks dark, gloomy, and worn down. ")
    print("The right one is less worn but nicer.")
    response = input("Do you choose the left path or the right path? ")
#what happens when each path is chosen
#trying to fix bc it always goes to the option of left
    if response == "left" or response == "Left":
        print("You trip on a rock and hit your head.")
        dead()
    elif response == "right" or response == "Right":
        print("You make it to the other side and see a field of corn.")
    else:
        invalid()
        road()
road()

def scarecrow_brain():
    print("As you walk through the field you see a tall shadow.")
    print("It comes towards you and you see a large scarecrow!")
    print("He kindly asks you to help him find a brain and you say yes!")
    print("In order to find his brain you must go to the center of the maze.")
    print("You keep heading forward and hit a wall, the only way to go is right.")
    print("You go straight, it divides into a path on the left and right")
    response = input("Left or right? ")
    if response == "right" or response == "Right":
        print("The right path leads to a dead end! You head back and go left instead.")
    else:
        print("You keep heading down the left path until you hit a dead and turn right.")
        print("This way leads to another diversion, left or right? ")
        if response == "left" or response == "Left":
            print("You hit a dead end and head back the other way.")
        elif response == "right" or response == "Right":
            response = input("You keep walking and turn with the corner. "
                  "As you keep walking you can either turn right or go forward. ")
            if response == "right" or "Right":
                print("You walk down the right path and follow the only turns until you see a huge sqare area with a chest!")
                print("You open the chest and find the scarecrow's brain in a jar!")
                print("You give it back to him and he promises to help you find your ruby shoes.")
            else:
                return 0







# if response == "left" or "Left":
#     print("As you walk along the path you trip on the uneven bricks")
#     dead()
# elif road() == "right" or "Right":
#     print("As you walk through the path something red and shiny catches your eye in the shadows.")
#     print(str(input("Do you want to check what it is? Yes or no?")))
#     if input == "Yes" or "yes":
#         print("You find out it's a red snake and it bites you!")
#         dead()
#     else:
#         print ("You keep going down the path. You avoided the poisonous snake!")
# else:
#     invalid()
#     road()
#having problems figuring out how to ask the question again if entered invalid response
