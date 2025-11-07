import turtle
win = turtle.Screen()
win.title("turtle paint brush")
win.bgcolor("lightgrey")
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
def go_up():
  t.setheading(90)
  t.fd(20)
def go_down():
  t.setheading(270)
  t.fd(20)
def go_left():
  t.setheading(180)
  t.fd(20)
def go_right():
  t.setheading(0)
  t.fd(20)
def increase_pen_size():
  t.pensize(t.pensize()+2)
def decrease_pen_size():
  t.pensize(t.pensize()-2)
def red():
  t.color("red")
def blue():
  t.color("blue")
def green():
  t.color("green")
def yellow():
  t.color("yellow")
def cyan():
  t.color("cyan")
def marineblue():
  t.color("#3b9ecf")
def clear_screen():
  t.clear()
win.listen()
win.onkey(go_up,"Up")
win.onkey(go_down,"Down")
win.onkey(go_left,"Left")
win.onkey(go_right,"Right")
win.onkey(red,"r")
win.onkey(blue,"b")
win.onkey(green,"g")
win.onkey(yellow,"y")
win.onkey(cyan,"c")
win.onkey(marineblue,"m")
win.onkey(clear_screen,"x")
win.onkey(increase_pen_size,"+")
win.onkey(decrease_pen_size,"-")
t.penup()
t.goto(-380,260)
t.t.write("Arrow keys = move| r = red| b = blue| g = green| y = yellow| c = cyan| m = marineblue| x = clear screen",font = ("Arial",12,"bold"))
goto(0,0)
t.pendown()
win.mainloop()
import pygame
import random
pygame.init()
width,height = 500,500
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("night sky")
running = True
while running:
   window.fill((0,0,0))
   for i in range(100):
     x = random.randint(0,width)
     y = random.randint(0,height)
     pygame.draw.circle(window,(255,255,255),(x,y),2)
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       running = False
   pygame.display.update()
pygame.quit()
