from afvlakking import *

totalen = []

with open('invoer.txt') as invoer:
    eerste_getal = int(invoer.readline().strip())
    for i in range(eerste_getal):
        nieuwe_regel = invoer.readline().strip()
        getallen = [int(x) for x in nieuwe_regel.split()]
        totalen.append(aantal_vakjes(getallen[1:]))

with open("uitvoer.txt", "w") as uitvoer:
    for i in range(len(totalen)):
        uitvoer.write(f'{str(i)} {str(totalen[i])}')