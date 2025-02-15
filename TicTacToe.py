# Project - TicTacToe Human vs. Computer

#Purpose: To recreate the childhood game of TicTacToe with an intelligent AI to play against

# Author: Saad Sanaullah
#
# Date: November 14, 2023

board = [[ 0 for x in range(3)] for y in range(3)] # 3x3 nested list
X_MARK = ' x ' # set to  ' x ' for player.
O_MARK = ' o ' # set to ' o ' for computer O
player = X_MARK   
WIN = 10  #BUG was here 
TIE = 12
# Methods -- add your own here as well

# setup board
def setupBoard():
    board[0][0] = ' 1 '
    board[0][1] = ' 2 '
    board[0][2] = ' 3 '
    board[1][0] = ' 4 '
    board[1][1] = ' 5 '
    board[1][2] = ' 6 '
    board[2][0] = ' 7 '
    board[2][1] = ' 8 '
    board[2][2] = ' 9 '
# End of setupBoard

# using two loops inside each other to create a grid of 3
def displayBoard():
    for r in range(3):    
        print(" ",end="")
        for c in range(3):
            print(board[r][c], end="")
            if c < 2:
                print("|",end="")
        print()
        if(r < 2):
            print(" ---|---|---")
# end of displayBoard

#checking all the different combinations of a winning situation or a blocking situation, and will return a string that is associated with a specific slot on the grid 

def checkMove(playerXorO):
  '''checks specific combinations that look for equality between an important slot sequence. returns missing slot string of that sequence or -1 if nothing is found. Has a parameter to idenitfy player or computer'''
  if (board[0][0] == board[0][1] == playerXorO) and validMove(board[0][2] ):
    return 'H13'
  elif board[0][0] == board[0][2]  == playerXorO and validMove(board[0][1] ):
    return 'H12'
  elif board[0][1] == board[0][2] == playerXorO and validMove(board[0][0] ):
    return 'H11'
  elif board[1][0] == board[1][1]  == playerXorO and validMove(board[1][2] ):
    return 'H23'
  elif board[1][0] == board[1][2] == playerXorO and validMove(board[1][1] ):
    return 'H22'
  elif board[1][1] == board[1][2] == playerXorO and validMove(board[1][0] ):
    return 'H21'
  elif board[2][0] == board[2][1] == playerXorO and validMove(board[2][2] ):
    return 'H33'
  elif board[2][0] == board[2][2] == playerXorO and validMove(board[2][1] ):
    return 'H32'
  elif board[2][1] == board[2][2] == playerXorO and validMove(board[2][0] ):
    return 'H31'
  elif board[0][0] == board[1][0] == playerXorO and validMove(board[2][0] ):
    return 'V13'
  elif board[0][0] == board[2][0] == playerXorO and validMove(board[1][0] ):
    return 'V12'
  elif board[1][0] == board[2][0] == playerXorO and validMove(board[0][0] ):
    return 'V11'
  elif board[0][1] == board[1][1] == playerXorO and validMove(board[2][1] ):
    return 'V23'
  elif board[0][1] == board[2][1] == playerXorO and validMove(board[1][1] ):
    return 'V22'
  elif board[1][1] == board[2][1] == playerXorO and validMove(board[0][1] ):
    return 'V21'
  elif board[2][2] == board[1][2] == playerXorO and validMove(board[0][2] ):
    return 'V31'
  elif board[0][2] == board[2][2] == playerXorO and validMove(board[1][2] ):
    return 'V32'
  elif board[1][2] == board[0][2] == playerXorO and validMove(board[2][2] ):
    return 'V33'
  elif board[1][1] == board[2][2] == playerXorO and validMove(board[0][0] ):
    return 'D11'
  elif board[0][0] == board[1][1] == playerXorO and validMove(board[2][2] ):
    return 'D13'
  elif board[0][0] == board[2][2] == playerXorO and validMove(board[1][1] ):
    return 'D12'
  elif board[0][2] == board[1][1] == playerXorO and validMove(board[2][0] ):
    return 'D23'
  elif board[1][1] == board[2][0] == playerXorO and validMove(board[0][2] ):
    return 'D21'
  elif board[2][0] == board[0][2] == playerXorO and validMove(board[1][1] ):
    return 'D22'
  return -1  #return when no winning combination

