import random

class Rock_Paper_Scissor_Mehmet_Ozay:
    def __init__(self):
        self.count_computer = 0
        self.count_user = 0
        self.gameTools()
    
    # Rock, Paper and Scissor here
    def gameTools(self):
        self.rock = '''
                _______
        -----'      ____)
                  (______)
                (________)
                    (____)
        -----._____(___)

        '''

        self.paper = '''

            _________
        ---'    _____)_____
                    _______)
                    _________)
                    _______)
        ---._____________)            

        '''

        self.scissor = '''

            ________
        ---'    _____)_____
                    _______)
                ____________)
                (____)
        ---.____(___)

        '''

    # Shows the options that the computer and the user should select
    def gameOptions(self):
        if(self.computer == 1):
            print(self.rock)
        elif(self.computer == 2):
            print(self.paper)
        elif(self.computer == 3):
            print(self.scissor)
        else:
            print("Wrong guess")
            
        if(self.user == 1):
            print(self.rock)
        elif(self.user == 2):
            print(self.paper)
        elif(self.user == 3):
            print(self.scissor)
        else:
            print("Wrong guess")
          
    # Show the scoreboard
    def countOptions(self):  
        if(self.count_computer <= 0):
            self.count_computer = 0
        elif((self.count_user <= 0)):
            self.count_user = 0
        elif(self.count_computer >= 2):
            self.count_computer = 2  
        elif((self.count_user >= 2)):
            self.count_user = 2    
        else:
            pass
        
    # Starts the game again
    def gameAgain(self):
        while(True):
            self.choise = input("Do you want to play again (y/n) : ")
            if(self.choise == 'y'):
                self.count_computer = 0
                self.count_user = 0
                self.gameBegin()
            elif(self.choise == 'n'):
                break
            else:
                print("Wrong choice, please try again")
                return 
        
    # Shows the endgame screen
    def endGameOptions(self):
        if(self.computer == self.user):
            print("Draw")
            self.countOptions()
            print("Computer : "+str(self.count_computer)+" - "+str(self.count_user)+" : User")
        elif((self.computer == 1 and self.user == 3) or (self.computer == 2 and self.user == 1) or (self.computer == 3 and self.user == 2)):
            self.count_computer += 1
            self.count_user -= 1
            self.countOptions()
            print("Computer win")
            print("Computer : "+str(self.count_computer)+" - "+str(self.count_user)+" : User")
        elif((self.computer == 3 and self.user == 1) or (self.computer == 1 and self.user == 2) or (self.computer == 2 and self.user == 3)):
            self.count_computer -= 1
            self.count_user += 1
            self.countOptions()
            print("User win")
            print("Computer : "+str(self.count_computer)+" - "+str(self.count_user)+" : User")
        else:
            print("This is an impossible")
    
    # The game is start menu
    def gameBegin(self):
        while(True): 
            print("1 - Rock\n2 - Paper\n3 - Scissor\n")
            self.computer = random.randint(1,3)
            try:  
                self.user = int(input("Choose a number between 1 and 3 : "))
                if self.user not in [1, 2, 3]:
                        raise ValueError
            except ValueError:
                print("Wrong number, please try again")
                return 
            
            self.gameOptions()
            self.endGameOptions()
            
            if(self.count_computer == 2):
                print("Game over, the champion is computer")
                self.gameAgain()
                break
            elif(self.count_user == 2):
                print("Game over, the champion is you")
                self.gameAgain()
                break              
while(True):
    print('''      _=====_                               _=====_\n     / _____ \                             / _____ \\\n   +.-\'_____\'.---------------------------.-\'_____\'.+\n  /   |     |  \'.        S O N Y        .\'  |  _  |   \\\n / ___| /|\\ |___ \\                     / ___| /_\\ |___ \\\n/ |      |      | ;  __           _   ; | _         _ | ;\n| | <---   ---> | | |__|         |_:> | ||_|       (_) | |\n| |___   |   ___| ;SELECT       START ; |___       ___| ;\n|\\    | \\|/ |    /  _     ___      _   \\    | (X) |    /|\n| \\   |_____|  .\',\'" "\', |___|  ,\'" "\', \'.  |_____|  .\' |\n|  \'-.______.-\' /       \\ANALOG/       \\  \'-._____.-\'   |\n|               |       |------|       |                |\n|              /\\       /      \\       /\\               |\n|             /  \'.___.\'        \'.___.\'  \\              |\n|            /                            \\             |\n \\          /                              \\           /\n  \\________/                                \\_________/''')
    print("\nWELCOME TO GAME\n")
    print("1 - Play Game\nQ - Quit Game\n")
    choose = input("Choose a number/letter to play : ")
    if choose == '1':
        game = Rock_Paper_Scissor_Mehmet_Ozay()
        game.gameBegin()
    elif((choose == 'Q') or (choose == 'q')):
        break
    else:
        print("Wrong letter/number. Please try again.")
    