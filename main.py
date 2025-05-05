import turtle
import colorsys

loop_1 = 25
loop_2 = 15
circle_radius = 50

turtle.speed(0)
turtle.bgcolor("black")
turtle.width(2)
turtle.setup((circle_radius + 282.84) * 2, (circle_radius + 282.84) * 2)
turtle.sety(-circle_radius)

for i in range(loop_1):
  for j in range(loop_2):
    turtle.color(colorsys.hsv_to_rgb(j/loop_2, i/loop_1, 1):
    turtle.right(90)
    turtle.circle(200-i*4, 90)
    turtle.left(90)
    turtle.circle(200-i*4, 90)
    turtle.left(180)
    turtle.circle(circle_radius, 360 / loop_2)

turtle.ht()
turtle.exitonclick()
