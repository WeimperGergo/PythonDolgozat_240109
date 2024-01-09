import random


def dollar():
    print("II/A, B, C:", end="\n\t")
    rndLista = []
    for i in range(11):
        rnd = random.randint(-100, 1024)
        rndLista.append(rnd)
        print(rnd, end="$")
    rnd = random.randint(-100, 1024)
    rndLista.append(rnd)
    print(rnd)
    return rndLista


def otteloszthatoak_szama(lista):
    print("II/D, E:", end="\n\t")
    i = 0
    oszthato5 = 0
    while i < len(lista):
        if (lista[i] % 5) == 0:
            oszthato5 += 1
        i += 1
    return oszthato5


def konzolra_ir(szam):
    return f"Az 5-el oszthatóak száma: {szam}"


def fajlba_ir(szam):
    fajlba = open("kimutatas.txt", "w", encoding="utf-8")
    fajlba.write(f"II/F:\n\tAz 5-el oszthatóak száma: {szam}")
    fajlba.close()
