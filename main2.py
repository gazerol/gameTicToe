from tkinter import Tk, Label, Button
import random


def end_game(char):
    # Disabling field buttons
    for button in all_buttons:
        button.config(state="disabled")
    if char == 'X':
        label.config(text="Winner Computer", font=('Verdana', 14, 'bold'))
    else:
        label.config(text="Winner Player", font=('Verdana', 14, 'bold'))


def move_computer():
    # Computer Step recording
    while True:
        b_row = random.randint(0, 9)
        b_col = random.randint(0, 9)
        if field[b_row][b_col]['text'] != 'X' and field[b_row][b_col]['text'] != 'O':
            field[b_row][b_col].config(text='O', bg="orange", state="disabled")
            break


def check_loss(char):
    # Horizontal Loss Check
    for i in range(10):
        for j in range(6):
            if field[i][j]['text'] == field[i][j + 1]['text'] == field[i][j + 2]['text'] \
                    == field[i][j + 3]['text'] == field[i][j + 4]['text'] == char:
                return True
    # Vertical Loss Check
    for i in range(6):
        for j in range(10):
            if field[i][j]['text'] == field[i + 1][j]['text'] == field[i + 2][j]['text'] \
                    == field[i + 3][j]['text'] == field[i + 4][j]['text'] == char:
                return True
    # Checking the loss by diagonals
    for i in range(6):
        for j in range(6):
            if field[i][j]['text'] == field[i + 1][j + 1]['text'] == field[i + 2][j + 2]['text'] \
                    == field[i + 3][j + 3]['text'] == field[i + 4][j + 4]['text'] == char:
                return True
    for i in range(6):
        for j in range(4, 10):
            if field[i][j]['text'] == field[i + 1][j - 1]['text'] == field[i + 2][j - 2]['text'] \
                    == field[i + 3][j - 3]['text'] == field[i + 4][j - 4]['text'] == char:
                return True


def move_player(row, col):
    # Recording a player's step
    global count_step
    count_step += 1
    field[row][col].config(text='X', bg="cyan", state="disabled")
    if check_loss('X'):
        end_game('X')

    move_computer()
    if check_loss('O'):
        end_game('O')

    if count_step == 50:
        label.config(text="DRAW", font=('Verdana', 14, 'bold'))


def app():
    # Adding buttons-fields for the game
    for row in range(10):
        line = []
        for col in range(10):
            button = Button(
                text='',
                width=4,
                height=2,
                bg='LightSteelBlue',
                command=lambda select_row=row, select_col=col: move_player(select_row, select_col)
            )
            button.grid(row=row+1, column=col+1)
            line.append(button)
            all_buttons.append(button)
        field.append(line)

    window.mainloop()


def new_game():
    # Creating variables
    global field, all_buttons, count_step, game
    field = []
    all_buttons = []
    count_step = 0
    game = True
    label.config(text="The game started")
    app()


if __name__ == '__main__':
    # Creating GUI
    window = Tk()
    window.title("X and O")
    window.config(padx=10, pady=10)

    label = Label(font=('Verdana', 14, 'bold'))
    label.grid(row=0, column=0, columnspan=10)

    butt_new_game = Button(text='New Game', font=('Verdana', 14, 'bold'), bg='LightSteelBlue', command=new_game)
    butt_new_game.grid(row=11, column=0, columnspan=10)

    # Run Game
    global field, all_buttons, count_step, game
    new_game()
