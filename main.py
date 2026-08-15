#TODO: GitHub repository.

# #imports
import pygame as pg
import vars as v

#initialization
pg.init()
clock = pg.time.Clock()
running = True
dt = 0

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #Filling the screen with a colour after every frame
    v.screen.fill("dark grey")

    #draws map sprite
    v.screen.blit(pg.transform.scale(v.vars_map["bg_sprite"], (v.map_size[0], v.map_size[1])), (v.map_pos.x,v.map_pos.y))

    #draws player sprite
    v.screen.blit(pg.transform.scale(v.vars_map["player_sprite"], (v.player_size[0], v.player_size[1])), (v.player_pos.x - (v.player_size[0]/2), v.player_pos.y - (v.player_size[1]/2)))

    #Checks for movement
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and v.map_pos[1] < -10:
        v.map_pos.y += 300 * dt

    if keys[pg.K_s] and v.map_pos[1] > -v.map_size[0] + v.screen_size[1] + 10:
        v.map_pos.y -= 300 * dt

    if keys[pg.K_a] and v.map_pos[0] < -10:
        v.map_pos.x += 300 * dt

    if keys[pg.K_d] and v.map_pos[0] > -v.map_size[1] + v.screen_size[0] + 10:
        v.map_pos.x -= 300 * dt

    #flips the screen
    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()