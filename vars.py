#imports
import pygame as pg

#surfaces
screen_size = (900, 600)
screen = pg.display.set_mode((screen_size[0], screen_size[1]))

#setting player variables
player_size = (100, 100)
player_pos = pg.Vector2(screen_size[0] / 2, screen_size[1] / 2)

#map data
map_size = (screen_size[0]*4, screen_size[1]*4)
map_pos = pg.Vector2(-200, -200)

#textbox vars
box_size = (900, 200)
box_y = screen_size[1] - box_size[1]
font_size = 32
name_pos = ((screen_size[0]/4)*3, box_y + font_size/2)
#Change this later (if I cba)
body_pos = (40, box_y + 80)
t_index = 0
t_shown = True

#font
pg.font.init()
pfont = pg.font.Font("fonts/Pixel.ttf", font_size)

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