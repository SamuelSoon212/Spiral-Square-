from turtle import *

length = 5
depth = 0
speed(99999999)
pensize(2)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

while depth < 300:
    pencolor(colors[depth%7])
    depth += 1
    right(91)
    forward(length + depth*3)

mainloop()
