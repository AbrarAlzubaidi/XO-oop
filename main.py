import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        """
        initialize class attributes with empty strings
        """
        self.name = ""
        self.symbol = ""
        
    def choose_name(self, i):
        """
        give user access to enter the name
        """
        while True:
            name = input(f'Player {i}, enter player name (letters only)> ')
            if self.check_name(name):
                self.name = name
                break
            print('Invalid name. please enter a valid name')
        
    def check_name(self, name):
        """
        check if player name contains only characters(alphabet)
        """
        if name.isalpha() == True:
            return True
        return False
        
    def choose_symbol(self):
        """
        give user access to enter the symbol
        """
        while True:
            symbol = input(f"{self.name}, choose a symbol (single letter)> ")
            if self.check_symbol(symbol):
                self.symbol = symbol.upper()
                break
            print('Invalid symbol, choose a valid one')
        
    def check_symbol(self, symbol):
        """
        check if symbol is only one character
        """
        if len(symbol) == 1 and symbol.isalpha():
            return True
        return False
        
      
class Menu:
    
    def show_main_menu(self):
        """
        show main menu game
        """
        print('Welcome to the tic-toe game please choose (s) to start the game or (q) to quit\n')
        while True:
            msg = input("> ")
            if msg == "s":
                clear_screen()
                return msg
            elif msg == 'q':
                break
            else:
                print('please enter either (s) or (q)')
            
    def show_finish_menu(self):
        """
        show restart menu game
        """
        print("thank you for your playing with us hope you like this game,\n if you want to play again choose (r) as restart or (q) as quit")
        while True:
            msg = input()
            if msg == "r":
                return msg
            elif msg == 'q':
                break
            else:
                print('please enter either (s) or (q)')
       

class Board:
    def __init__(self):
        """
        initialize a board with 1-9
        """
        self.board = [ str(i) for i in range(1,10)]
        self.b_size = len(self.board)
        
    def show_board(self):
        """
        show the board to the user
        """
        for i in range(0, self.b_size, 3):
            print(' | '.join(self.board[i:i+3]))
            if i==6:
                break
            print('-'*10)
        
    def reset_board(self):
        """
        reset the board
        """
        for i in range(self.b_size):
            if not(self.board[i].isdigit()):
                self.board[i] = str(i+1)
        # or we can do it by: self.board = [ str(i) for i in range(1,10)]
    
    def update_board(self, position, choice):
        """
        update the board with the user choice
        """
        if self.is_valid_move(position):
            self.board[position-1] = choice
            return True
        return False
        
    def is_valid_move(self, position):
        """
        check if the choosen cell is availabl
        """
        return self.board[position-1].isdigit()
        

class Game:
    def __init__(self):
        """
        initialize game logic
        """
        self.board = Board()
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.curr_player_idx = 0 
        
    def start_game(self):
        """
        start the game
        """
        selected_choice = self.menu.show_main_menu()
        
        if selected_choice == 's':
            self.play_game()
        else:
            self.end_game()
    
    def end_game(self):
        """
        end the game
        """
        print('Thank you 🤗')
    
    def play_game(self):
        """
        play the game 
        """
        for i, player in enumerate(self.players, start=1):
            player.choose_name(i)
            player.choose_symbol()
            clear_screen()
            
        self.board.show_board()
        print('\n')
        
        while True:
            self.play_trun()
            if self.check_win():
                winner = self.players[not self.curr_player_idx].name
                print(f'Player 🥳🥳 {winner} 🥳🥳 wins 😎 \n')
            if self.check_draw():
                print(f'Game is over, no possible moves remains 🙄 \n')
                
            if self.check_win() or self.check_draw():
                choice = self.restart_game()
                if choice == 'r':
                    clear_screen()
                    self.play_game()
                else:
                    self.end_game()
                    break
    
    def play_trun(self):
        """
        check players turn 
        """
        curr_player = self.players[self.curr_player_idx] 
        choice = input(f'Player\'s {curr_player.name} turn, choose where you want to put {curr_player.symbol}> ')
        clear_screen()
        # check if the choice is not a letter and between 1-9
        # if the choice is a number and between 1-9: check if the number is not taken
        while True:
            try:
                if 0< int(choice) < 10 and self.board.update_board(int(choice), curr_player.symbol):
                    self.board.show_board()
                    print('\n')
                    
                    break
                else:
                    choice = input('Please choose for above available numbers and it should between 1->9> ')
                    self.board.update_board(int(choice), curr_player.symbol)
                    self.board.show_board()
                    print('\n')
                    
            except ValueError:
                print('please enter a number (1-9) not a letter')
                
        self.switch_player()
        
    def switch_player(self):
        """
        switch between players
        """
        self.curr_player_idx = not self.curr_player_idx
    
    def check_win(self):
        """
        check if win condition happen
        """
        return (
                self.board.board[0] == self.board.board[1] == self.board.board[2]
            ) or (
                self.board.board[3] == self.board.board[4] == self.board.board[5] 
            ) or (
                self.board.board[6] == self.board.board[7] == self.board.board[8]
            ) or (
                self.board.board[0] == self.board.board[3] == self.board.board[6]
            ) or (
                self.board.board[1] == self.board.board[4] == self.board.board[7]
            ) or (
                self.board.board[2] == self.board.board[5] == self.board.board[8]
            ) or (
                self.board.board[0] == self.board.board[4] == self.board.board[8]
            ) or (
                self.board.board[2] == self.board.board[4] == self.board.board[6]
            ) 
            
        """
        check this a BOOOOM way to solve this
        win_conoditions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [0,4,6]
        ]
        
        for combo in win_conoditions:
            if(self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False
        """   
    
    def check_draw(self):
        """
        check if draw condition happen
        """
        # check if all the board is a letter and no one win
        return all(not cell.isdigit() for cell in self.board.board)
    
    def restart_game(self):
        """
        reset the game
        """
        self.board.reset_board()
        self.curr_player_idx = 0 # to make sure the first player will play first
        
        return self.menu.show_finish_menu()
    
           
if __name__ == "__main__":
    game = Game()
    
    game.start_game()