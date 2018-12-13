import time


def dead():
    print("Sorry! Looks like you're stuck forever. :(")
    exit(0)


def invalid():
    print("That isn't an option! Try again!")


# start with introduction
def intro():
    print("You've been magically transported to the World of Oz.")
    time.sleep(1)
    print("You must find the ruby shoes and remember to be kind "
          "in order to return home but if you die you're stuck in this world forever")
    time.sleep(1)

# road = int(input("Enter left for the worn down path or 2 for the nicer path: "))


def road():
    print("You walk along the yellow brick road and see that it divides into two paths.")
    time.sleep(1)
    print("The path on the left looks dark, gloomy, and worn down. ")
    time.sleep(1)
    print("The right one is less worn but nicer.")
    time.sleep(1)
    response = input("Do you choose the left path or the right path? ")
    time.sleep(1)
    # what happens when each path is chosen
    # trying to fix bc it always goes to the option of left
    if response == "left" or response == "Left":
        print("You trip on a rock and hit your head.")
        time.sleep(1)
        dead()
    elif response == "right" or response == "Right":
        print("You make it to the other side and see a field of corn.")
        time.sleep(1)
    else:
        invalid()
        road()


def scarecrow_brain():
    print("As you walk through the field you see a tall shadow.")
    time.sleep(1)
    print("It comes towards you and you see a large scarecrow!")
    time.sleep(1)
    print("He kindly asks you to help him find a brain and you say yes!")
    time.sleep(1)
    print("In order to find his brain you must go to the center of the maze.")
    time.sleep(1)
    print("You keep heading forward and hit a wall, the only way to go is right.")
    time.sleep(1)
    print("You go right, it divides into a path on the left and right")
    time.sleep(1)
    response = input("Left or right? ")
    time.sleep(1)
    if response == "right" or response == "Right":
        print("The right path leads to a dead end! You head back and go left instead.")
        time.sleep(1)
    else:
        print("You keep heading down the left path until you hit a dead and turn right.")
        time.sleep(1)
        response = input("This way leads to another diversion, left or right? ")
        time.sleep(1)
        if response == "left" or response == "Left":
            print("You hit a dead end and head back the other way.")
            time.sleep(1)
            print("You walk down the right path "
                  "and follow the only turns until you see a huge square area with a chest!")
            time.sleep(1)
            print("You open the chest and find the scarecrow's brain in a jar!")
            time.sleep(1)
            print("You give it back to him and he promises to help you find your ruby shoes.")
            time.sleep(1)
        elif response == "right" or response == "Right":
            response = input("You keep walking and turn with the corner. "
                             "As you keep walking you can either turn right or go forward. ")
            time.sleep(1)
            if response == "right" or "Right":
                print("You walk down the right path "
                      "and follow the only turns until you see a huge square area with a chest!")
                time.sleep(1)
                print("You open the chest and find the scarecrow's brain in a jar!")
                time.sleep(1)
                print("You give it back to him and he promises to help you find your ruby shoes.")
                time.sleep(1)
            else:
                print("You hit a dead end go back the other way and find a chest!")
                time.sleep(1)
                print("You open the chest and find the scarecrow's brain in a jar!")
                time.sleep(1)
                print("You give it back to him and he promises to help you find your ruby shoes.")
                time.sleep(1)


def tin_man_heart():
    # made cave a function inside the function in order to restate prompt of entering cave
    def cave():
        print("You all head into the cave and see written in the wall '1902'")
        time.sleep(1)
        print("As you wind through the narrow walls of the cave it leads into a big room with a waterfall!")
        time.sleep(1)
        print("You see a chest similar to the one the Scarecrow had but this one has a lock!")
        time.sleep(1)
        lock()

    # made lock a function in order to restate asking password if incorrect
    def lock():
        password = 1902
        password_response = input("What is the password to open the chest? ")
        if password_response == password:
            print("You hear a click and the chest opens to a glowing heart!")
            print("You give it back to the Tin Man, he thanks you and agrees to help you get home!")
        else:
            print("Wrong password! Try again!")
            lock()
        # introducing puzzle

    print("You and the Scarecrow keep following the yellow brick road "
          "and see a Tin Man sitting on a bench and oil besides him. ")
    print("You use the oil to free him!")
    print("He asks you to help him find a heart and you agree!")
    print("You all keep walking along the road until you see a cave next to a forest. The cave is oddly glowing red.")
    response = input("Do you want to go in? ")
    if response == "yes" or response == "Yes":
        cave()
    else:
        print("Too bad, suck it up buttercup, you have to go in.")
        cave()


def lion_courage():
    # introducing puzzle for courage
    print("As you walk out of the cave and into the forest you meet a cowardly Lion!")
    print("He asks you to help him find his courage since he's scared of everything"
          "and you want to help him because he a cutie (not based on the movie, he NOT a cutie!")
    print("He tells you that flying monkeys stole his courage and hid it somewhere in the forest.")
    print("You all continue down the path until it diverges into 3.")

    # in order to restate prompt if invalid response
    def road_2():
        response = input("Do you want to go to the left, middle, or left?")
        if response == "left" or response == "Left":
            print("You ran into a flying monkey and it almost kills you! You run back.")
            road_2()
        elif response == "right" or response == "Right":
            print("You found his courage!")
            print("He's so grateful that he agrees to help you find the ruby shoes!")
            print("You now have a team of a smart Scarecrow, a kind Tin Man, and even a brave Lion to help you!")
        elif response == "middle" or response == "Middle":
            print("You ran into a flying monkey and it attacks you!")
            print("The Scarecrow is ripped apart, the Tin Man was crumpled, and the Lion ran away!")
            dead()
        else:
            invalid()
            road_2()

    road_2()


def ruby_shoes():
    # introducing castle and puzzle
    print("You all keep traveling on the yellow brick road and it takes you to an emerald castle "
          "where you meet Glinda the Good Witch of the North")
    print("She tells you that the ruby slippers are hidden inside the castle.")

    # separate function in order to restate it if invalid
    def castle_maze():
        response = input(("You see a grand staircase, do you want to go up or go to the dining room? "))
        if response == "up" or "Up":
            print("You make it upstairs to the library and there's an old wizard reading.")
            print("He tells you that he's been watching your adventure, he challenges you to complete a timed quiz "
                  "in order to win the ruby shoes for you to go home.")

            def quiz():
                response = input("Do you want to take it?")
                if response == "yes" or response == "Yes":
                    import time
                    start_time = time.time()
                    timer = 0
                    correct = "corn maze"


# easier to read and see order of game
def main():
    intro()
    road()
    scarecrow_brain()
    tin_man_heart()
    lion_courage()
    ruby_shoes()


main()



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
# having problems figuring out how to ask the question again if entered invalid response
