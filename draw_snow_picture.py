from turtle import *


def Koch(length):
    if length < 10:
        fd(length)
        return
    Koch(length/3)
    lt(60)
    Koch(length/3)
    rt(120)
    Koch(length/3)
    lt(60)
    Koch(length/3)

def snowflake(n):
    for i in range(3):
        Koch(n)
        rt(120)

if __name__ == '__main__':
    speed(0)
    up()
    goto(-100, 100)
    down()
    snowflake(500)
    ht()
    done()