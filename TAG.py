def dead():
    print("Sorry, you died and can never return home. :(")
    exit(0)


def invalid():
    print("That isn't an option! Try again!")

yes_or_no = ["yes", "no"]
directions = ["left", "right", "forward",]


# start with introduction
print("You've been magically transported to the World of Oz." )
print("You must find the ruby shoes to return home but if you die you're stuck in this world forever")
print("You walk along the golden brick road and see that it divides into two paths.")
print("The path on the left looks dark, gloomy, and worn down. ")
print("The right one is less worn but nicer.")
#road = int(input("Enter left for the worn down path or 2 for the nicer path: "))


response = ""
while response not in directions:
    response = input("Do you choose the left path or the right path?")
#what happens when each path is chosen
#trying to fix bc it always goes to the option of left
    print("You head down the left path, you end up tripping and hitting your head on a rock.")
    print("You head down the right path, you make it to the other side and see a scarecrow.")
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
