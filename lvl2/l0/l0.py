import arcade

WIDTH = 800
HEIGHT = 600
class Ball(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__("ball.png", 0.1,center_x=center_x, center_y=center_y)
        self.change_x=5
        self.change_y=2

class Game(arcade.Window):
    def __init__(self):

        super().__init__(WIDTH, HEIGHT, "Ping pong")
        self.ball=Ball(WIDTH/2, HEIGHT/2)
    def on_draw(self):
        self.clear((255,0,0))
        self.ball.draw()
    def update(self, delta_time: float):
        self.ball.update()


window=Game()
arcade.run()