# makeMove() : returns the board position of the computer move
def makeMove () :
  '''Returns the board position of the computer move and is the logic that decides to make a specific move depending on availability of the other slots'''

  #1.Score a winning move if any:winningMove() : returns -1 if no computer winning move 
  slot = winningMove()
  if slot == -1 :
    slot = blockMove()

    #2.Block any moves:blockMove():returns -1 if no human winning move to block otherwise move 
   
    if slot == -1 :
      slot = counteractPlayerTrickMove()

    #3.Counteract any trickMoves by X ,returns -1 if no moves to counteract found
     
      if slot == -1 :
        slot = trickMove()
    
        
      #4.Any trick moves we can score:trickMove() : returns -1 if no tricky move, otherwise move
        if slot == -1 :
          slot = bruteForce()

  return slot      
  #4.Lastly score in any free slot
def counteractPlayerTrickMove() :
  '''looks at two two most common types of counter trick mehtods, and actively decides to block them or counter them. Function does not take in any parameters, and returns slot strings of the important slots to be executed.'''
  #if center free then put O mark in the centre?
  if validMove(board[1][1]):
    return "H22"
  
  if ( board[1][1] == O_MARK and board[0][0] == X_MARK and board[2][2] ==X_MARK ) or (board[0][2] == X_MARK and board[1][1]== O_MARK and board[2][0]== X_MARK ) :

    #then try to put an omark in the non-corner squares if they are free , so x ends up chasing us to block and does not do the trickMove
    if validMove(board[0][1]):
      return "H12"
    elif validMove(board[1][0]) :
       return "H21"
    elif validMove(board[2][1]):
      return "H32"  
    elif validMove(board[1][2]):
      return "H23"
  else :
    #no trick moves by x to counteract found 
    return -1

def bruteForce():
  
  '''Returns important board positions to counterattack and label against the player. These specific positions have strategic value on the board, and are returned in the slot string format. Function does not take in any parameters.'''

  
  #4 corners 
  if validMove(board[0][2]):
   return "H13"
  elif validMove(board[0][0]):
    return "H11"
  elif validMove(board[2][0]):
    return "H31"
  elif validMove(board[2][2]):
    return "H33"
    
  #edges
  elif validMove(board[0][1]):
    return "H12"
  elif validMove(board[1][0]):
    return "H21"
  elif validMove(board[1][2]):
    return "H23"
  elif validMove(board[2][1]):
    return "H32"


    
#1.Block any moves:blockMove():returns -1 if no human winning move to block otherwise move 
def blockMove() :
  '''looks at all the winning combinations and blocks if the player has one. Takes in no parameters, returns -1 if no winning move is found, and slot if a winning combination is found.''' 
  slot = checkMove(X_MARK) 
  if  slot == -1: #NO winning x's combination
    return -1 
  else : #winning combination found
    return slot

#2.Score a winning move if any:winningMove() : returns -1 if no computer winning move 
def winningMove() :
  '''looks at winning combinations and executes last position for the computer to win. Takes in no parameters, returns -1 if there is no winning move, and slot if a winning move is found.'''
  slot = checkMove(O_MARK) 
  if  slot == -1: #NO winning O's combination
    return -1 
  else : #winning combination found
    return slot

