import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.current_player = 'X'
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.game_over = False

    def play(self, row, col):
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

class TicTacToeGUI:
    def __init__(self):
        self.game = TicTacToe()

        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.status_label = tk.Label(self.root, text='Current player: ' + self.game.current_player)
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(self.root, text='Restart Game', command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)

        self.root.mainloop()

    def button_click(self, row, col):
        if self.game.board[row][col] == '' and not self.game.game_over:
            self.game.play(row, col)
            self.buttons[row][col].config(text=self.game.board[row][col])
            if self.game.game_over:
                self.status_label.config(text='Game over! Winner: ' + self.game.current_player)
            else:
                self.status_label.config(text='Current player: ' + self.game.current_player)

    def restart_game(self):
        self.game = TicTacToe()
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)
        self.status_label.config(text='Current player: ' + self.game.current_player)

if __name__ == '__main__':
    TicTacToeGUI()

give me a testing code and yaml file to deploy on github pages
