import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.player_sprite = None
    
    def setup(self):
        self.player_sprite = arcade.Sprite("player.png", scale=0.1)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
    
    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
    def update(self, delta_time):
        self.player_sprite.update()

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
