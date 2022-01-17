def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas


def eng_to_rus(e,r):
    word=input("Write your word - ")
    eng=loe_failist('Eng.txt')
    if word in eng:
        print(r[1])

