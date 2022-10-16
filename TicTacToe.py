import time


class TicTacToe:
    player_symbol = ["X", "O"]

    def __init__(self):
        self.fields = {
            1: " ",
            2: " ",
            3: " ",
            4: " ",
            5: " ",
            6: " ",
            7: " ",
            8: " ",
            9: " "
        }
        self.player_turn = 1

    def check_victory(self):
        symbol = TicTacToe.player_symbol[self.get_player_minus1()]
        if self.fields[1] == symbol and self.fields[2] == symbol and self.fields[3] == symbol:
            return True
        elif self.fields[4] == symbol and self.fields[5] == symbol and self.fields[6] == symbol:
            return True
        elif self.fields[7] == symbol and self.fields[8] == symbol and self.fields[9] == symbol:
            return True
        elif self.fields[1] == symbol and self.fields[5] == symbol and self.fields[9] == symbol:
            return True
        elif self.fields[7] == symbol and self.fields[5] == symbol and self.fields[3] == symbol:
            return True
        else:
            return False

    def victory(self):
        print(f"congratulations player{self.player_turn} you have won!")

    def get_player_minus1(self):
        return self.player_turn - 1

    def print_field(self):
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
        i = input("which field do you choose? (1-9)\n")
        if int(i) in self.fields.keys():
            return int(i)
        else:
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
        self.fields[field] = TicTacToe.player_symbol[self.get_player_minus1()]

    def play(self):
        print("welcome to TicTacToe by Phaseoil!")
        time.sleep(1)
        print("this is the playing field you'll be using")
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
        input("press a button to leave")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
