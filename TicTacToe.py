import os
import keyboard


class TicTacToe:
    player_symbols = ["X", "O"]

    def __init__(self):
        self.fields = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
        self.player_turn = 1
        self.victory_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def check_victory(self):
        symbol = self.player_symbols[self.get_player_minus1()]
        for c in self.victory_conditions:
            if self.fields[c[0]] == symbol and self.fields[c[1]] == symbol and self.fields[c[2]] == symbol:
                return True
        return False

    def victory(self):
        print(f"congratulations player{self.player_turn} you have won!")

    def get_player_minus1(self):
        return self.player_turn - 1

    def print_field(self):
        os.system('cls')
        print("welcome to TicTacToe by Phaseoil!")
        print("this is the playing field you'll be using")
        print(f""" {self.fields[1]} | {self.fields[2]} | {self.fields[3]}
 {self.fields[4]} | {self.fields[5]} | {self.fields[6]}
 {self.fields[7]} | {self.fields[8]} | {self.fields[9]}""")

    def check_draw(self):
        invalid_fields = []
        for key in self.fields.keys():
            if self.check_valid_field(key):
                return False
            else:
                invalid_fields.append(key)
            if len(invalid_fields) == len(self.fields.keys()):
                return True

    def change_turn(self):
        if self.player_turn == 1:
            self.player_turn = 2
        elif self.player_turn == 2:
            self.player_turn = 1

    @staticmethod
    def draw():
        print("yay, neither player1 nor player2 has won! it's a draw!")

    def get_userinput(self):
        while True:
            i = input("which field do you choose? (1-9)\n")
            try:
                int(i)
            except ValueError:
                self.print_field()
                print("that isn't even a number...")
                continue
            if int(i) in self.fields.keys():
                return int(i)
            else:
                self.print_field()
                print("this field doesn't exist")

    def check_valid_field(self, field):
        if field in self.fields.keys():
            if self.fields[field] == " ":
                return True
            else:
                return False
        else:
            return False

    def claim_field(self, field):
        self.fields[field] = TicTacToe.player_symbols[self.get_player_minus1()]

    def play(self):
        while True:
            self.print_field()
            print(f"player {self.player_turn}'s turn")
            i = self.get_userinput()
            if self.check_valid_field(i):
                self.claim_field(i)
            else:
                continue
            if self.check_victory():
                self.print_field()
                self.victory()
                break
            if self.check_draw():
                self.print_field()
                self.draw()
                break
            self.change_turn()
        print("thank you for playing!")
        print("press space to play again or c to cancel")
        while True:
            if keyboard.is_pressed('space'):
                spiel = TicTacToe()
                spiel.play()
            if keyboard.is_pressed('c'):
                os._exit(0)


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
