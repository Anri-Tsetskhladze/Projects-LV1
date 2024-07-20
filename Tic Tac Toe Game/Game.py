import pygame
import sys

pygame.init()

width, height = 500, 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

board = [['' for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

def draw_board():
    screen.fill(white)
    pygame.draw.line(screen, black, (width // 3, 0), (width // 3, height), 7)
    pygame.draw.line(screen, black, (2 * width // 3, 0), (2 * width // 3, height), 7)
    pygame.draw.line(screen, black, (0, height // 3), (width, height // 3), 7)
    pygame.draw.line(screen, black, (0, 2 * height // 3), (width, 2 * height // 3), 7)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, red, (col * width // 3 + 20, row * height // 3 + 20), ((col + 1) * width // 3 - 20, (row + 1) * height // 3 - 20), 15)
                pygame.draw.line(screen, red, ((col + 1) * width // 3 - 20, row * height // 3 + 20), (col * width // 3 + 20, (row + 1) * height // 3 - 20), 15)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, blue, (col * width // 3 + width // 6, row * height // 3 + height // 6), width // 6 - 20, 15)

def check_winner():
    global game_over

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            game_over = True
            return board[row][0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            game_over = True
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != '':
        game_over = True
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != '':
        game_over = True
        return board[0][2]

    return None

def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return False
    return True

def restart_game():
    global board, current_player, game_over
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // (height // 3)
            col = x // (width // 3)

            if board[row][col] == '':
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    draw_board()
    winner = check_winner()
    if winner:
        print(f"Player {winner} wins!")
        game_over = True
    elif is_board_full():
        print("It's a tie!")
        game_over = True

    pygame.display.update()