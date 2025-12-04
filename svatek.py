import turtle


screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Přání k svátku")

ramecek = turtle.Turtle()
ramecek.speed(4)
ramecek.pensize(5)
ramecek.color("darkgreen")

ramecek.penup()
ramecek.goto(-220, 160)
ramecek.pendown()

for _ in range(2):
    ramecek.forward(440)
    ramecek.right(90)
    ramecek.forward(320)
    ramecek.right(90)


text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 60)
text.color("darkblue")
text.write("Všechno nejlepší", align="center", font=("Arial", 28, "bold"))

text.goto(0, 20)
text.color("purple")
text.write("k svátku!", align="center", font=("Arial", 32, "bold"))


kvet = turtle.Turtle()
kvet.speed(3)
kvet.color("magenta")
kvet.pensize(3)

kvet.penup()
kvet.goto(0, -80)
kvet.pendown()

for _ in range(6):
    kvet.circle(40)
    kvet.left(60)

kvet.color("green")
kvet.right(90)
kvet.forward(120)


turtle.done()
