import pygame
def input_box(window, font, x, y, width, height):
    input_box_rect = pygame.Rect(x, y, width, height)
    input_text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.draw.rect(window, (0, 0, 0), input_box_rect, 2)

        text_surface = font.render(input_text, True, (0, 0, 0))
        window.blit(text_surface, (input_box_rect.x + 5, input_box_rect.y + 5))

        pygame.display.flip()