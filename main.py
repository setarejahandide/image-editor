board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j]==0:
                import random
                new_number=random.randint(1,9)
                #bo[i][j]=new_number
                row=i
                column=j
                #check_the_board
                for i in bo[row]:
                    if i==new_number:
                        valid='no'
                        #bo[row][column]=0
                    else:
                        valid='yes'

    
                if valid=='yes':
                    for i in range(len(bo)):
                        if bo[i][column]==new_number:
                            valid='no'
                        else:
                            valid='yes'
                if valid=='yes':
                    bo[row][column]=new_number
                        
    

find_empty(board)
print(board)


