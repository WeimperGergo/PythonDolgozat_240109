import random


def italok():
    print("I/A, B:", end="\n\t")
    iKod = input("Ital kódja: ")
    iDb = int(input("\tDarabszáma: "))
    vanOszlop = False
    print("I/C:", end="\n\t")
    szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(0, len(szamok)):
        if iKod == "A" + str(szamok[i]):
            print("Kiadott ital: Fanta")
            vanOszlop = True
        elif iKod == "B" + str(szamok[i]):
            print("Kiadott ital: Lipton Ice Tea")
            vanOszlop = True
        elif iKod == "C" + str(szamok[i]):
            print("Kiadott ital: Sprite")
            vanOszlop = True
        elif iKod == "D" + str(szamok[i]):
            print("Kiadott ital: Víz")
            vanOszlop = True
        elif iKod == "H" + str(szamok[i]):
            print("Kiadott ital: Coca-cola")
            vanOszlop = True
    if not vanOszlop:
        print("Nincs ilyen oszlop")

    nyeroszam = random.randint(0, 10)
    print(f"\tNyerőszám: {nyeroszam} -> ", end="")
    if nyeroszam == 10:
        print("Ön nyert: Vendégünk az üdítőre!")
    else:
        print("Ma sajnos nem nyert ingyen üdítőt!")
