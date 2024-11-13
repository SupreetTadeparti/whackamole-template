import pygame
from random import randrange

DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 512
GRID_COLS = 20
GRID_ROWS = 16
SQUARE_SIZE = 32

def draw_lines(screen):
    # Vertical Lines
    for i in range(1, GRID_COLS):
        x = (DISPLAY_WIDTH / GRID_COLS) * i
        pygame.draw.line(screen, (13, 112, 13), (x, 0), (x, DISPLAY_HEIGHT))
    
    # Horizontal Lines
    for i in range(1, GRID_ROWS):
        y = (DISPLAY_HEIGHT / GRID_ROWS) * i
        pygame.draw.line(screen, (13, 112, 13), (0, y), (DISPLAY_WIDTH, y))
    

def draw_mole(screen, mole_image, mole_pos):
    screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))

def gen_centered_pos():
    col = randrange(0, GRID_COLS)
    row = randrange(0, GRID_ROWS)

    return (SQUARE_SIZE * col, SQUARE_SIZE * row )

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        (mole_width, mole_height) = mole_image.get_size()
        mole_pos = gen_centered_pos()
        screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_mole = pygame.Rect((*mole_pos, mole_width, mole_height)).collidepoint(*event.pos)
                    if clicked_mole:
                        mole_pos = gen_centered_pos()
            screen.fill("light green")
            draw_lines(screen)
            draw_mole(screen, mole_image, mole_pos)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
