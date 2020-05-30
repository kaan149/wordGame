import time
import sys
game_is_still_going = True

try:
    # FIRST FILE ADJUSTMENTS TO CREATE PROPER DICTIONARY FOR OUR GAME!!! "MATCHES"
    file = open(sys.argv[1], "r", encoding="utf-8")
    correct_words = file.read()
    adjustment = []
    source = []
    keys = []
    values = []
    real_values = []
    game_source = {}

    for i in correct_words.split("\n"):
        adjustment.append(i)

    for j in range(len(adjustment)):

        for k in adjustment[j].split(":"):
            source.append(k)

    for z in range(len(source)):

        if z % 2 == 0:
            keys.append(source[z])
        else:
            values.append(source[z])

    for i in values:
        i = str(i)
        a = i.split(",")
        real_values.append(a)

    for i in range(len(keys)):
        game_source[keys[i]] = real_values[i]

    # SECOND FILE ADJUSTMENTS TO CREATE PROPER DICTIONARY FOR OUR GAME!!! "SCORING"

    file2 = open(sys.argv[2], "r", encoding="utf-8")
    letter_values = file2.read()
    adj2 = []
    source2 = []
    keys2 = []
    values2 = []
    points = {}

    for i in letter_values.split("\n"):
        adj2.append(i)

    for j in range(len(adj2)):

        for k in adj2[j].split(":"):
            source2.append(k)

    for z in range(len(source2)):

        if z % 2 == 0:
            keys2.append(source2[z])
        else:
            values2.append(source2[z])

    for i in range(len(keys2)):
        points[keys2[i]] = values2[i]

except IndexError:
    game_is_still_going = False
    print("You must write two arguments for this program")


def game_control():
    while game_is_still_going == True:

        for i in game_source:
            global score
            score = 0
            print("Shuffled letters are {}. Please guess words for these letters with minimum three letters".format(i))
            now = time.time()
            inputs = []

            while time.time() - now < 30:

                global x
                x = input("Guessed Word:")
                x = x.replace("i,ı", "İ,I").upper()

                if x.replace("İ,I", "i,ı").lower() in inputs:

                    print("This word is guessed before")
                    if 30 - int(time.time() - now) >= 0:
                        print("You have {} time".format(30 - int(time.time() - now)))
                    else:
                        print("Time's up")

                elif x in game_source[i]:

                    points_calculator()
                    inputs.append(x.replace("İ,I", "i,ı").lower())

                    if 30 - int(time.time() - now) >= 0:
                        print("You have {} time".format(30 - int(time.time() - now)))
                    else:
                        print("Time's up")

                else:
                    print("Your guessed word is not a valid word")
                    if 30 - int(time.time() - now) >= 0:
                        print("You have {} time".format(30 - int(time.time() - now)))
                    else:
                        print("Time's up")

            print("Score for {} is {} and guessed words are ".format(i, score), *inputs, sep="-")


def points_calculator():
    global score
    local_score = 0

    for i in x:
        value = points[i]
        value = int(value)
        local_score += value
    a = local_score * len(x)
    score += a

game_control()
