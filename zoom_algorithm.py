#!/usr/bin/env python3

import pygame as pg
from modules.constants import *

def main():
    pg.init()

    screen = pg.display.set_mode(WINDOW)
    clock = pg.time.Clock()
    running = True
    zoom = False
    reset = False

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    # Zoom In
                    zoom = 'in'
                if event.key == pg.K_DOWN:
                    # Zoom Out
                    zoom = 'out'
                if event.key == pg.K_r:
                    reset = True


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")


        # RENDER YOUR GAME HERE
        for rect in rects:
            # Reset if user pushes 'R'
            if reset:
                rect.re_init()
            # Zoom if user pushes arrows (up or down)
            if zoom:
                rect.do_zoom(pg.mouse.get_pos(), zoom)
            # Print the results
            rect.draw(screen)

        reset = False
        zoom = False
        # flip() the display to put your work on screen
        pg.display.flip()

        clock.tick(60)  # limits FPS to 60

    pg.quit()

if __name__ == "__main__":
    main()