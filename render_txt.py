import pygame as pg
import vars as v

def drawtxt():
    try:
        #draws sprite
        if v.t_shown:
            v.screen.blit(pg.transform.scale(v.vars_map["txt_b_sprite"], (v.box_size[0], v.box_size[1])), (0, v.box_y))

        #opens the dialogue text file and splits it by line
        with open("dialogue.txt", "r") as dialogue:
            lines = dialogue.read().splitlines()

        current_txt = lines[v.t_index].split(";")
        pg.font.init()
        text = v.pfont.render(current_txt[0].upper(), True, "black")
        body = v.pfont.render(current_txt[1].upper(), True, "black")
        v.screen.blit(text, (v.name_pos[0], v.name_pos[1]))
        v.screen.blit(body, (v.body_pos[0], v.body_pos[1]))

    except IndexError:
        v.t_shown = False
