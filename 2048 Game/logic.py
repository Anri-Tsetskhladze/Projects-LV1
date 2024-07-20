import random

def initialize_game():
    mat = [[0] * 4 for _ in range(4)]
    add_new(mat)
    add_new(mat)
    return mat

def add_new(mat):
    row, col = random.choice([(r, c) for r in range(4) for c in range(4) if mat[r][c] == 0])
    mat[row][col] = 2

def compress(mat):
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
    return mat

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append(mat[i][::-1])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([mat[j][i] for j in range(4)])
    return new_mat

def move_left(grid):
    new_grid = compress(grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    return new_grid

def move_right(grid):
    new_grid = reverse(grid)
    new_grid = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid

def move_up(grid):
    new_grid = transpose(grid)
    new_grid = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid

def move_down(grid):
    new_grid = transpose(grid)
    new_grid = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'
    
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER'
    
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'
    
    return 'LOST'