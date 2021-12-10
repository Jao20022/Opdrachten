
# This program practically runs indefinitely, since Python is rather slow reading through thousands of lines
# The program, however, works as it should, and an interrupted version of the result is steamgames.json
import json


def addGame(push):
    global gameFile
    with open(gameFile, "r") as loadFile:
        lst = json.load(loadFile)
        lst.append(push)

    with open(gameFile, "w") as writeFile:
        json.dump(lst, writeFile, indent=4)


gameFile = "steamgames.json"
with open("../../External Gits/project/data/steam.json", "r") as jsonFile:
    data = json.load(jsonFile)
    payload = data
    gameNum = 0
    for game in payload:
        gameNum += 1
        push = {
            "game": game["name"]
        }
        if game["name"] == "Counter-Strike" and gameNum > 2:
            print(f"All games have been added! The file had {gameNum} games saved.")
            break
        else:
            addGame(push)
            print(f"Added a game to the file. [{gameNum}]")

    print("Function completed.")