#function will take the string slot and act on it. Can be used to either block the players move, or land the winning move. 
def makeMyMove(slot):
  '''is the function that actually makes a move depending on the slot string it recieves as a parameter. Does not return anything.'''
  
  if slot == 'H13':
    board[0][2] = O_MARK
  elif slot == 'H12':
    board[0][1] = O_MARK
  elif slot == 'H11':
    board[0][0] = O_MARK
  elif slot == 'H23':
    board[1][2] = O_MARK
  elif slot == 'H22':
    board[1][1] = O_MARK
  elif slot == 'H21':
    board[1][0] = O_MARK
  elif slot == 'H33':
    board[2][2] = O_MARK
  elif slot == 'H32':
    board[2][1] = O_MARK
  elif slot == 'H31':
    board[2][0] = O_MARK
  elif slot == 'V31':
    board[0][2] = O_MARK
  elif slot == 'V21':
    board[0][1] = O_MARK
  elif slot == 'V11':
    board[0][0] = O_MARK
  elif slot == 'V32':
    board[1][2] = O_MARK
  elif slot == 'V22':
    board[1][1] = O_MARK
  elif slot == 'V12':
    board[1][0] = O_MARK
  elif slot == 'V33':
    board[2][2] = O_MARK
  elif slot == 'V23':
    board[2][1] = O_MARK
  elif slot == 'V13':
    board[2][0] = O_MARK
  elif slot == 'D11':
    board[0][0] = O_MARK
  elif slot == 'D12':
    board[1][1] = O_MARK
  elif slot == 'D13':
    board[2][2] = O_MARK
  elif slot == 'D21':
    board[0][2] = O_MARK
  elif slot == 'D22':
    board[1][1] = O_MARK
  elif slot == 'D23':
    board[2][0] = O_MARK


def trickMove():
  '''Looks at the common trick strategies and executes them effeciently when given a chance by retturning a slot string. has no parameters.'''
  #Try to get 3 corners
  corner_TOPLEFT =board[0][0]
  corner_TOPRIGHT= board[0][2]
  corner_BOTTOMLEFT =board[2][0]
  corner_BOTTOMRIGHT= board[2][2]
  CENTER = board[1][1]
  #Four scenarios 
  
  #First scenario:
  if (corner_TOPRIGHT == O_MARK or validMove(corner_TOPRIGHT) ) and (corner_BOTTOMLEFT == O_MARK or validMove(corner_BOTTOMLEFT)) and (corner_BOTTOMRIGHT == O_MARK or validMove(corner_BOTTOMRIGHT)) and (validMove(CENTER) or CENTER == O_MARK):
    if validMove(corner_TOPRIGHT):
      return "H13"
    elif validMove( corner_BOTTOMRIGHT) :
      return "H33"
    elif validMove(corner_BOTTOMLEFT):
      return "H31"

  elif (corner_TOPRIGHT == O_MARK or validMove(corner_TOPRIGHT) )and (corner_BOTTOMRIGHT == O_MARK or validMove(corner_BOTTOMRIGHT) ) and (corner_TOPLEFT == O_MARK or validMove(corner_TOPLEFT) ) and (validMove(CENTER) or CENTER == O_MARK):
    if validMove(corner_TOPRIGHT):
      return "H13"
    elif validMove(corner_BOTTOMRIGHT):
      return "H33"
    elif validMove(corner_TOPLEFT ):
      return "H11"
   



  elif (corner_TOPRIGHT == O_MARK or validMove(corner_TOPRIGHT)) and (corner_TOPLEFT == O_MARK or validMove(corner_TOPLEFT)) and (corner_BOTTOMLEFT == O_MARK or validMove(corner_BOTTOMLEFT) ) and (validMove(CENTER) or CENTER == O_MARK) :
    if validMove(corner_TOPRIGHT):
      return "H13"
    elif validMove(corner_TOPLEFT):
      return "H11"
    elif validMove(corner_BOTTOMLEFT):
      return "H31"
    


  elif (corner_TOPLEFT == O_MARK or validMove(corner_TOPLEFT)) and(corner_BOTTOMLEFT == O_MARK or validMove(corner_BOTTOMLEFT)) and(corner_BOTTOMRIGHT == O_MARK or validMove(corner_BOTTOMRIGHT)) and (validMove(CENTER) or CENTER == O_MARK) :
    if validMove(corner_TOPLEFT):
      return "H11"
    elif validMove(corner_BOTTOMLEFT) :
      return "H31"
    elif validMove(corner_BOTTOMRIGHT ):
      return "H33"

  else:  #no trick move available so return -1 to calling function
    return -1
     
  
