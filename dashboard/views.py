from django.shortcuts import render
from .models import MorphSuit, Movement, MoveForm, RangerTeam, Map
import random
import os


# Create your views here.
def dashboard(request):
    newGame()
    suitList = ["Red Suit", "Blue Suit", "Black Suit", "Pink Suit", "Yellow Suit", "White Suit", "Green Suit"]
    for i in range(7):
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        if x == 5 and y == 5:
            z = random.randint(1, 4)
            a = random.randint(1, 2)
            if a == 1:
                x += z
            else:
                x -= z
        if x == 1 and y == 9:
            z = random.randint(1, 4)
            y -= z

        morphSuit = MorphSuit(suit_name=suitList[i], suit_x=x, suit_y=y)
        morphSuit.save()

    buildMap()
    rangers = RangerTeam()
    rangers.save()

    context = {}
    return render(request, 'dashboard/index.html', context)


def gameLoop(request):
    form = MoveForm()
    p1 = random.randint(1, 6)
    p2 = random.randint(1, 6)
    p3 = random.randint(1, 6)
    p4 = random.randint(1, 6)
    p5 = random.randint(1, 6)
    p6 = random.randint(1, 6)
    p7 = random.randint(1, 6)
    avg = round((p1 + p2 + p3 + p4 + p5 + p6 + p7) / 7)
    area = terainType()
    numEnemy = encounter(avg)
    if numEnemy == '8':
        numEnemy = "GOLDAR"

    print("moved " + str(avg))

    context = {"p1": p1,
               "p2": p2,
               "p3": p3,
               "p4": p4,
               "p5": p5,
               "p6": p6,
               "p7": p7,
               "avg": avg,
               "area": area,
               'numEnemy': numEnemy,
               'form': form}

    if request.method == "POST":
        form = MoveForm(request.POST)
        if form.is_valid():
            ranger = RangerTeam.objects.all().first()
            updateMap(ranger.position_x, ranger.position_y, form.cleaned_data['mov_x'], form.cleaned_data['mov_y'])
            ranger.position_x = form.cleaned_data['mov_x']
            ranger.position_y = form.cleaned_data['mov_y']
            ranger.turn_count += 1
            ranger.save()
            print("turn " + str(ranger.turn_count))
            return render(request, 'dashboard/gameBoard.html', context)

    return render(request, 'dashboard/gameBoard.html', context)


def newGame():
    MorphSuit.objects.all().delete()
    RangerTeam.objects.all().delete()
    if os.path.exists("map.txt"):
        os.remove("map.txt")


def terainType():
    terain = ['field', 'city', 'alley', 'river', 'office building']
    terrainRoll = random.randint(0, 4)
    area = terain[terrainRoll]
    return area


def encounter(avg):
    enconterRoll = random.randint(1, 10)
    print("encounter roll " + str(enconterRoll))
    enemyRoll = random.randint(1, 8)
    print("enemy roll " + str(enemyRoll))

    ranger = RangerTeam.objects.all().first()
    if ranger.turn_count == 0:
        return 0
    if avg == 1:
        if enconterRoll == 1:
            print("encountered enemy")
            return str(enemyRoll)
        else:
            return "0"
    elif avg == 2:
        if enconterRoll <= 2:
            print("encountered enemy")
            return str(enemyRoll)
        else:
            return "0"
    elif avg == 3:
        if enconterRoll <= 3:
            print("encountered enemy")
            return str(enemyRoll)
        else:
            return "0"
    elif avg == 4:
        if enconterRoll <= 4:
            print("encountered enemy")
            return str(enemyRoll)
        else:
            return "0"
    elif avg == 5:
        if enconterRoll <= 5:
            print("encountered enemy")
            return str(enemyRoll)
        else:
            return "0"
    elif avg == 6:
        if enconterRoll <= 6:
            print("encountered enemy")
            return str(enemyRoll)
        else:
            return "0"


def buildMap():
    morphSuit = MorphSuit.objects.all()
    map = Map()
    newMap = []
    strMap = ""

    for i in range(82):
        newMap.append("O")

    newMap[73] = "P"
    newMap[41] = 'X'

    for suit in morphSuit:
        # print(suit.suit_name)
        # print(str(suit.suit_x) + "," +str(suit.suit_y))
        x = suit.suit_x + 9*(suit.suit_y-1)
        newMap[x] = 'R'

    for i in newMap:
        strMap += i

    # print("len map " + str(len(newMap)))
    j = 1
    while j < len(strMap):
        if j % 9 == 0:
            print(strMap[j])
        else:
            print(strMap[j], end=' ')
        j += 1

    map.drawMap = strMap
    map.save()

    f = open("map.txt", "a")
    f.write(strMap)
    f.close()


def updateMap(x1, y1, x2, y2):
    newMap = []
    strMap = ""
    print("update map")
    f = open("map.txt", "r")
    file = f.readlines()
    f.close()
    map = file[0]
    newMap[:] = map
    oldPos = x1 + 9*(y1-1)
    newPos = x2 + 9*(y2-1)
    newMap[oldPos] = "O"
    newMap[newPos] = "P"

    for i in newMap:
        strMap += i

    f = open("map.txt", "w")
    f.write(strMap)
    f.close()
