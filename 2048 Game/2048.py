import logic

def print_matrix(mat):
    for row in mat:
        print(row)
    print()

def main():
    mat = logic.initialize_game()
    print_matrix(mat)
    
    while True:
        move = input("Press the command (W, A, S, D): ").lower()
        if move == 'w':
            mat = logic.move_up(mat)
        elif move == 's':
            mat = logic.move_down(mat)
        elif move == 'a':
            mat = logic.move_left(mat)
        elif move == 'd':
            mat = logic.move_right(mat)
        else:
            print("Invalid Key Pressed")
            continue

        state = logic.get_current_state(mat)
        if state == 'WON':
            print("YOU WON!")
            break
        elif state == 'LOST':
            print("GAME OVER!")
            break
        else:
            logic.add_new(mat)
            print_matrix(mat)

if __name__ == "__main__":
    main()