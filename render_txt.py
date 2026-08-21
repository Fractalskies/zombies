import pygame as pg
import vars as v

def drawtxt():
    #draws sprite
    v.screen.blit(pg.transform.scale(v.vars_map["txt_b_sprite"], (v.box_size[0], v.box_size[1])), (0, v.box_y))

    #opens the dialogue text file and splits it by line
    with open("dialogue.txt", "r") as dialogue:
        lines = dialogue.read().splitlines()

    #Iterates through each line and splits by a semicolon (not a comma because we may need to use this in dialogue)
    for i in lines:
        j = i.split(";")
        pg.font.init()
        text = v.pfont.render(j[0].upper(), True, "black")
        v.screen.blit(text, (v.name_pos[0], v.name_pos[1]))

