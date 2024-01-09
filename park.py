from Park_o import Park


def beolvas():
    lista = []

    fajlbol = open("park1.txt", "r", encoding="utf-8")
    fajlbol.readline()
    sorok = fajlbol.readlines()
    fajlbol.close()

    for i in range(0, len(sorok)):
        lista.append(Park(sorok[i]))

    return lista


def vizsgalt_evek(lista):
    vizsgaltDb = 0
    for i in range(0, len(lista)):
        vizsgaltDb += 1
    print("III/A, B:", end="\n\t")
    return f"A vizsgált évek száma: {vizsgaltDb} db"


def park_atlag(lista: list[Park]):
    print("III/C:", end="\n\t")
    evDb = 0
    parkok = 0
    for i in range(0, len(lista)):
        evDb += 1
        parkok += lista[i].helyTipus
    print(f"A 23 év alatt átlagos állatkert, vadaspark, kultúrpark száma: {round(parkok/evDb, 2)} db")


def legtobb_latogato(lista: list[Park]):
    print("III/D:")
    maxIndex = 0
    i = 1
    while i < len(lista):
        if lista[i].latogatas > lista[maxIndex].latogatas:
            maxIndex = i
        i += 1
    print(f"\tA legnagyobb látogatás szám: {int(lista[maxIndex].latogatas*1000)}, éve: {lista[maxIndex].ev}")

