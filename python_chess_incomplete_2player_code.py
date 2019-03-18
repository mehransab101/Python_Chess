
def main():
    rows=10
    cols=9
    mat=[[(i+1)*(j+1) for j in range(cols)]for i in range(rows)]
    mat[0][0]='0'
    mat[0][1]=mat[1][0]='1'
    mat[0][2]=mat[2][0]='2'
    mat[0][3]=mat[3][0]='3'
    mat[0][4]=mat[4][0]='4'
    mat[0][5]=mat[5][0]='5'
    mat[0][6]=mat[6][0]='6'
    mat[0][7]=mat[7][0]='7'
    mat[0][8]=mat[8][0]='8'#this was the border numbers from 1 to 8
    #----
    #this is the row below the board that has letters A to H
    mat[9][0]='0'
    mat[9][1]='A'
    mat[9][2]='B'
    mat[9][3]='C'
    mat[9][4]='D'
    mat[9][5]='E'
    mat[9][6]='F'
    mat[9][7]='G'
    mat[9][8]='H'
    #----
    mat[2][1]=mat[2][2]=mat[2][3]=mat[2][4]=mat[2][5]=mat[2][6]=mat[2][7]=mat[2][8]='B-P'
    #this is the black pawn first state------------
    mat[7][1]=mat[7][2]=mat[7][3]=mat[7][4]=mat[7][5]=mat[7][6]=mat[7][7]=mat[7][8]='W-P'
    #this is the white pawn first state------------
    mat[3][1]=mat[3][2]=mat[3][3]=mat[3][4]=mat[3][5]=mat[3][6]=mat[3][7]=mat[3][8]=chr(14)
    mat[4][1]=mat[4][2]=mat[4][3]=mat[4][4]=mat[4][5]=mat[4][6]=mat[4][7]=mat[4][8]=chr(14)
    mat[5][1]=mat[5][2]=mat[5][3]=mat[5][4]=mat[5][5]=mat[5][6]=mat[5][7]=mat[5][8]=chr(14)
    mat[6][1]=mat[6][2]=mat[6][3]=mat[6][4]=mat[6][5]=mat[6][6]=mat[6][7]=mat[6][8]=chr(14)
    #this is the first free spaces of the chess board--------------
    mat[1][1]=mat[1][8]='B-R'#black rooks
    mat[8][1]=mat[8][8]='W-R'#white rooks
    #----
    mat[1][2]=mat[1][7]='BKN'#black knight
    mat[8][2]=mat[8][7]='WKN'#white knight
    #----
    mat[1][3]=mat[1][6]='BBI'#black Bishop
    mat[8][3]=mat[8][6]='WBI'#black Bishop
    #----
    mat[1][4]='BQU'#black Queen
    mat[8][4]='WQU'#White Queen
    #----
    mat[1][5]='BKI'#black KING
    mat[8][5]='WKI'#White KING
    
    infinity=True# this is the inifinity loop of the whole chess game!!!
    list_black=[]#black collection of white pieces it has captured
    list_white=[]#white collection of black pieces it has captured
    turn=0
    while infinity==True:
        turn=turn+1#for odd and even numbers
        mod=turn % 2#if (mod=1 turn is 'odd') else ( mod=0 turn is 'even') u can also use('if' mod>0 for odd and 'else' means even)
        #printing the information:
        print('\n')
        print('B-P:Black PAWN/W-P:White PAWN')
        print('B-R:Black ROOK/W-R:White ROOK')
        print('BKN:Black Knight/WKN:White Knight')
        print('BBI:Black Bishop/WBI:White Bishop')
        print('BQU:Black Queen/WQU:White Queen')
        print('BKI:Black King!/WKI:White King!')
        print('\n')
        if mod>0:
            print('-Whites=✓           TURN          -Blacks=')#means that 'turn' is odd number like 1,3,5 ...
        else:
            print('-Whites=           TURN          -Blacks=✓')#means that 'turn' is even number like 2,4,6 ...
        print(' Black Piece:',list_black,' ,')
        print('  -------------------------------------------')
        #print matrix
        for i in range(rows):
            for j in range(cols):
                print('{:>4} '.format(mat[i][j]), end='')
            print()
            print()
        print('  -------------------------------------------')
        print(' White Piece:',list_white,' ,','\n')
        #selecting the coordinates of the piece to move----
        #selecting the piece x and y
        print("select the set that you want to move (first the 'LEFT<' number  then the 'TOP^' number):")
        while True:
            x=int(input("enter the x:"))
            y=int(input("enter the y:"))
            if (x<1 or x>8 or y<1 or y>8): #unspecified numbers in the entry!
                print("Select Between The Range Please!")
                
            if mat[x][y]==chr(14):
                print("that space is empty please choose again!")
                
            if (mod==1 and (mat[x][y]=='B-P' or mat[x][y]=='B-R' or mat[x][y]=='BKN' or mat[x][y]=='BBI' or mat[x][y]=='BQU' or mat[x][y]=='BKI')):#mod=1 means turn is odd which means its whites turn but the players choose black set pieces
                print("its 'whites' turn not black!")
                
                break
        
            elif (mod==0 and (mat[x][y]=='W-P' or mat[x][y]=='W-R' or mat[x][y]=='WKN' or mat[x][y]=='WBI' or mat[x][y]=='WQU' or mat[x][y]=='WKI')):#mod=0 means turn is even which means its black turn but the players choose white set pieces
                print("its 'Blacks' turn not white!")
                
                break
                
            else:
                break
        #
        #selecting the space to move to by x1 and y1
        while True:
            print("Move to:")
            x1=int(input("enter the x1:"))
            y1=int(input("enter the y1:"))
            if (x1<1 or x1>8 or y1<1 or y1>8): #unspecified number entry
                print("Select Between The Range Please!")
            else:
                break


            #for the black pawn !-------------------------------------------------------------for each piece you have to do movements an attacks thats it

        if mat[x][y]=='B-P' and mat[x+1][y]==chr(14) and mat[x+2][y]==chr(14):
            if (x+1==x1 and y==y1) or (x+2==x1 and y==y1) :#and if the selected location(x1,y1) is equal to (x+1,y) or equal (x+2,y) the reason we didnt put mat[x+1][y] ==mat[x1][y1] or mat[x+2][y]==mat[x1][y1] as a condition is that this means you are looking at what is inside the mat[][] rather than the moves that we are looking for.
                mat[x1][y1]=mat[x][y]#move to new location
                mat[x][y]=chr(14)#empty the last location
            else:#means that the selected space isnt available for the black pawn
                print("you cannot do this action")
        #if the black pawn that you want to move isnt on the initial coordinates?we only need to look at the x to know this
        if mat[x][y]=='B-P' and mat[x+1][y]==chr(14) and x!=2:#x!=2
            if (x+1==x1 and y==y1):#its not initial coordiates then we can only move the pawn once forward
                mat[x1][y1]=mat[x][y]#move to new location
                mat[x][y]=chr(14)#empty the last location
            else:
                print("you cannot do this action")
        #for attack front left
        if (mat[x][y]=='B-P') and (mat[x+1][y-1]=='W-P' or mat[x+1][y-1]=='W-R' or mat[x+1][y-1]=='WKN' or mat[x+1][y-1]=='WBI' or mat[x+1][y-1]=='WQU'):
            if (x+1==x1 and y-1==y1):
                list_black.append(mat[x1][y1])
                mat[x1][y1]=mat[x][y]
                mat[x][y]=chr(14)
        #for attack front right
        if (mat[x][y]=='B-P') and (mat[x+1][y+1]=='W-P' or mat[x+1][y+1]=='W-R' or mat[x+1][y+1]=='WKN' or mat[x+1][y+1]=='WBI' or mat[x+1][y+1]=='WQU'):
            if (x+1==x1 and y+1==y1):
                list_black.append(mat[x1][y1])
                mat[x1][y1]=mat[x][y]
                mat[x][y]=chr(14)

        #for attacking the king!
        if (mat[x][y]=='B-P') and (mat[x+1][y+1]=='WKI' or mat[x+1][y-1]=='WKI'):
            if (x+1==x1 and y+1==y1):#king be on the right side front
                print('\n',"**Check! for the white king!**")
            elif(x+1==x1 and y-1==y1):#king be on the left side front
                print('\n',"**Check for the white king!**")
        
        #for the white pawn -------------------------------------------------------------------------------------------------------------------
        #if the selectedpiece is a White pawn!
        if mat[x][y]=='W-P' and mat[x-1][y]==chr(14) and mat[x-2][y]==chr(14):
            if (x-1==x1 and y==y1) or (x-2==x1 and y==y1):
                mat[x1][y1]=mat[x][y]
                mat[x][y]=chr(14)
            else:
                print("you cannot do this action")

        #if the white pawn that you want to move isnt on the initial coordinates?we only need to look at the x to know this
        if mat[x][y]=='W-P' and mat[x-1][y]==chr(14) and x!=7:#x!=7
            if (x-1==x1 and y==y1):#its not initial coordiates then we can only move the pawn once forward
                mat[x1][y1]=mat[x][y]#move to new location
                mat[x][y]=chr(14)#empty the last location
            else:
                print("you cannot do this action")
        #for attack front left
        if (mat[x][y]=='W-P') and (mat[x-1][y-1]=='B-P' or mat[x-1][y-1]=='B-R' or mat[x-1][y-1]=='BKN' or mat[x-1][y-1]=='BBI' or mat[x-1][y-1]=='BQU'):
            if (x-1==x1 and y-1==y1):
                list_white.append(mat[x1][y1])
                mat[x1][y1]=mat[x][y]
                mat[x][y]=chr(14)
        #for attack front right
        if (mat[x][y]=='W-P') and (mat[x-1][y+1]=='B-P' or mat[x-1][y+1]=='B-R' or mat[x-1][y+1]=='BKN' or mat[x-1][y+1]=='BBI' or mat[x-1][y+1]=='BQU'):
            if (x-1==x1 and y+1==y1):
                list_white.append(mat[x1][y1])
                mat[x1][y1]=mat[x][y]
                mat[x][y]=chr(14)

        #for attacking the king!
        if (mat[x][y]=='W-P') and (mat[x-1][y+1]=='BKI' or mat[x-1][y-1]=='BKI'):
            if (x-1==x1 and y+1==y1):#king be on the right side front
                print('\n',"**Check! for the black king!**")
            elif(x-1==x1 and y-1==y1):#king be on the left side front
                print('\n',"**Check for the black king!**")


        #for the black ROOK (B-R)!----------------------------------------------------------------------------------------------------------
        if mat[x][y]=='B-R' and (y==y1 or x==x1): #y==y1 or x==x1 means exactly the mmovement of the ROOK
            if x<x1:#searching downwards
                for item in range(x+1, x1+1): #x1 isnt included so we use +1
                    mat[x][y]=chr(14)
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y1]='B-R'
                        mat[item-1][y]=chr(14)#delete the last box
                                                
                    elif (mat[item][y]==chr(14)):
                        mat[item][y]='B-R'
                        mat[item-1][y]=chr(14)#deleting the last box
                        continue
                    elif (mat[item][y]=='WKI'):#check
                        print('Check! for the white king')
                        break
                    else:
                        mat[item-1][y]='B-R'#you find your own pieces in the board and you stay just before them
                        
                            #--------------
            if x>x1:#searching upwards!                
                for item in range(x-1, x1-1, -1): #from x-1 to x1-1(because it stops before x1 so we -1 so its exacly x1) == range(start , stop ,step)
                    mat[x][y]=chr(14)
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='B-R'
                        mat[item+1][y]=chr(14)
                                                
                    elif (mat[item][y]==chr(14)):
                        mat[item][y]='B-R'
                        mat[item+1][y]=chr(14)#deleting the last box
                        continue
                    elif mat[item][y]=='WKI':#check for the white king!
                        print('Check! for the white king')
                        break
                    else:#means the set piece in front is your own
                        mat[item+1][y]='B-R'#you find your own pieces in the board and you stay just before them
                        
            if y>y1:#searching left wards
                for item in range(y-1, y1-1, -1):
                    mat[x][y]=chr(14)
                    if (mat[x][item]=='W-P' or mat[x][item]=='W-R' or mat[x][item]=='WKN' or mat[x][item]=='WBI' or mat[x][item]=='WQU'):
                        list_black.append(mat[x][item])
                        mat[x][item]='B-R'
                        mat[x][item+1]=chr(14)#delete the last box it has hit from the enemy sets
                        
                    elif (mat[x][item]==chr(14)):
                        mat[x][item]='B-R'
                        mat[x][item+1]=chr(14)#deleting the last box in moved on
                        continue
                    elif mat[x][item]=='WKI':#check for the white king!
                        print('Check! for the white king')
                        break
                    else:
                        mat[x][item+1]='B-R'#finding own set peices
                        
                               

            if y<y1:#searching right wards                
                for item in range(y+1, y1+1, +1):
                    mat[x][y]=chr(14)
                    if (mat[x][item]=='W-P' or mat[x][item]=='W-R' or mat[x][item]=='WKN' or mat[x][item]=='WBI' or mat[x][item]=='WQU'):
                        list_black.append(mat[x][item])
                        mat[x][item]='B-R'
                        mat[x][item-1]=chr(14)#delete the last box it has hit from the enemy sets
                        
                    elif (mat[x][item]==chr(14)):                        
                        mat[x][item]='B-R'
                        mat[x][item-1]=chr(14)#deleting the last box in searching rightwards
                        continue
                    elif mat[x][item]=='WKI':#check for the white king!
                        print('Check! for the white king')
                        break
                    else:
                        mat[x][item-1]='B-R'#finding own set peices
                        
        #for the white ROOK (W-R)!------------------------------------------------------------------------------------------------------
        if mat[x][y]=='W-R' and (y==y1 or x==x1): #y==y1 or x==x1 means exactly the mmovement of the ROOK
            if x<x1:#searching downwards
                for item in range(x+1, x1+1): #x1 isnt included so we use +1
                    mat[x][y]=chr(14)
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y1]='W-R'
                        mat[item-1][y]=chr(14)#delete the last box
                                                
                    elif (mat[item][y]==chr(14)):
                        mat[item][y]='W-R'
                        mat[item-1][y]=chr(14)#deleting the last box
                        continue
                    elif (mat[item][y]=='BKI'):#check
                        print('Check! for the black king')
                        break
                    else:
                        mat[item-1][y]='W-R'#you find your own pieces in the board and you stay just before them
                        
                            #--------------
            if x>x1:#searching upwards!                
                for item in range(x-1, x1-1, -1): #from x-1 to x1-1(because it stops before x1 so we -1 so its exacly x1) == range(start , stop ,step)
                    mat[x][y]=chr(14)
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='W-R'
                        mat[item+1][y]=chr(14)
                                                
                    elif (mat[item][y]==chr(14)):
                        mat[item][y]='W-R'
                        mat[item+1][y]=chr(14)#deleting the last box
                        continue
                    elif mat[item][y]=='BKI':#check for the black king!
                        print('Check! for the black king')
                        break
                    else:#means the set piece in front is your own
                        mat[item+1][y]='W-R'#you find your own pieces in the board and you stay just before them
                        
            if y>y1:#searching left wards
                for item in range(y-1, y1-1, -1):
                    mat[x][y]=chr(14)
                    if (mat[x][item]=='B-P' or mat[x][item]=='B-R' or mat[x][item]=='BKN' or mat[x][item]=='BBI' or mat[x][item]=='BQU'):
                        list_white.append(mat[x][item])
                        mat[x][item]='W-R'
                        mat[x][item+1]=chr(14)#delete the last box it has hit from the enemy sets
                        
                    elif (mat[x][item]==chr(14)):
                        mat[x][item]='W-R'
                        mat[x][item+1]=chr(14)#deleting the last box in moved on
                        continue
                    elif mat[x][item]=='BKI':#check for the black king!
                        print('Check! for the black king')
                        break
                    else:
                        mat[x][item+1]='W-R'#finding own set peices
                        
                               

            if y<y1:#searching right wards                
                for item in range(y+1, y1+1, +1):
                    mat[x][y]=chr(14)
                    if (mat[x][item]=='B-P' or mat[x][item]=='B-R' or mat[x][item]=='BKN' or mat[x][item]=='BBI' or mat[x][item]=='BQU'):
                        list_white.append(mat[x][item])
                        mat[x][item]='W-R'
                        mat[x][item-1]=chr(14)#delete the last box it has hit from the enemy sets
                        
                    elif (mat[x][item]==chr(14)):                        
                        mat[x][item]='W-R'
                        mat[x][item-1]=chr(14)#deleting the last box in searching rightwards
                        continue
                    elif mat[x][item]=='BKI':#check for the black king!
                        print('Check! for the black king')
                        break
                    else:
                        mat[x][item-1]='W-R'#finding own set peices


        #for black Knight--------------------------------------------------------------------
        if mat[x][y]=='BKN':
            if ((x-1==x1 and y-2==y1) or (x-2==x1 and y-1==y1) or (x-2==x1 and y+1==y1) or (x-1==x1 and y+2==y1) or (x+1==x1 and y-2==y1) or (x+2==x1 and y-1==y1) or (x+1==x1 and y+2==y1) or (x+2==x1 and y+1==y1)) and mat[x1][y1]==chr(14) :
                mat[x][y]=chr(14)
                mat[x1][y1]='BKN'
                
            if (mat[x1][y1]=='W-P' or mat[x1][y1]=='W-R' or mat[x1][y1]=='WKN' or mat[x1][y1]=='WBI' or mat[x1][y1]=='WQU'):#for attack
                list_black.append(mat[x1][y1])
                mat[x][y]=chr(14)
                mat[x1][y1]='BKN'
                
            elif (mat[x1][y1]=='WKI'):#for the king
                print("check for the white king!")
                break
            
        #for white knight--------------------------------------------------------------------
        if mat[x][y]=='WKN':
            if ((x-1==x1 and y-2==y1) or (x-2==x1 and y-1==y1) or (x-2==x1 and y+1==y1) or (x-1==x1 and y+2==y1) or (x+1==x1 and y-2==y1) or (x+2==x1 and y-1==y1) or (x+1==x1 and y+2==y1) or (x+2==x1 and y+1==y1)) and mat[x1][y1]==chr(14) :
                mat[x][y]=chr(14)
                mat[x1][y1]='WKN'
                
            if (mat[x1][y1]=='B-P' or mat[x1][y1]=='B-R' or mat[x1][y1]=='BKN' or mat[x1][y1]=='BBI' or mat[x1][y1]=='BQU'):#for attack
                list_white.append(mat[x1][y1])
                mat[x][y]=chr(14)
                mat[x1][y1]='WKN'
                
            elif (mat[x1][y1]=='BKI'):#for the king
                print("check for the black king!")
                break

        #for black Bishop!----------------------------------------------------------
        if mat[x][y]=='BBI':
            if (x1>x and y1<y ):#searching downleft wards
                mat[x][y]=chr(14)
                for item in range(x+1, x1+1, +1):       #x1+1 is for the              
                    y=y-1
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BBI'
                        mat[item-1][y+1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):#before mat[item][y]==chr(14)
                        mat[item][y]='BBI' #mat[item][y]='BBI'
                        mat[item-1][y+1]=chr(14)#mat[item-1][y+1]=chr(14)
                        
                    elif (mat[item][y]=='WKI'):
                        print('check for the white king!')
                        break
                    elif (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BKI' or mat[item][y]=='BQU'):
                        print("You Cant Hit Your Own Pieces!") #the selected space is filled with your own pieces
                        mat[item-1][y+1]='BBI'
                        continue      
                    
            #-------------
            if (x1<x and y1>y ):#searching up right wards
                mat[x][y]=chr(14)
                for item in range(x-1, x1-1, -1):
                    y=y+1
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BBI'
                        mat[item+1][y-1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):#look
                        mat[item][y]='BBI'
                        mat[item+1][y-1]=chr(14)
                        
                    elif (mat[item][y]=='WKI'):
                        print('check the white king!')
                        break
                    elif (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BKI' or mat[item][y]=='BQU'):
                        print("You Cant Hit Your Own Pieces!")
                        mat[item+1][y-1]='BBI'
                        
                        continue
                        
            #-------------
            if (x1>x and y1>y):#searching down right wards
                mat[x][y]=chr(14)
                for item in range(x+1, x1+1, +1):
                    y=y+1
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BBI'
                        mat[item-1][y-1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='BBI'
                        mat[item-1][y-1]=chr(14)
                        
                    elif (mat[item][y]=='WKI'):
                        print('check the white king!')
                        break
                    
                    elif (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BKI' or mat[item][y]=='BQU'):
                        
                        print("You Cant Hit Your Own Pieces!")
                        mat[item-1][y-1]='BBI'
                        continue
                        

            #-----------
            if (x1<x and y1<y):#searching up left wards
                mat[x][y]=chr(14)
                for item in range(x-1, x1-1, -1):
                    y=y-1
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BBI'
                        mat[item+1][y+1]=chr(14)#delete the one before
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='BBI'
                        mat[item+1][y+1]=chr(14)#delete the one before
                        
                    elif (mat[item][y]=='WKI'):
                        print('check the white king!')
                        break
                    elif (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BKI' or mat[item][y]=='BQU'):
                        print("You Cant Hit Your Own Pieces!")
                        mat[item+1][y+1]='BBI'
                        continue
                    
        #for White Bishop!----------------------------------------------------------
        if mat[x][y]=='WBI':
            if (x1>x and y1<y ):#searching downleft wards
                mat[x][y]=chr(14)
                for item in range(x+1, x1+1, +1):       #x1+1 is for the              
                    y=y-1
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WBI'
                        mat[item-1][y+1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):#before mat[item][y]==chr(14)
                        mat[item][y]='WBI' #mat[item][y]='BBI'
                        mat[item-1][y+1]=chr(14)#mat[item-1][y+1]=chr(14)
                        
                    elif (mat[item][y]=='BKI'):
                        print('check for the Black king!')
                        break
                    elif (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WKI' or mat[item][y]=='WQU'):
                        print("You Cant Hit Your Own Pieces!") #the selected space is filled with your own pieces
                        mat[item-1][y+1]='WBI'
                        continue      
                    
            #-------------
            if (x1<x and y1>y ):#searching up right wards
                mat[x][y]=chr(14)
                for item in range(x-1, x1-1, -1):
                    y=y+1
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WBI'
                        mat[item+1][y-1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):#look
                        mat[item][y]='WBI'
                        mat[item+1][y-1]=chr(14)
                        
                    elif (mat[item][y]=='BKI'):
                        print('check the Black king!')
                        break
                    elif (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WKI' or mat[item][y]=='WQU'):
                        print("You Cant Hit Your Own Pieces!")
                        mat[item+1][y-1]='WBI'
                        continue
                        
            #-------------
            if (x1>x and y1>y):#searching down right wards
                mat[x][y]=chr(14)
                for item in range(x+1, x1+1, +1):
                    y=y+1
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WBI'
                        mat[item-1][y-1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='WBI'
                        mat[item-1][y-1]=chr(14)
                        
                    elif (mat[item][y]=='BKI'):
                        print('check the black king!')
                        break
                    
                    elif (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WKI' or mat[item][y]=='WQU'):
                        
                        print("You Cant Hit Your Own Pieces!")
                        mat[item-1][y-1]='WBI'
                        continue
                        

            #-----------
            if (x1<x and y1<y):#searching up left wards
                mat[x][y]=chr(14)
                for item in range(x-1, x1-1, -1):
                    y=y-1
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WBI'
                        mat[item+1][y+1]=chr(14)#delete the one before
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='WBI'
                        mat[item+1][y+1]=chr(14)#delete the one before
                        
                    elif (mat[item][y]=='BKI'):
                        print('check the black king!')
                        break
                    elif (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WKI' or mat[item][y]=='WQU'):
                        print("You Cant Hit Your Own Pieces!")
                        mat[item+1][y+1]='WBI'
                        continue
                    
        #For The Black Queen!--------------------------------------
        if mat[x][y]=='BQU':
            if (x1>x and y1<y ):#searching downleft wards
                mat[x][y]=chr(14)
                for item in range(x+1, x1+1, +1):       #x1+1 is for the              
                    y=y-1
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BQU'
                        mat[item-1][y+1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):#before mat[item][y]==chr(14)
                        mat[item][y]='BQU' #mat[item][y]='BBI'
                        mat[item-1][y+1]=chr(14)#mat[item-1][y+1]=chr(14)
                        
                    elif (mat[item][y]=='WKI'):
                        print('check for the white king!')
                        break
                    elif (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BKI'):
                        print("You Cant Hit Your Own Pieces!") #the selected space is filled with your own pieces
                        mat[item-1][y+1]='BQU'
                        continue      
                    
            #-------------
            if (x1<x and y1>y ):#searching up right wards
                mat[x][y]=chr(14)
                for item in range(x-1, x1-1, -1):
                    y=y+1
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BQU'
                        mat[item+1][y-1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):#look
                        mat[item][y]='BQU'
                        mat[item+1][y-1]=chr(14)
                        
                    elif (mat[item][y]=='WKI'):
                        print('check the white king!')
                        break
                    elif (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BKI'):
                        print("You Cant Hit Your Own Pieces!")
                        mat[item+1][y-1]='BQU'
                        
                        continue
                        
            #-------------
            if (x1>x and y1>y):#searching down right wards
                mat[x][y]=chr(14)
                for item in range(x+1, x1+1, +1):
                    y=y+1
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BQU'
                        mat[item-1][y-1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='BQU'
                        mat[item-1][y-1]=chr(14)
                        
                    elif (mat[item][y]=='WKI'):
                        print('check the white king!')
                        break
                    
                    elif (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BKI'):
                        
                        print("You Cant Hit Your Own Pieces!")
                        mat[item-1][y-1]='BQU'
                        continue
                        

            #-----------
            if (x1<x and y1<y):#searching up left wards
                mat[x][y]=chr(14)
                for item in range(x-1, x1-1, -1):
                    y=y-1
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BQU'
                        mat[item+1][y+1]=chr(14)#delete the one before
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='BQU'
                        mat[item+1][y+1]=chr(14)#delete the one before
                                            
                    elif (mat[item][y]=='WKI'):
                        print('check the white king!')
                        break
                    elif (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BKI'):
                        print("You Cant Hit Your Own Pieces!")
                        mat[item+1][y+1]='BQU'
                        continue

            #----------------searching left, right, up, down
            if (x<x1 and y==y1 and mat[x1][y1]!='BQU'):#searching downwards and the goal matrix isnt moved meaning the last 4 if has not occured
                for item in range(x+1, x1+1): #x1 isnt included so we use +1
                    mat[x][y]=chr(14)
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y1]='BQU'
                        mat[item-1][y]=chr(14)#delete the last box
                                                
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='BQU'
                        mat[item-1][y]=chr(14)#deleting the last box
                        continue
                    elif (mat[item][y]=='WKI'):#check
                        print('Check! for the white king')
                        break
                    else:
                        mat[item-1][y]='BQU'#you find your own pieces in the board and you stay just before them
                        
                            #--------------
            if (x>x1 and y==y1 and mat[x1][y1]!='BQU'):#searching upwards! and the goal matrix isnt moved meaning the last 4 if has not occured               
                for item in range(x-1, x1-1, -1): #from x-1 to x1-1(because it stops before x1 so we -1 so its exacly x1) == range(start , stop ,step)
                    mat[x][y]=chr(14)
                    if (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WQU'):
                        list_black.append(mat[item][y])
                        mat[item][y]='BQU'
                        mat[item+1][y]=chr(14)
                                                
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='BQU'
                        mat[item+1][y]=chr(14)#deleting the last box
                        continue
                    elif mat[item][y]=='WKI':#check for the white king!
                        print('Check! for the white king')
                        break
                    else:#means the set piece in front is your own
                        mat[item+1][y]='BQU'#you find your own pieces in the board and you stay just before them
                        
            if (y>y1 and x==x1 and mat[x1][y1]!='BQU'):#searching left wards and the goal matrix isnt moved meaning the last 4 if has not occured
                for item in range(y-1, y1-1, -1):
                    mat[x][y]=chr(14)
                    if (mat[x][item]=='W-P' or mat[x][item]=='W-R' or mat[x][item]=='WKN' or mat[x][item]=='WBI' or mat[x][item]=='WQU'):
                        list_black.append(mat[x][item])
                        mat[x][item]='BQU'
                        mat[x][item+1]=chr(14)#delete the last box it has hit from the enemy sets
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[x][item]='BQU'
                        mat[x][item+1]=chr(14)#deleting the last box in moved on
                        continue
                    elif mat[x][item]=='WKI':#check for the white king!
                        print('Check! for the white king')
                        break
                    else:
                        mat[x][item+1]='BQU'#finding own set peices
                        
                               

            if (y<y1 and x==x1 and mat[x1][y1]!='BQU'):#searching right wards and the goal matrix isnt moved meaning the last 4 if has not occured               
                for item in range(y+1, y1+1, +1):
                    mat[x][y]=chr(14)
                    if (mat[x][item]=='W-P' or mat[x][item]=='W-R' or mat[x][item]=='WKN' or mat[x][item]=='WBI' or mat[x][item]=='WQU'):
                        list_black.append(mat[x][item])
                        mat[x][item]='BQU'
                        mat[x][item-1]=chr(14)#delete the last box it has hit from the enemy sets
                        
                    elif (mat[x1][y1]==chr(14)):                        
                        mat[x][item]='BQU'
                        mat[x][item-1]=chr(14)#deleting the last box in searching rightwards
                        continue
                    elif mat[x][item]=='WKI':#check for the white king!
                        print('Check! for the white king')
                        break
                    else:
                        mat[x][item-1]='BQU'#finding own set peices
                        
        #For The White Queen!--------------------------------------
        if mat[x][y]=='WQU':
            if (x1>x and y1<y ):#searching downleft wards
                mat[x][y]=chr(14)
                for item in range(x+1, x1+1, +1):       #x1+1 is for the              
                    y=y-1
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WQU'
                        mat[item-1][y+1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):#before mat[item][y]==chr(14)
                        mat[item][y]='WQU' #mat[item][y]='BBI'
                        mat[item-1][y+1]=chr(14)#mat[item-1][y+1]=chr(14)
                        
                    elif (mat[item][y]=='BKI'):
                        print('check for the Black king!')
                        break
                    elif (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WKI'):
                        print("You Cant Hit Your Own Pieces!") #the selected space is filled with your own pieces
                        mat[item-1][y+1]='WQU'
                        continue      
                    
            #-------------
            if (x1<x and y1>y ):#searching up right wards
                mat[x][y]=chr(14)
                for item in range(x-1, x1-1, -1):
                    y=y+1
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WQU'
                        mat[item+1][y-1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):#look
                        mat[item][y]='WQU'
                        mat[item+1][y-1]=chr(14)
                        
                    elif (mat[item][y]=='BKI'):
                        print('check the black king!')
                        break
                    elif (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WKI'):
                        print("You Cant Hit Your Own Pieces!")
                        mat[item+1][y-1]='WQU'
                        
                        continue
                        
            #-------------
            if (x1>x and y1>y):#searching down right wards
                mat[x][y]=chr(14)
                for item in range(x+1, x1+1, +1):
                    y=y+1
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WQU'
                        mat[item-1][y-1]=chr(14)
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='WQU'
                        mat[item-1][y-1]=chr(14)
                        
                    elif (mat[item][y]=='BKI'):
                        print('check the black king!')
                        break
                    
                    elif (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WKI'):
                        
                        print("You Cant Hit Your Own Pieces!")
                        mat[item-1][y-1]='WQU'
                        continue
                        

            #-----------
            if (x1<x and y1<y):#searching up left wards
                mat[x][y]=chr(14)
                for item in range(x-1, x1-1, -1):
                    y=y-1
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WQU'
                        mat[item+1][y+1]=chr(14)#delete the one before
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='WQU'
                        mat[item+1][y+1]=chr(14)#delete the one before
                                            
                    elif (mat[item][y]=='BKI'):
                        print('check the black king!')
                        break
                    elif (mat[item][y]=='W-P' or mat[item][y]=='W-R' or mat[item][y]=='WKN' or mat[item][y]=='WBI' or mat[item][y]=='WKI'):
                        print("You Cant Hit Your Own Pieces!")
                        mat[item+1][y+1]='WQU'
                        continue

            #----------------searching left, right, up, down
            if (x<x1 and y==y1 and mat[x1][y1]!='WQU'):#searching downwards and the goal matrix isnt moved meaning the last 4 if has not occured
                for item in range(x+1, x1+1): #x1 isnt included so we use +1
                    mat[x][y]=chr(14)
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y1]='WQU'
                        mat[item-1][y]=chr(14)#delete the last box
                                                
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='WQU'
                        mat[item-1][y]=chr(14)#deleting the last box
                        continue
                    elif (mat[item][y]=='BKI'):#check
                        print('Check! for the black king')
                        break
                    else:
                        mat[item-1][y]='WQU'#you find your own pieces in the board and you stay just before them
                        
                            #--------------
            if (x>x1 and y==y1 and mat[x1][y1]!='WQU'):#searching upwards! and the goal matrix isnt moved meaning the last 4 if has not occured               
                for item in range(x-1, x1-1, -1): #from x-1 to x1-1(because it stops before x1 so we -1 so its exacly x1) == range(start , stop ,step)
                    mat[x][y]=chr(14)
                    if (mat[item][y]=='B-P' or mat[item][y]=='B-R' or mat[item][y]=='BKN' or mat[item][y]=='BBI' or mat[item][y]=='BQU'):
                        list_white.append(mat[item][y])
                        mat[item][y]='WQU'
                        mat[item+1][y]=chr(14)
                                                
                    elif (mat[x1][y1]==chr(14)):
                        mat[item][y]='WQU'
                        mat[item+1][y]=chr(14)#deleting the last box
                        continue
                    elif mat[item][y]=='BKI':#check for the white king!
                        print('Check! for the black king')
                        break
                    else:#means the set piece in front is your own
                        mat[item+1][y]='WQU'#you find your own pieces in the board and you stay just before them
                        
            if (y>y1 and x==x1 and mat[x1][y1]!='WQU'):#searching left wards and the goal matrix isnt moved meaning the last 4 if has not occured
                for item in range(y-1, y1-1, -1):
                    mat[x][y]=chr(14)
                    if (mat[x][item]=='B-P' or mat[x][item]=='B-R' or mat[x][item]=='BKN' or mat[x][item]=='BBI' or mat[x][item]=='BQU'):
                        list_white.append(mat[x][item])
                        mat[x][item]='WQU'
                        mat[x][item+1]=chr(14)#delete the last box it has hit from the enemy sets
                        
                    elif (mat[x1][y1]==chr(14)):
                        mat[x][item]='WQU'
                        mat[x][item+1]=chr(14)#deleting the last box in moved on
                        continue
                    elif mat[x][item]=='BKI':#check for the white king!
                        print('Check! for the black king')
                        break
                    else:
                        mat[x][item+1]='WQU'#finding own set peices
                        
                               

            if (y<y1 and x==x1 and mat[x1][y1]!='WQU'):#searching right wards and the goal matrix isnt moved meaning the last 4 if has not occured               
                for item in range(y+1, y1+1, +1):
                    mat[x][y]=chr(14)
                    if (mat[x][item]=='B-P' or mat[x][item]=='B-R' or mat[x][item]=='BKN' or mat[x][item]=='BBI' or mat[x][item]=='BQU'):
                        list_white.append(mat[x][item])
                        mat[x][item]='WQU'
                        mat[x][item-1]=chr(14)#delete the last box it has hit from the enemy sets
                        
                    elif (mat[x1][y1]==chr(14)):                        
                        mat[x][item]='WQU'
                        mat[x][item-1]=chr(14)#deleting the last box in searching rightwards
                        continue
                    elif mat[x][item]=='BKI':#check for the white king!
                        print('Check! for the black king')
                        break
                    else:
                        mat[x][item-1]='WQU'#finding own set peices
                        
        #for the black KING!---------------------
        if mat[x][y]=='BKI':
            if (((x-1==x1 and y==y1) or (x-1==x1 and y-1==y1) or (x==x1 and y-1==y1) or (x+1==x1 and y-1==y1) or (x+1==x1 and y==y1) or (x+1==x1 and y+1==y1) or (x==x1 and y+1==y1) or (x-1==x1 and y+1==y1)) and mat[x1][y1]==chr(14)):
                mat[x][y]=chr(14)
                mat[x1][y1]='BKI'
                
            if (mat[x1][y1]=='W-P' or mat[x1][y1]=='W-R' or mat[x1][y1]=='WKN' or mat[x1][y1]=='WBI' or mat[x1][y1]=='WQU'):#for attack
                list_black.append(mat[x1][y1])
                mat[x][y]=chr(14)
                mat[x1][y1]='BKI'
                
            if (mat[x1][y1]=='B-P' or mat[x1][y1]=='B-R' or mat[x1][y1]=='BKN' or mat[x1][y1]=='BBI' or mat[x1][y1]=='BQU'):#for own pieces
                print("those are yours!")
                
            if (mat[x1][y1]=='WKI'):
                print("check for the White king!")
                break
            else:
                print("you cant do that!")
                
        #for the White KING!---------------------
        if mat[x][y]=='WKI':
            if (((x-1==x1 and y==y1) or (x-1==x1 and y-1==y1) or (x==x1 and y-1==y1) or (x+1==x1 and y-1==y1) or (x+1==x1 and y==y1) or (x+1==x1 and y+1==y1) or (x==x1 and y+1==y1) or (x-1==x1 and y+1==y1)) and mat[x1][y1]==chr(14)):
                mat[x][y]=chr(14)
                mat[x1][y1]='WKI'
                
            if (mat[x1][y1]=='B-P' or mat[x1][y1]=='B-R' or mat[x1][y1]=='BKN' or mat[x1][y1]=='BBI' or mat[x1][y1]=='BQU'):#for attacks
                list_white.append(mat[x1][y1])
                mat[x][y]=chr(14)
                mat[x1][y1]='WKI'

            if (mat[x1][y1]=='W-P' or mat[x1][y1]=='W-R' or mat[x1][y1]=='WKN' or mat[x1][y1]=='WBI' or mat[x1][y1]=='WQU'):#for own pieces
                print("those are yours!")
                
            if (mat[x1][y1]=='BKI'):
                print("check for the black king!")
                break
            else:
                print("You cant do that")
                
                        
       
        #------------below must be editted-------------
                
        

main()
        