def isWinHorizontal1():
  '''Function has no parameters and returns true if there is equality between all slots in a winning combination. Else returns false.'''
  if board[0][0] == board[0][1] ==  board[0][2] :
    return True
  else:
    return False

#For the following functions get rid of the parameter and make #three equality checks as we did in isWinHorizontal
def isWinHorizontal2():
  '''Function has no parameters and returns true if there is equality between all slots in a winning combination. Else returns false.'''
  if board[1][0] == board[1][1] == board[1][2]:
    return True
  else:
    return False

def isWinHorizontal3():
  '''Function has no parameters and returns true if there is equality between all slots in a winning combination. Else returns false.'''
  if board[2][0] == board[2][1] == board[2][2]:
      return True
  else:
      return False

def isWinVertical1():  
  '''Function has no parameters and returns true if there is equality between all slots in a winning combination. Else returns false.'''
  if board[0][0] == board[1][0] == board[2][0]:
    return True
  else:
    return False

def isWinVertical2():
  '''Function has no parameters and returns true if there is equality between all slots in a winning combination. Else returns false.'''
  if board[0][1] == board[1][1] == board[2][1]:
    return True
  else:
    return False

def isWinVertical3():
  '''Function has no parameters and returns true if there is equality between all slots in a winning combination. Else returns false.'''
  if board[0][2] == board[1][2] == board[2][2]:
    return True
  else:
    return False

def isWinDiagonal1():
  '''Function has no parameters and returns true if there is equality between all slots in a winning combination. Else returns false.'''
  if board[0][0] == board[1][1] == board[2][2]:
    return True
  else:
    return False

def isWinDiagonal2():
  '''Function has no parameters and returns true if there is equality between all slots in a winning combination. Else returns false.'''
  if board[0][2] == board[1][1] == board[2][0]:
    return True
  else:
    return False


def win(playerorcomp):
  ''' looks if any winning combinations have returned True. takes in a parameter to identify either the player or computer. Returns win if is True'''
  if isWinVertical1() or isWinVertical2() or isWinVertical3() or isWinHorizontal1() or isWinHorizontal2() or isWinHorizontal3() or isWinDiagonal1() or isWinDiagonal2():
    return WIN 

#Check all the slots if there is   
def tie():
  '''looks to see if all pieces of the board is taken, and returns Tie if it does. has no parameters.'''
  if validMove(board[0][0])== False and validMove(board[0][1])== False and validMove(board[0][2])==False  and validMove(board[1][0])==False  and validMove(board[1][1])==False and validMove(board[1][2])==False  and validMove(board[2][0])==False  and validMove(board[2][1])== False  and validMove(board[2][2])== False:
    return TIE


#Check if there is an 'x' or an 'o' already there : If its not there , then its a free slot so return true
def validMove(slot):
  '''looks to see if a slot is free or not. Takes in the parameter slot to identify which slot and returns True if it is free, False if it is not''' 
  if X_MARK == slot or O_MARK == slot:
    return False
  else:
    return True

