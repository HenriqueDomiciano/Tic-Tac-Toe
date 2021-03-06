from tkinter import *
from tkinter import messagebox
import time

class Main:
    def __init__(self,master):
        
        self.master = master

        self.placar = Frame(master)
        self.placar.pack()

        self.zero = Frame(master)
        self.zero.pack()
        
        self.primeiro =Frame(master)
        self.primeiro.pack()
    
        self.segundo = Frame(master)
        self.segundo.pack()
        
        self.terceiro = Frame(master)
        self.terceiro.pack()

        h=10
        w=15
        self.botao_clear = Button(self.zero,text = "Clear",command = self.clean)
        self.botao_clear.pack(side = LEFT)

        self.label_jog = Label(self.zero)
        self.label_jog['text']= f'E a vez do jogador X'
        self.label_jog.pack(side = LEFT)

        self.score = Label(self.placar)

        self.botao1 = Button(self.primeiro,text = ' ',command = lambda : self.set_on_pressed(self.botao1,(0,0)), height = h, width = w)
        self.botao1.pack(side = LEFT)
        
        self.botao2 = Button(self.primeiro,text = ' ',command = lambda : self.set_on_pressed(self.botao2,(0,1)),  height = h, width = w)
        self.botao2.pack(side = LEFT)
        
        self.botao3 = Button(self.primeiro,text = ' ',command = lambda : self.set_on_pressed(self.botao3,(0,2)), height = h, width = w)
        self.botao3.pack(side = LEFT)
        
        self.botao4 = Button(self.segundo,text = ' ',command = lambda : self.set_on_pressed(self.botao4,(1,0)), height = h, width = w)
        self.botao4.pack(side = LEFT)

        self.botao5 = Button(self.segundo,text = ' ',command = lambda : self.set_on_pressed(self.botao5,(1,1)), height = h, width = w)
        self.botao5.pack(side = LEFT)
        
        self.botao6 = Button(self.segundo,text = ' ',command = lambda : self.set_on_pressed(self.botao6,(1,2)), height = h, width = w)
        self.botao6.pack(side = LEFT)

        self.botao7 = Button(self.terceiro,text =' ',command = lambda : self.set_on_pressed(self.botao7,(2,0)), height = h, width = w)
        self.botao7.pack(side = LEFT)

        self.botao8 = Button(self.terceiro,text = ' ',command = lambda : self.set_on_pressed(self.botao8,(2,1)), height = h, width = w)
        self.botao8.pack(side = LEFT)

        self.botao9 = Button(self.terceiro,text=' ',command = lambda : self.set_on_pressed(self.botao9,(2,2)), height = h, width = w)
        self.botao9.pack(side = LEFT)

        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        
        self.actual_player = "X"

        self.button_board = [[self.botao1,self.botao2,self.botao3],[self.botao4,self.botao5,self.botao6],[self.botao7,self.botao8,self.botao9]]
        self.jogada = 0 
        self.iteracoes = 0
        self.pontos_comp = 0 
        self.pontos_player = 0 

    def set_on_pressed(self,button,pos):
        if button['text'] == ' ':
            if self.actual_player == 'X':
                button['text']='X'
                self.board[pos[0]][pos[1]] = 1
                pos0,pos1 = self.find_best_pos()
                self.button_board[pos0][pos1]['text']='O'
                self.jogada+=2
                resultado = self.win_or_tie()
                if not(resultado[0]):
                    ganhador = resultado[1]
                    messagebox.showinfo('Ganhador',f"{ganhador}")
                    if ganhador ==  'X ganhou':
                        self.pontos_player+=1
                    elif ganhador == 'O ganhou':
                        self.pontos_comp +=1
                    self.score['text']=f'Player: {self.pontos_player} ponto(s)         Computador: {self.pontos_comp} ponto(s)'
                    self.score.pack()
                    self.clean()   
        else:
            messagebox.showinfo('Info','Jogada n??o valida')
    def can_be_tie(self,x):
        return list(x).count(0)<2 and sum(x)<2
    def win_or_tie(self):
        tie = []
        for i in range(len(self.board)):
            soma =self.board[i]
            tie.append(self.can_be_tie(soma))
            if sum(soma)==3:
                return False,"X ganhou"
            elif sum(soma)==-3:
                return False,"O ganhou"
        c=[ list(e) for e in zip(*self.board)]  
        for j in range(len(c[0])):
            soma = c[j]
            tie.append(self.can_be_tie(soma))
            if sum(soma) ==3:
                return False,"X ganhou"
            elif sum(soma) == -3:
                return False,"O ganhou"
        soma = []
        for i in range(len(self.board)):
            soma.append(self.board[i][i])
        if sum(soma) == 3:
            return False,"X ganhou"
        elif sum(soma) == -3:
            return False,"O ganhou"
        tie.append(self.can_be_tie(soma))
        soma = []
        for i in range(len(self.board)):
            soma.append(self.board[i][len(self.board[i])-1-i])
        if sum(soma) == 3:
            return False,"X ganhou"
        elif sum(soma) == -3:
            return False,"O ganhou"
        tie.append(self.can_be_tie(soma))
        if all(tie):
            return False,"Empate"
        return True,'_'
    def clean(self):
        self.botao1['text']=' '
        self.botao2['text']=' '
        self.botao3['text']=' '
        self.botao4['text']=' '
        self.botao5['text']=' '
        self.botao6['text']=' '
        self.botao7['text']=' '
        self.botao8['text']=' '
        self.botao9['text']=' '
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.actual_player='X'
    def find_best_pos(self):
        best_score = -10000
        pos = 0
        start_time  = time.time()
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]==0:
                    self.board[i][j]=-1
                    score = self.minimax(False)
                    self.board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        pos = i,j
        print(f'O tempo foi de {time.time()-start_time}' )
        self.board[pos[0]][pos[1]] = -1

        return pos[0],pos[1]  
    def minimax(self,isMaximizing):
        self.iteracoes+=1
        result = self.win_or_tie()[1]
        if result=='O ganhou':
            return 100
        elif result=='X ganhou':
            return -100
        elif result=='Empate':
            return 0 
        if isMaximizing:
            best_score = -10000
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j]==0:
                        self.board[i][j]=-1
                        self.jogada+=1
                        score = self.minimax(False)
                        self.jogada-=1
                        self.board[i][j] = 0
                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 10000
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j]==0:
                        self.board[i][j]= 1
                        self.jogada+=1
                        score = self.minimax(True)
                        self.jogada-=1
                        self.board[i][j] = 0
                        if score < best_score:
                            best_score = score
            return best_score    
root = Tk()
app(root)
root.mainloop()