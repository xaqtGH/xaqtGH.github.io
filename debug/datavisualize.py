import json

var_players = input("How many players were there?\t:")
print(var_players + " players...")

print("Most recent map?\t*", end='')
str_recentmap = input()
print("Most recent map was :", str_recentmap + ".bsp")

data = {
    "playerCount":  var_players,
    "recentMap" :   str_recentmap,
}


with open("out.json", "w") as f:
    json.dump(data, f, indent=4) # indent for pretty-printing

print("JSON file generated!")