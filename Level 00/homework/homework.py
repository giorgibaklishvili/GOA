from turtle import *

speed(10)
width(7)



#drawing a square
forward(200)       
left(90) 
forward(200)       
left(90)
forward(200)
left(90)
forward(200)

#drawing a door


left(90)
forward(70)
color("green")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
color("black")



#drawing a roof


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("red")

# drawing a window
color("purple")
penup()
goto(70,115)
pendown()
left(120)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(25)
left(90)
forward(60)


exitonclick()