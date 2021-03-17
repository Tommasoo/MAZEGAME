import pygame

white = (255, 255, 255)
black = (0, 0, 0)

def button(mouse, surf, hoover_colour, rect, button_text = '', line_width = 5, button_colour = (255, 255, 255)):
    if mouse_on_button(mouse, rect):
        draw_button(surf, hoover_colour, rect, True, button_text, line_width, button_colour)
    else:
        draw_button(surf, hoover_colour, rect, False, button_text, line_width, button_colour)


def draw_button(surf, color, rect, hoover, button_text, button_line_width, button_colour, text_font = 'calibri', text_size = 30, ):
    #surf.fill(white)

    if hoover:
        pygame.draw.rect(surf, color, rect, 0)
    else:
        pygame.draw.rect(surf, button_colour, rect, 0)

    pygame.draw.rect(surf, black, rect, button_line_width)

    #text start
    if not (button_text == ''):
        button_font = pygame.font.SysFont(text_font, text_size, bold=True)  # font
        text = button_font.render(button_text, True, black)  #testo
        text_width, text_height = button_font.size(button_text)

        x_coord_text = rect[0] + rect[2] // 2 - text_width // 2
        y_coord_text = rect[1] + rect[3] // 2 - text_height // 2

        surf.blit(text, (x_coord_text, y_coord_text))


def mouse_on_button(mouse, rect):
    if rect[0] <= mouse[0] <= rect[0] + rect[2] and rect[1] <= mouse[1] <= rect[1] + rect[3]:
        return True
    else:
        return False