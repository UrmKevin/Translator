from module1 import *

while 1:
    way=int(input("1 - Eng to Rus\n2 - Rus to Eng\n3 - end task\n"))
    if way==1:
        eng_to_rus('Eng.txt','Rus.txt')
        print("_____")
    elif way==2:
        print("rustoeng")
    elif way==3:
        break
