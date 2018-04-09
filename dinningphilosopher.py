import threading
from threading import Thread

#wait and signal functions

def wait(sem):
    while chopstick[sem]<=0:
        pass
    chopstick[sem]=chopstick[sem]-1
    return chopstick[sem]

def signal(sem):
    chopstick[sem]=chopstick[sem]+1
    return chopstick[sem]
#main code


chopstick=[1]*5
def pro1():
    philos(1)
    print("first done")
    return "ok"
def pro2():
    philos(2)
    print("second done")
    return 2
def pro4():
    philos(4)
    print("fourth done")
    return 4
def philos(i):
    while True:
        wait(i)
        wait((i+1)%5)
        print("{0} is eating".format(i))
        signal(i)
        signal((i+1)%5)
        break
if __name__=="__main__":
    print("start")
    Thread(target = pro1).start()
    Thread(target = pro2).start()
    Thread(target = pro4).start()
    print("end")
