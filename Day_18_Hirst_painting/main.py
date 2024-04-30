#TODO 1: Use the colorgram to extract a list of RGB-tuples
# import colorgram
#
# colors = colorgram.extract("image.jpg.jpg", 1000)
# color_palette = []
#
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.r
#     new_color = (r, g, b)
#     color_palette.append(new_color)
#
# print(color_palette)

color_list = [(219, 153, 219), (133, 171, 133), (222, 72, 222), (215, 131, 215), (24, 119, 24), (241, 208, 241),
              (121, 177, 121),  (38, 119, 38), (20, 165, 20), (219, 83, 219), (140, 86, 140), (131, 83, 131),
              (175, 185, 175), (21, 168, 21),  (161, 209, 161), (174, 154, 174), (3, 96, 3), (237, 161, 237),
              (238, 166, 238), (54, 59, 54), (152, 207, 152),  (102, 126, 102), (40, 56, 40), (34, 87, 34),
              (232, 209, 232), (74, 79, 74), (44, 70, 44)]

# TODO 2: Create a spot painting using this color lists. Requirements:
import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("triangle")
tim.speed("fastest")
t.colormode(255)
tim.penup()

#1) 10x10 rows of spots,
for i in range(10):
    tim.setpos(-225, -200 + 50 * i)
    for _ in range(10):

#2) dots 20 in size
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()

#3) 50 paces apart
        tim.forward(50)

screen = Screen()
screen.exitonclick()

#Why is my color_list only using a few select colors?