# take a turn - human player & Computer player logic
# this method will need your modification skills here
def turn(playerXO):
  '''The main turn for either computer or player, which is identified by a parameter. returns loc if loc is 0. Returns win or tie if either player has won or game is tied.'''
  loc = 1 #initial assignment to location    
  # CODE FOR HUMAN PLAYER HERE
  if playerXO == X_MARK : 
    while True :
      data = input("please enter 1-9 to make your move (0 to quit): ")

      while data.isnumeric() == False or data not in ("1","2","3","4","5","6","7","8","9","0"):
          data = input("Error: enter 1-9 to make your move (0 to quit): ")

      loc = int(data)             # the location of the move
      
      if loc == 1:
        if validMove(board[0][0]) == True:
          board[0][0]= playerXO     # the move is played
          break
        else:
          print("Error: this spot is already taken")
      elif loc == 2:
        if validMove(board[0][1]) == True:
          board[0][1]= playerXO
          break
        else:
          print("Error: this spot is already taken")
      elif loc == 3:
        if validMove(board[0][2]) == True:
          board[0][2]= playerXO
          break
        else:
          print("Error: this spot is already taken")

      elif loc == 4:
        if validMove(board[1][0]) == True:
          board[1][0]= playerXO
          break
        else:
          print("Error: this spot is already taken")

      elif loc == 5:
        if validMove(board[1][1]) == True:
          board[1][1]= playerXO
          break
        else:
          print("Error: this spot is already taken")

      elif loc == 6:
        if validMove(board[1][2]) == True:
          board[1][2]= playerXO
          break
        else:
          print("Error: this spot is already taken")

      elif loc == 7:
        if validMove(board[2][0]) == True:
          board[2][0]= playerXO
          break
        else:
          print("Error: this spot is already taken")

      elif loc == 8:
        if validMove(board[2][1]) == True:
          board[2][1]= playerXO
          break
        else:
          print("Error: this spot is already taken")

      elif loc == 9:
        if validMove(board[2][2]) == True:
          board[2][2]= playerXO
          break
        else:
          print("Error: this spot is already taken")

      elif loc == 0 :
        return loc
  else :
    # COMPUTER AI CODE HERE . . .
    print("\nComputers Turn...\n")  
    slot = makeMove()
    makeMyMove(slot)
    #def makeMyMove(slot):
  #2. call the makeMove Function:
      # makeMove() : returns the board position of the computer move
        #1.Block any moves:blockMove():returns -1 if no human winning move to block otherwise move 
        #2.Score a winning move if any:winningMove() : returns -1 if no computer winning move 
        #3.Any trick moves we can score:trickMove() : returns -1 if no tricky move, otherwise move
        #4.Lastly score in any free slot

  #Have they won ?
  if win(playerXO) == WIN :
    return WIN
  if tie() == TIE :
    return TIE

  return loc     # if 0 was entered we need to know because that means to quit









# --------------- The Game -------------------

gamerule = True
while gamerule == True:
  print("""\
    _____ _   _____       _____         
  |_   _(_)_|_   _|_ _ _|_   _|__  ___ 
    | | | / _|| |/ _` / _|| |/ _ \/ -_)
    |_| |_\__||_|\__,_\__||_|\___/\___|""")
  print()
  print("To play enter a position labeled 1 to 9")
  print("Player 1 will be x and Player 2 will be o")
  print()

  setupBoard()
  displayBoard()

  # GAME LOOP .. simple game loop .. make changes here
  player = X_MARK  #X starts first
  result =  turn(player) #dummy value
  while result not in (0, WIN, TIE):
    displayBoard()
    if player == ' x ':     # switch player between moves
        player = ' o '
    else:
        player = ' x '
    
    result =  turn(player)

  if result == 0 :  #the user wants to quit 
    gamerule = False
   

  elif result == WIN or result == TIE:

    #Display the winning/tie game board and inform the user status
    displayBoard()
    if result == TIE :
      print("Its a tie !")
    elif result == WIN :
      if player == X_MARK :
        print("Player has won!")
      else : #player must be omark
        print("Computer has won") 
  
    playagain = input("Would you like to play again? y/Y for yes or n/N for no: ")

    while (playagain.lower() not in ("y" ,"n" )) :
      playagain = input("Please enter a correct input, y/Y for yes or n/N for no: ")
    if playagain == "y" or playagain=="Y":
      gamerule = True
    elif playagain == "N" or playagain=="n":
      gamerule = False
    
  
  


# End GAME LOOP
print()
print("Thank you for playing!")
