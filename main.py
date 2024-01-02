import re
class Player:
    def __init__(self):
        """
        initialize class attributes with empty strings
        """
        self.name = ""
        self.symbol = ""
        
    def choose_name(self):
        while True:
            name = input('Enter player name (letters only)')
            if self.check_name():
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
        symbol = input(f"{self.name}, choose a symbol (single letter)")
        while True:
            if self.check_symbol:
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
            msg = input()
            if msg == "s":
                return msg
            elif msg == 'q':
                print('Thank you')
                break
            else:
                print('please enter either (s) or (q)')
            
    def show_finish_menu(self):
        print("thank you for your playing with us hope you like this game,\n if you want to play again choose (r) as restart or (q) as quit")
        while True:
            msg = input()
            if msg == 'r':
                return msg
            elif msg == 'q':
                print('thanks for your playing with us')
                break
            else:
                print('please enter either (r) or (q)')
       
    def validate_choice(self, choice):
        if choice == 'r' or choice == 's':
            return choice
        elif choice == 'q':
            print('thanks for your playing with us')
            
if __name__ == "__main__":
    menu_obj = Menu()
    # menu_obj.show_main_menu()
    menu_obj.show_finish_menu()