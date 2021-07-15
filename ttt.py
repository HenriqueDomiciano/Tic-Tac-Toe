# starting the board
b1 = """_|_|_\n_|_|_\n | | """
b_inicial = """1|2|3\n4|5|6\n7|8|9"""
print('as posições são :')
print(b_inicial+'\n\n\n')
def find_best_pos(board):
    best_score = -10000
    pos = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                board[i][j]=-1
                score = minimax(board,False)
                board[i][j] = 0
                if score > best_score:
                    best_score = score
                    pos = i,j
    board[pos[0]][pos[1]] = -1
    return board,(pos[0]*3+pos[1]%3)+1  
def minimax(board,isMaximizing):
    if win_or_tie(board)[1]=='O ganhou':
        return 100
    elif win_or_tie(board)[1]=='X ganhou':
        return -100
    elif win_or_tie(board)[1]=='Empate':
        return 0 
    if isMaximizing:
        best_score = -10000
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==0:
                    board[i][j]=-1
                    score = minimax(board,False)
                    board[i][j] = 0
                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = 10000
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==0:
                    board[i][j]= 1
                    score = minimax(board,True)
                    board[i][j] = 0
                    if score < best_score:
                        best_score = score
        return best_score
        
def arruma(bo,pos,lance):
    x_und = 'X'
    O_und = 'O'
    if lance%2==0:
        bo = bo[:(pos-1)*2] + x_und + bo[(pos-1)*2 + 1:]
    else:
        bo = bo[:(pos-1)*2] + O_und + bo[(pos-1)*2 + 1:]
    return bo
def can_be_tie(x):
    return x.count(0)<2 and sum(x)<2
def win_or_tie(b):
    tie = []
    for i in range(len(b)):
        soma =b[i]
        tie.append(can_be_tie(soma))
        if sum(soma)==3:
            return False,"X ganhou",
        elif sum(soma)==-3:
            return False,"O ganhou"
    c=[ list(e) for e in zip(*b)] #transposing the matriz wich represents the game to check columns 
    for j in range(len(c[0])):
        soma = c[j]
        tie.append(can_be_tie(soma))
        if sum(soma) ==3:
            return False,"X ganhou"
        elif sum(soma) == -3:
            return False,"O ganhou"
    soma = []
    for i in range(len(b)):
        soma.append(b[i][i])
    if sum(soma) == 3:
        return False,"X ganhou"
    elif sum(soma) == -3:
        return False,"O ganhou"
    tie.append(can_be_tie(soma))
    soma = []
    for i in range(len(b)):
        soma.append(b[i][len(b[i])-1-i])
    if sum(soma) == 3:
        return False,"X ganhou"
    elif sum(soma) == -3:
        return False,"O ganhou"
    tie.append(can_be_tie(soma))
    if all(tie):
        return False,"Empate"
    return True,'_'    
board = [[0,0,0] for i in range(3)]
lance = 0
is_valid = win_or_tie(board)
while is_valid[0]:
    print(b1)
    if lance == 9:
        print('empatou')
        break
    if lance%2==0:
        posx = int(input('Digite a posição do x'))
        i = (posx-1)//3
        j = (posx%3)-1
        if board[i][j]==0:
            board[i][j]=1
            b1 = arruma(b1,posx,lance)
        else:
            print("Posição invalida digite novamente")
            continue
    else:
        board,posy = find_best_pos(board)
        print(f'O computador jogou {posy}')
        b1 = arruma(b1,posy,lance)
    lance+=1
    is_valid = win_or_tie(board)
print(is_valid[1])
print(b1)