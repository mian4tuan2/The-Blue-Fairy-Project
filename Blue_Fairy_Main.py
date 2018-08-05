#print("Hello, World!")
#print("I can use this as an editor please!")
#                  This is my First Game, The Blue Fairy Project's Main File. You are welcome to try your hand at this text-based adventure game.
#
#                                                      -FlareStormGaming, Github
import sys
quit = False
while not quit:
    print("Enter a Command")
    x = input("--->")
    print("You entered '%s'" % x)
    if x == "quit":
        quit = True
    else:
        print("You are smart!")