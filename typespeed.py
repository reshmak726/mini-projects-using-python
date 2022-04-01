from os import times
from time import *
import random as r
def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except :
            error=error+1
    return error

def speedtime(timestart,timeend,userinput):
    timedelay = timeend - timestart 
    time_R = round(timedelay,2)
    speed = len(userinput)/time_R
    return round(speed)
while True:
    ck = input("ready to test: yes/no ")
    if ck=="yes":

        test = ["hello my names is typo and i am very fast in typing are you also fast in same...","we are from mumbai,india","welcome to india you guyzz"]

        test1=r.choice(test)
        print("********typing speed*********")
        print(test1)
        print()
        print()
        time1=time()
        testinput=input(" Enter : ")
        time2=time()

        print('speed : ' ,speedtime(time1,time2,testinput)," w/sec")
        print("error : " ,mistake(test1,testinput))

    elif ck=="no":
        print("thank you")
        break

    else:
        print("wrong input ")
