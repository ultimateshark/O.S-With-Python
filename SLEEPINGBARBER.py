import threading
from threading import Thread



class semz():
    sem=0
    def wait(self):
        while self.sem<=0:
            pass
        self.sem=self.sem-1
        return self.sem
    def signal(self):
        self.sem=self.sem+1
        return self.sem
class semo():
    sem=1
    def wait(self):
        while self.sem<=0:
            pass
        self.sem=self.sem-1
        return self.sem
    def signal(self):
        self.sem=self.sem+1
        return self.sem
cust=semz()
barb=semz()
seat=semo()
class free():
    free=5
free=free()

def barber():
    while True:
        try:
            cust.wait()
            seat.wait()
            free.free+=1
            barb.signal()
            seat.signal()
            print("barber code")
        except KeyboardInterrupt:
            break


def customer():
    while True:
        try:
            seat.wait()
            if free.free>0:
                free.free=free.free-1
                cust.signal()
                seat.signal()
                barb.wait()
                print("cust code")
            else:
                seat.signal()
                print("cust code")
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    print("start")
    Thread(target = barber).start()
    Thread(target = customer).start()
    print("end")
