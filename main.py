# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("Gritti.jpeg",38)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")

tim.pu()
tim.hideturtle()

color_list = [(239, 220, 198), (198, 157, 124), (240, 212, 222), (134, 166, 183), (193, 141, 157), (208, 232, 219),
              (208, 224, 235), (137, 177, 159), (216, 202, 143), (137, 91, 72), (141, 77, 94), (75, 106, 130),
              (184, 93, 111), (70, 122, 98), (190, 100, 87), (225, 171, 185), (230, 174, 163), (85, 152, 128),
              (148, 145, 83), (166, 207, 189), (78, 150, 162), (159, 205, 213), (113, 121, 156), (101, 44, 62),
              (182, 187, 211), (68, 37, 52), (68, 45, 32), (38, 46, 67), (51, 56, 95), (104, 47, 40), (34, 60, 45),
              (38, 80, 60), (75, 73, 38), (37, 76, 82)]

tim.setheading(225)
tim.fd(250)
tim.setheading(0)

number_of_dots = 101

for dot_count in range(1,number_of_dots):
    tim.dot(20,random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()