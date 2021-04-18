import math
from turtle import *
from listClass import mylist


rotace = (math.sqrt(5)+1)/2  # float(input())
listy = int(20000)  # int(input())
distancek = float(0.1)  # float(input())
const = math.pi * 2 * rotace
rotace -= math.floor(rotace)
if rotace > 0.5:
    rotace -= 1
rotacek = math.ceil(1/rotace)


def list(iter):
    offset = iter * distancek
    offrot = iter * const - math.floor(iter/rotacek)*2*math.pi
    setpos(offset * math.cos(offrot), offset * math.sin(offrot))
    mylist()

def vykresli():
    tracer(1, 0)
    hideturtle()

    speed(0)
    penup()
    for i in range(listy):
        list(i)
        left(360 * rotace)
    done()


#########################
def main():
    vykresli()


if __name__ == "__main__":
    main()
