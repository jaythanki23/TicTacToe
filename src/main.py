import pygame
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN

# pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 300, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LINE_COLOR = (37, 47, 46)
GREEN = (0, 128, 0)
ALT_BLUE = (17, 141, 180)

FPS = 60

matrix = np.zeros([3, 3])

p1 = 11
p2 = 10

x_image = pygame.image.load(r"F:\Programming\Python-Projects\TicTacToe\x.png")
o_image = pygame.image.load(r"F:\Programming\Python-Projects\TicTacToe\o.png")

x_image = pygame.transform.scale(x_image, (70, 70))
o_image = pygame.transform.scale(o_image, (70, 70))


def draw_window():
    WIN.fill(WHITE, rect=(0, 0, 300, 300))
    # pygame.draw.rect(WIN, WHITE, (50, 20, 120, 100))
    # Horizontal lines
    pygame.draw.line(WIN, LINE_COLOR, (0, 100), (300, 100), 10)
    pygame.draw.line(WIN, LINE_COLOR, (0, 200), (300, 200), 10)
    # Vertical lines
    pygame.draw.line(WIN, LINE_COLOR, (100, 0), (100, 300), 10)
    pygame.draw.line(WIN, LINE_COLOR, (200, 0), (200, 300), 10)
    pygame.display.update()


def display(count, row, col, ans):
    myfont = pygame.font.SysFont('Calibri', 30)

    if ans == "X" or ans == "O":
        game_over(ans)

    else:

        if count % 2 != 0:
            o_text_surface = myfont.render("O's Turn", False, WHITE)
            pygame.draw.rect(WIN, BLACK, (0, 300, 300, 100))
            WIN.blit(o_text_surface, (100, 350))
            WIN.blit(x_image, (col*100 + 10, row*100 + 10))
            pygame.display.update()

        if count % 2 == 0:
            x_text_surface = myfont.render("X's Turn", False, WHITE)
            pygame.draw.rect(WIN, BLACK, (0, 300, 300, 100))
            WIN.blit(x_text_surface, (100, 350))
            WIN.blit(o_image, (col*100 + 10, row*100 + 10))
            pygame.display.update()

        if count >= 9:
            text_surface = myfont.render(f"Draw", False, BLACK)
            pygame.draw.rect(WIN, WHITE, (0, 0, 300, 400))
            WIN.blit(text_surface, (150, 150))


def check_entries(matrix):
    # axis = 1 is for rows, axis = 0 is for columns

    # check columns
    col_ans1 = np.all(matrix == 11, axis=0)
    col_ans2 = np.all(matrix == 10, axis=0)
    if True in col_ans1:
        return "X"
    if True in col_ans2:
        return "O"

    # check rows
    row_ans1 = np.all(matrix == 11, axis=1)
    row_ans2 = np.all(matrix == 10, axis=1)
    if True in row_ans1:
        return "X"
    if True in row_ans2:
        return "O"

    # check both diagonals
    main_diag = matrix.diagonal()
    if np.all(main_diag == 11):
        return "X"
    if np.all(main_diag == 10):
        return "O"

    sec_diag = np.fliplr(matrix).diagonal()
    if np.all(sec_diag == 11):
        return "X"
    if np.all(sec_diag == 10):
        return "O"

    return "No winner yet"


def game_logic(x, y, count):
    if count % 2 != 0:
        matrix[x, y] = p1

    if count % 2 == 0:
        matrix[x, y] = p2

    if count >= 5:
        ans = check_entries(matrix)
        if ans == "X":
            return "X"

        if ans == "O":
            return "O"

    return ""


def game_over(ans):
    myfont = pygame.font.SysFont('Calibri', 30)
    text_surface = myfont.render(f"Game over: Winner is {ans}", False, BLACK)
    pygame.draw.rect(WIN, WHITE, (0, 0, 300, 400))
    WIN.blit(text_surface, (10, 150))


def main():
    turn_count = 0
    run = True
    clock = pygame.time.Clock()
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == MOUSEBUTTONDOWN:
                mousex = event.pos[0]
                mousey = event.pos[1]

                clicked_row = int(mousey // 100)
                clicked_col = int(mousex // 100)

                turn_count += 1
                ans = game_logic(clicked_row, clicked_col, turn_count)
                display(turn_count, clicked_row, clicked_col, ans)
                # print((mousex, mousey))
                # print(clicked_row, clicked_col)

        # draw_window()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
