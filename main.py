class Player:
    def __init__(self):
        """
        initialize class attributes with empty strings
        """
        self.name = ""
        self.symbol = ""
        
    def choose_name(self):
        while True:
            name = input('Enter player name (letters only)> ')
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
        print('Welcome to the tic-toe game please choose (s) to start the game or (q) to quit\n')
        while True:
            msg = input("> ")
            if msg == "s":
                return msg
            elif msg == 'q':
                break
            else:
                print('please enter either (s) or (q)')
            
    def show_finish_menu(self):
        print("thank you for your playing with us hope you like this game,\n if you want to play again choose (r) as restart or (q) as quit")
        while True:
            msg = input()
            if msg == "s":
                return msg
            elif msg == 'q':
                print('Thank you')
                break
            else:
                print('please enter either (s) or (q)')
       

class Board:
    def __init__(self):
        self.board = [ str(i) for i in range(1,10)]
        self.b_size = len(self.board)
        
    def show_board(self):
        for i in range(0, self.b_size, 3):
            print(' | '.join(self.board[i:i+3]))
            if i==6:
                break
            print('-'*10)
        
    def reset_board(self):
        for i in range(self.b_size):
            if not(self.board[i].isdigit()):
                self.board[i] = str(i+1)
        # or we can do it by: self.board = [ str(i) for i in range(1,10)]
    
    def update_board(self, position, choice):
        if self.is_valid_move(position):
            self.board[position-1] = choice
            return True
        print('this cell is taken, try to choose another position again')
        return False
        
    def is_valid_move(self, position):
        return self.board[position-1].isdigit()
        

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player()
        self.player2 = Player()
        self.menu = Menu()
        self.curr_player_idx = 1 # by default player 1
        
    def start_game(self):
        selected_choice = self.menu.show_main_menu()
        
        if selected_choice == 's':

            self.play_game()
        else:
            self.end_game()
    
    def end_game(self):
        self.menu.show_finish_menu()
    
    def play_game(self):
        self.player1.choose_name()
        self.player1.choose_symbol()
        
        self.player2.choose_name()
        self.player2.choose_symbol()
        
        print('\n')
        self.board.show_board()
        
        for i in range(9):
            
            player_choice = input(f'\n {self.player1.name} turn, now choose a place to put ({self.player1.symbol})> ')
            self.board.update_board(int(player_choice), self.player1.symbol)
        
        print('\n')
        self.board.show_board()
        
        
        
    
    def check_win(self):
        pass
    
    def check_draw(self):
        pass
    
    def restart_game(self):
        pass    
        
             
if __name__ == "__main__":
    game = Game()
    
    game.start_game()