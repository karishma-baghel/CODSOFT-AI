import random

def print_board(state):
    print(f"{state[0]} | {state[1]} | {state[2]}")
    print(f"{state[3]} | {state[4]} | {state[5]}")
    print(f"{state[6]} | {state[7]} | {state[8]}")

def check_win(state):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if state[win[0]] == state[win[1]] == state[win[2]] != ' ':
            return True
    return False

def ai_move(state):
    available_moves = [i for i in range(9) if state[i] == ' ']
    move = random.choice(available_moves)
    return move
def main():
    state = [' '] * 9
    turn = 'X'
    print("Welcome to Tic Tac Toe")

    while True:
        print_board(state)
        player = 'Your' if turn == 'X' else 'AI'
        print(f"{player}'s Chance")
        if turn == 'X':
            value = int(input("Please enter a value (1-9): ")) - 1
            state[value] = 'X'
        else:
            print("AI's Chance")
            value = ai_move(state)
            print(f"AI chose {value + 1}")
            state[value] = '0'
        if check_win(state):
            print_board(state)
            print(f"You won the match!" if turn == 'X' else "AI won the match!")
            break
        turn = '0' if turn == 'X' else 'X'

if __name__ == "__main__":
    main()
