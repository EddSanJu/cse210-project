import arcade

from game.constants import *
from game.background import Background
from game.actor import Actor
from game.level import Level
from game.cast import Cast

# The Director is a inherited class of parent arcade.Window. This is because in the Arcade library, the Window class does act like the "director"
class Director(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME)

        self._cast = Cast()

        #variables to create the GUI elements
        self.gui_camera = None
        self.score = 0
        #

    def setup(self):
        self._background = Background('grass.png')

        self._level = Level('1.csv', self._cast)

        self._player = Actor('female_idle.png', [2, 3])

        self._key = Actor('keys.png',  [3, 3]) 

        #element to show the GUI
        self.gui_camera = arcade.Camera(self.width, self.height)
        self.score = 0
        #





    def on_draw(self):
        self._background.draw()

        self._player.draw()

        self._key.draw()

        self._level.draw()

        #GUI drawing
        self.gui_camera.use()
        game_text = f"Keys {self.score}"
        arcade.draw_text(
            game_text,
            10, #add margin to the left
            620, #add margin to the bottom 
            arcade.csscolor.WHITE,
            15 # font size
        )


    def on_key_press(self, key, modifiers):
        position = self._player.get_position()
        
        x = position.get_x()
        y = position.get_y()

        # Check if player is within the boundaries of the window
        if key == arcade.key.UP:
            if y <= 8:
                y = y + 1
        elif key == arcade.key.DOWN:
            if y >= 1:
                y = y - 1
        elif key == arcade.key.LEFT:
            if x >= 1:
                x = x - 1
        elif key == arcade.key.RIGHT:
            if x <= 13:
                x = x + 1

        # Check for player collision with any elements. If there is a collision, return to prevent the collision
        for actor in self._cast.get_actors('elements'):
            if x == actor.get_position().get_x() and y == actor.get_position().get_y():
                return

        position.set_x(x)

        position.set_y(y)