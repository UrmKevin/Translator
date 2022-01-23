from module1 import *

rus_list=[]
eng_list=[]
rus_list=loe_failist("rus.txt",rus_list)
eng_list=loe_failist("eng.txt",eng_list)

while 1:
    menu=input("\nRääkida -R,\nKõik sõnad -S,\nTõlgida -T,\nUus sõna -U,\nViga -V,\nKontroll -K,\nLõpp -L\n--> ")
    if menu.upper()=="U":
        rus_list=uus_sona("rus.txt",input("Новое слово: "))
        eng_list=uus_sona("eng.txt",input("New word: "))

    elif menu.upper()=="S":
        print(rus_list)
        print(eng_list)

    elif menu.upper()=="T":
        tolkimine(rus_list,eng_list)

    elif menu.upper()=="V":
        viga(rus_list,eng_list,"rus.txt","eng.txt")

    elif menu.upper()=="R":
        keel=input("Mis keeles ütelda?")
        sona=input("Sõna: ")
        heli(sona,keel)

    elif menu.upper()=="L":
        break

    elif menu.upper()=="K":
        kontroll(rus_list,eng_list)

    else:
        break

