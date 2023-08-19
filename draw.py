import turtle
import loadImage
import colorsys
import math

def spiral(numOfLines, strokesPerFrame):
    for x in range(numOfLines):
        turtle.color(((x/numOfLines), (x/numOfLines), (x/numOfLines) ** 3))
        turtle.forward(x)
        turtle.right(98)
        x = x + 1
        if x % strokesPerFrame == 0:
            turtle.update()
            loadImage.save()
    return numOfLines//strokesPerFrame
            
def rainbow():
    t = turtle
    n = 36 
    h = 0 
    for i in range(460): 
        c = colorsys.hsv_to_rgb(h,1,0.9) 
        h+=1/n 
        t.color(c) 
        t.left(145) 
        if i % (math.floor((i ** 2)/1000)+1) == 0:
            turtle.update()
            loadImage.save()
        for j in range(5): 
            t.forward(300) 
            t.left(150)