import pygame as pg

pg.init()
font = pg.font.Font(None, 30)

def debug(info, x = 10, y = 10):
    display_surface = pg.display.get_surface()
    debug_surface = font.render(str(info), True, 'Black')
    debug_rect = debug_surface.get_rect(topleft = (x, y))
    display_surface.blit(debug_surface, debug_rect)