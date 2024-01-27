#!/usr/bin/env python3

import pygame as pg
from modules.constants import *

def main():
    pg.init()

    screen = pg.display.set_mode(WINDOW)
    clock = pg.time.Clock()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        # RENDER YOUR GAME HERE

        for rect in rects:
            rect.draw(screen)

        # flip() the display to put your work on screen
        pg.display.flip()

        clock.tick(60)  # limits FPS to 60

    pg.quit()

if __name__ == "__main__":
    main()