from button import Button
from settings import *
import pygame


def slider_function(window, event, slider_position, x, y, length, min_value, max_value):
    black = (0, 0, 0)
    white = (255, 255, 255)
    is_dragging = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if x <= mouse_x <= x + length and y - 20 <= mouse_y <= y + 20:
                is_dragging = True
    elif event.type == pygame.MOUSEBUTTONUP:
        is_dragging = False
    elif event.type == pygame.MOUSEMOTION:
        if is_dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if x <= mouse_x <= x + length:
                slider_position = mouse_x - x

    value = min_value + (max_value - min_value) * (slider_position / length)
    window.fill(black)
    pygame.draw.line(window, white, (x, y), (x + length, y), 5)
    pygame.draw.circle(window, white, (x + slider_position, y), 15)
    pygame.display.update()

    return value



