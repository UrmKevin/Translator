def loe_failist(f:str,l:list):
    """Info failist f listisse l
    """
    fail=open(f,'r',encoding="utf-8-sig")
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def failisse_salvestamine(f:str,l:list):
    """Loetelu salvestame failisse
    """
    fail=open(f,'w')
    for el in l:
        fail.write(el+'\n')
    fail.close()

def rida_salvestamine(f:str,rida:str):
    """Üks sõna või lause(rida) salvestame failisse
    :param str f: fail kuku salvestame
    :param str rida: 
    """
    fail=open(f,'a')
    fail.write(rida+'\n')
    fail.close()

def uus_sona(f:str,rida:str)->list:
    """Lisame uus sõna failisse ja listisse
    :param str f: Faili nimetus
    :param str rida: lisatav sõna
    """
    #l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
    #l=loe_failist(f)
    #return l

def correction(sona:str,l:list):
    for i in range(len(l)):
        if l[i]==sona:
            uus_sona=sona.replace(sona,input("Uus sõna"))
            l.insert(i,uus_sona)
            l.remove(sona)
    return l

#def failisse():

def tolkimine(l1:list,l2:list):
    """
    """
    sona=input("Mida tõlkida: ")
    if sona in l1:
        tolk=l2[l1.index(sõna)]
        print(sona+" - "+tolk)
    elif sona in l2:
        tolk=l1[l2.index(sona)]
        print(sona+" - "+tolk)
    else:
        print("Sõna puudub sõnastikus")

def viga(l1:list,l2:list,f1:str,f2:str):
    sona=input("Sõna veaga? ")
    if sona not in l1 and sona not in l2:
        print("Sõna puudub")
    else:
        if sona in l1:
            tolk=l2[l1.index(sona)]
            l1.remove(sona)
            l2.remove(tolk)
        if sona in l2:
            tolk=l1[l2.index(sona)]
            l1.remove(sona)
            l2.remove(tolk)
        l1.append(input("Введи новое слово: "))
        l2.append(input("Sisesta uus sõna: "))
        failisse_salvestamine(f1,l1)
        failisse_salvestamine(f2,l2)


import os
from random import *
from gtts import gTTS
from random import *

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")


def kontroll(l1,l2):
    s='1'
    while s=='1':
        a=choice(l1)
        sona=input('Translate '+a+'\n').lower()
        if sona in l2:
            if l2.index(sona)==l1.index(a):
                print('You were right!')
        else:
            print('You are wrong!')
        s=input('You want to continue? yes-1  no-0\n')
    return