import json
import matplotlib.pyplot as plt
import numpy as np

def begin():
    var_players = input("How many players were there?\t:")
    print(var_players + " players...")

    print("Most recent map?\t*", end='')
    str_recentmap = input()
    print("Most recent map was :", str_recentmap + ".bsp")

    data = { #defining the data
        "playerCount":  var_players,
        "recentMap": str_recentmap
    }

    with open("out.json", "w") as f:
        json.dump(data, f, indent=4) # indent for pretty-printing

    print("JSON file generated!")

    user_input = input("Visualize player count data? (Y/N) ") # ask me for input

    if user_input == "Y": #if Y, generate the player count graph
        print("Visualizing player count data...")

        plt.hist(var_players, bins=30, edgecolor='black')

        plt.xlabel("Player Count")
        plt.ylabel("Number")
        plt.title("Number Of Players")

        plt.show()

    if user_input == "N": #if N, ask me for input again
        print("Aborting...")
begin()