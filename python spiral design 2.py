import turtle
myPen = turtle.Pen()
turtle.bgcolor("black")
myPen.color("orange")
myPen.speed(-300)

side = 1

for i in range(450):
    myPen.forward(side)
    myPen.right(122)
    myPen.width(i/100 +1)
    side += 5

turtle.listen()
turtle.mainloop()
