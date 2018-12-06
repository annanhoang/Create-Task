# start with introduction
print("You've been magically transported to the World of Oz. " )
print("You must find the ruby shoes to return home but you only have 100 HP, if you reach 0 you lose. ")
print("You walk along the golden brick road and see that it divides into two paths.")
print("One path looks dark, gloomy, and worn down. ")
print("The other is less worn but nicer.")
road = int(input("Enter 1 for the worn down path or 2 for the nicer path: "))
# def road():
#     input(("Enter 1 for the worn down path or 2 for the nicer path: "))

#what happens when each path is chosen
if road == "1":
    print("As you walk along the path you trip on the uneven bricks and you lose 5 HP, "
          "but you get back up and keep walking.")
# elif road == 2:
else:
    print("As you walk through the path something red and shiny catches your eye in the shadows.")
    print(str(input("Enter 1 to check what it is or enter 2 to ignore: ")))
    if input == "1":
        print("You find out it's a red snake and it bites you!")
        HP = "90"
        print("Your HP is now 90")
    else:
        print ("You keep going forward but as you walk away you look back "
               "and avoided the poisonous.")
#having problems figuring out how to ask the question again if entered invalid response

def dead():
    print("Sorry, you died and can never return home. :(")
    exit(0)