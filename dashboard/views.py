from django.shortcuts import render
from .models import MorphSuit
import random

# Create your views here.
def dashboard(request):
    suitList = ["Red Suit", "Blue Suit", "Black Suit", "Pink Suit", "Yellow Suit", "White Suit", "Green Suit"]
    for i in range(7):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        morphSuit = MorphSuit(suit_name=suitList[i], suit_x=x, suit_y=y)
        morphSuit.save()

    context = {}
    return render(request, 'dashboard/index.html', context)

def gameLoop(request):
    p1 = random.randint(1, 6)
    p2 = random.randint(1, 6)
    p3 = random.randint(1, 6)
    p4 = random.randint(1, 6)
    p5 = random.randint(1, 6)
    p6 = random.randint(1, 6)
    p7 = random.randint(1, 6)
    avg = round((p1+p2+p3+p4+p5+p6+p7)/7)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p6)
    print(p7)
    print("-------")
    print(avg)
    context = {"p1": p1,
               "p2": p2,
               "p3": p3,
               "p4": p4,
               "p5": p5,
               "p6": p6,
               "p7": p7,
               "avg": avg}
    return render(request, 'dashboard/gameBoard.html', context)




