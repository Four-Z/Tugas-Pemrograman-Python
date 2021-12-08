import turtle
import time
from PIL import Image

t = turtle.Turtle()

digits = ['0111011', '0110011', '0011001', '0011011', '0111001', '0111101']
digits2 =['1110010', '1110010', '1100110', '1101100', '1110010', '1101100']

t.right(90)
t.width(3)
temp = 0
t.goto(temp, 0)

for i in range(2):
    t.pendown()
    t.forward(170)
    t.penup()
    if i-1 != 0:
        temp += 5
    t.goto(temp, 0)

for digit in digits:
    for i in digit:
        if i == "1":
            temp += 3
            t.goto(temp, 0)
            t.pendown()
            t.forward(150)
            t.penup()
        else:
            temp += 3

for i in range(2):
    temp += 5
    t.goto(temp, 0)
    t.pendown()
    t.forward(170)
    t.penup()

temp += 3
for digit in digits2:
    for i in digit:
        if i == "1":
            temp += 3
            t.goto(temp, 0)
            t.pendown()
            t.forward(150)
            t.penup()
        else:
            temp += 3

for i in range(2):
    t.goto(temp, 0)
    t.pendown()
    t.forward(170)
    t.penup()
    temp += 5

ts = t.getscreen()
canvas = ts.getcanvas()
canvas.postscript(file="turtle.eps")

img = Image.open("turtle.eps")
img.save("Barcode/turtle.jpg")

time.sleep(10)
