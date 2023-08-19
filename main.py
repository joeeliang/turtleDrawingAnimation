import turtle
import utils
import draw
import video
import os

def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    turtle.tracer(0)
    turtle.hideturtle()
    # Clean up animation files
    utils.removePreviousFiles(directory,"animation")

    # Initialize Turtle graphics
    utils.drawBackground("black", 1000, 1000)

    # Draw the animation
    draw.rainbow()

    #turns the png into videos, with fps, and total frames.
    video.pngToVideo(directory, 10, utils.frameCount(directory))
    
    #removes png and eps files of frames
    utils.removePreviousFiles(directory,"animation")
    
    # Exit
    turtle.bye()

    utils.openVideo("output.mp4")


main()
