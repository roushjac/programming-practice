import turtle

def draw_square(a_turtle):
    for a in range(4):
        a_turtle.forward(100)
        a_turtle.right(90)


def draw_circle_with_squares():
    window=turtle.Screen()

    brad = turtle.Turtle()
    brad.speed(100)
    
    num_of_squares = 30
    for square_num in range(1, num_of_squares+1):
        draw_square(brad)
        brad.right(360/num_of_squares)
    window.exitonclick()

draw_circle_with_squares()
