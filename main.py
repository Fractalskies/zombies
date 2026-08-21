#TODO: Add textboxes. Turn into OOP instead of FOP.

# #imports
import pygame as pg
import vars as v
import render_txt as text

#initialization
pg.init()
clock = pg.time.Clock()
running = True
dt = 0
pg.display.set_caption("Pure happiness and joy")


while running:
    for event in pg.event.get():
        #checks for the quit event
        if event.type == pg.QUIT:
            running = False
        #checks for a click event
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                v.t_index += 1

    #Filling the screen with a colour after every frame
    v.screen.fill("dark grey")

    #draws map sprite
    v.screen.blit(pg.transform.scale(v.vars_map["bg_sprite"], (v.map_size[0], v.map_size[1])), (v.map_pos.x,v.map_pos.y))

    #draws player sprite
    v.screen.blit(pg.transform.scale(v.vars_map["player_sprite"], (v.player_size[0], v.player_size[1])), (v.player_pos.x - (v.player_size[0]/2), v.player_pos.y - (v.player_size[1]/2)))

    #draws the text box sprite
    text.drawtxt()

    #Checks for movement, fix it later
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and v.map_pos[1] < -10:
        v.map_pos.y += 300 * dt

    #Make this dynamic later i can't be fucked rn
    if keys[pg.K_s] and v.map_pos[1] > -1600:
        v.map_pos.y -= 300 * dt

    if keys[pg.K_a] and v.map_pos[0] < -10:
        v.map_pos.x += 300 * dt

    if keys[pg.K_d] and v.map_pos[0] > -v.map_size[1] + v.screen_size[1]:
        v.map_pos.x -= 300 * dt

    #flips the screen
    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()