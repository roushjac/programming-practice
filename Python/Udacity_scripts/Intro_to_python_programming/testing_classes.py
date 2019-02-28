import turtle

class Shape():
    def __init__(self, name):
        self.name = name

    def draw(self):
        point = turtle.Turtle()
        if self.name == 'square':
            for a in range(4):
                point.forward(100)
                point.right(90)
        elif self.name == 'circle':
            point.circle(100)
        else:
            print('enter a valid shape')

brad = Shape(input('enter a shape - square or circle: '))

brad.draw()
            
