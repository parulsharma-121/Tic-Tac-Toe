positions=['1','2','3','4','5','6','7','8','9']

def game_Board(positions):
    print("  ", positions[0],"|",positions[1],"|",positions[2])
    print("-------------")
    print("  " , positions[3],"|",positions[4],"|",positions[5])
    print("-------------")
    print("  " , positions[6],"|",positions[7],"|",positions[8])


def checkWin(positions):
    isTie = True
    for val in positions:
        if(val!='X' and val!='O'):
            isTie = False
            break 
    
    if(isTie):
        print("Game Draw")
        return True

    if(positions[0]==positions[1] and positions[0]==positions[2]):
        print("Player with ",positions[0], " won")
        return True

    elif(positions[3]==positions[4] and positions[3]==positions[5]):
        print("Player with ",positions[3], " won")
        return True

    elif(positions[6]==positions[7] and positions[6]==positions[8]):
        print("Player with ",positions[6], " won")
        return True

    elif(positions[0]==positions[3] and positions[0]==positions[6]):
        print("Player with ",positions[0], " won")
        return True

    elif(positions[1]==positions[4] and positions[1]==positions[7]):
        print("Player with ",positions[1], " won")
        return True

    elif(positions[2]==positions[5] and positions[2]==positions[8]):
        print("Player with ",positions[2], " won")
        return True

    elif(positions[0]==positions[4] and positions[0]==positions[8]):
        print("Player with ",positions[0], " won")
        return True

    elif(positions[2]==positions[4] and positions[2]==positions[6]):
        print("Player with ",positions[2], " won")
        return True
    else:
        return False

def game_play(positions):  
    print("Player 1 choose the position: ",end="")
    p1 = int(input())-1
    if(positions[p1]!='X' and positions[p1]!='O'):
        positions[p1]='X'
    else:
        print('already occupied')    
    
    game_Board(positions)
    if(checkWin(positions)):
        return True

    print("PLayer 2 choose the position: ",end="")
    p2 = int(input())-1
    if(positions[p2]!='X' and positions[p2]!='O'):
        positions[p2]='O'
    else:
        print('already occupied')
        
   
    game_Board(positions)
    if(checkWin(positions)):
        return True
    
    return False

print("TIC_TAC_TOE")
print("X for player 1 and O for player 2")
game_Board(positions)
while(True):
    if(game_play(positions)):
        break

