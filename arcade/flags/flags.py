import arcade

PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        layer_options = {"Walls": {"use_spatial_hash": True}}
        tile_map = arcade.load_tilemap('map.tmx',layer_options=layer_options,scaling=0.5)
        self.scene = arcade.Scene.from_tilemap(tile_map)
        self.player = arcade.Sprite(':resources:/images/animated_characters/female_adventurer/femaleAdventurer_idle.png')
        self.player.position = (30, 200)
        self.scene.add_sprite("Player", self.player)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene.get_sprite_list("Walls"),
                                                         gravity_constant=GRAVITY)
        
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        self.jump_sound = arcade.load_sound(":resources:sounds/jump2.wav")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover1.wav")

    def on_update(self, delta_time):    
        self.scene.update_animation(delta_time)        

        if arcade.check_for_collision_with_list(self.player, self.scene["Water"]):
            arcade.play_sound(self.gameover_sound)
            self.player.change_y = -0.1  # Stop gravity

        if self.player.bottom < -20:
            self.player.position = (30, 400)  # Reset player position
       

        self.physics_engine.update()
    def on_draw(self):
        self.clear()
        self.scene.draw()     

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)

        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player.change_x = 0

window = arcade.Window(600,400,title="Arcade") 
window.set_location(900, 100)  
game = GameView()
window.show_view(game)
arcade.run()
 

