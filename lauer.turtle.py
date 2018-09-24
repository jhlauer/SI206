from turtle import *
space = Screen()
julia = Turtle()
julia.speed(0) 
space.setup(650,700)

def drawArt():
    def draw_line(start_x, start_y, goto_x, goto_y, width, color):
        julia.pensize(width)
        julia.color(color)        #change color to black
        julia.penup()
        julia.goto(start_x, start_y)
        julia.pendown()
        julia.left(90)
        julia.goto(goto_x, goto_y)

    def draw_rectangle(x, y, width, height, direction, border_color, fill_color):
        julia.penup()               #move
        julia.goto(x, y)      #lower red left corner
        julia.pendown()             #end move
        
        julia.color(border_color)    #border color
        julia.pensize(8)     #change pen size to 8 px 
        julia.fillcolor(fill_color)  #fill color 
        julia.setheading(direction)       # point due north
        
        julia.begin_fill()
        for sides in [1,2,3,4]:     # repeat the indented lines 4 times
            if sides % 2 == 0:              #if even side
                julia.forward(width)             # move forward by width
                julia.right(90)                #turn right
            else:                           #if odd side
                julia.forward(height)     #move forward by height
                julia.right(90)        # turn right 
        julia.end_fill()
        

    def draw_Mondarianart():
        draw_rectangle(-150, -120, 300, 350, 0, "black", "white") #long white
        draw_rectangle(200, -225, 150, 175, 0, "black", "yellow") #small yellow
        draw_rectangle(-150, -120, 225, 225, 270, "black", "blue") #small blue
        draw_rectangle(-150, 130, 225, 250, 270, "black", "white") #white upper left corner 
        draw_line(-150, 130, -375, 130, 20, "black") 
        draw_rectangle(-150, -120, 800, 800, 90, "black", "red") #big red

    draw_Mondarianart()

    def draw_shape(num_sides, length, turn, color):
        for sides in range(num_sides):    # repeat x times
            julia.forward(length)         # move forward by x units
            julia.right(turn)

    def repeat_draw(num_repeats, offset, angle, num_sides, length, turn, color, pensize):
        julia.pensize(pensize)
        julia.color(color)
        for repeats in range(num_repeats):   # draw the pattern x times
            julia.forward(offset)                 # Offset shapes
            julia.right(angle)                   #turn each one 
            draw_shape(num_sides, length, turn, color)

    julia.penup()
    julia.goto(-100, -200)
    julia.pendown()

    repeat_draw(20, 20, 20, 5, 100, 72, "pink", 8)

    julia.penup()
    julia.goto(100, 100)
    julia.pendown()

    repeat_draw(20, 20, 20, 6, 100, 60, "green", 4)

    julia.penup()
    julia.goto(-200, 150)
    julia.pendown()

    julia.pensize(4)
    def stamp(shape, color, start_size, num, grow_by, angle):
        julia.shape(shape)
        julia.color(color)
        for size in range(start_size, num, grow_by):
            julia.stamp()
            julia.forward(size)
            julia.right(angle)

    stamp("square", "purple", 2, 40, 2, 24)
    stamp("circle", "orange", 2, 55, 2, 25)
    stamp("turtle", "blue", 2, 70, 2, 26)

drawArt()
space.exitonclick()