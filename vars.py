#imports
import pygame as pg

#screen :\
screen_size = (900, 600)
screen = pg.display.set_mode((screen_size[0], screen_size[1]))

#setting player variables
player_size = (100, 100)
player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#map data
map_size = (1200, 1200)
map_pos = pg.Vector2(-200, -200)

#defining import hashmap
vars_map = {}
#defining import function
def import_image():
    #Saves data from text file as list
    with open("image_imports.txt", "r") as images:
        lines = images.read().splitlines()

    #Seperates values in lists then stores them as a hash map
    for i in lines:
        temp_list = i.split(",")
        vars_map[temp_list[0]] = pg.image.load("images/"+temp_list[1])

import_image()