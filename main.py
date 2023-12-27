
import turtle

class ChristmasScene:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(800, 600)

        self.circle = turtle.Turtle()
        self.circle.shape('circle')
        self.circle.color('red')
        self.circle.speed('fastest')
        self.circle.up()

        self.square = turtle.Turtle()
        self.square.shape('turtle')
        self.square.color('green')
        self.square.speed('fastest')
        self.square.up()

    def draw_circle(self, x, y):
        self.circle.goto(x, y)
        self.circle.stamp()

    def draw_square(self, x, y):
        self.square.goto(x, y)
        self.square.stamp()

    def draw_christmas_tree(self):
        k = 0
        for i in range(1, 17):
            y = 30 * i
            for j in range(i - k):
                x = 30 * j
                self.draw_square(x, -y + 280)
                self.draw_square(-x, -y + 280)

            if i % 4 == 0:
                x = 30 * (j + 1)
                self.circle.color('red')
                self.draw_circle(-x, -y + 280)
                self.draw_circle(x, -y + 280)
                k += 2

            if i % 4 == 3:
                x = 30 * (j + 1)
                self.circle.color('yellow')
                self.draw_circle(-x, -y + 280)
                self.draw_circle(x, -y + 280)

        self.square.color('brown')
        for i in range(17, 20):
            y = 30 * i
            for j in range(3):
                x = 30 * j
                self.draw_square(x, -y + 280)
                self.draw_square(-x, -y + 280)

        turtle.exitonclick()

if __name__ == "__main__":
    christmas_scene = ChristmasScene()
    christmas_scene.draw_christmas_tree()
