import os
import turtle

def removePreviousFiles(directory, startWith):
    fileList = os.listdir(directory)
    for filename in fileList:
        if filename.startswith(startWith):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"Removed: {file_path}")

def drawBackground(bgColour, screenWidth, screenHeight):
    turtle.pencolor(bgColour)
    # Move to starting position
    turtle.penup()
    turtle.goto(-screenWidth/2 - 10, screenHeight/2 + 10)
    turtle.pendown()
    turtle.begin_fill()  # Start filling the shape
    for _ in range(2):
        turtle.forward(screenWidth + 10)
        turtle.right(90)
        turtle.forward(screenHeight + 10)
        turtle.right(90)
    turtle.end_fill()  # End filling the shape
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def openVideo(videoPath):
    try:
        os.system(f"open {videoPath}")
    except Exception as e:
        print(f"Error: {e}")

def frameCount(directory):
    png_count = 0
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            png_count += 1
    return png_count
        