import turtle

bob = turtle.Turtle()
#保留窗口，直到我关闭
#turtle.mainloop()
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)#左转90度

def polygon(t, n, length):
 angle = 360 / n
 for i in range(n):
    t.fd(length)
    t.lt(angle)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


square(bob)
turtle.circle(100)
polygon(bob, 7, 70)
draw(bob, 10, 5)
turtle.mainloop()