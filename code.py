#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage


def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython 
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    background = stage.Grid(image_bank_background, 10, 8)
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        
        # update game logic
        
        # redraw Sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
    
