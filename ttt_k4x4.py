from tkinter import *
from tkinter import messagebox
import time
class app:
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

        self.quarto = Frame(master)
        self.quarto.pack()

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
        
        self.botao4 = Button(self.primeiro,text = ' ',command = lambda : self.set_on_pressed(self.botao4,(0,3)), height = h, width = w)
        self.botao4.pack(side = LEFT)

        self.botao5 = Button(self.segundo,text = ' ',command = lambda : self.set_on_pressed(self.botao5,(1,0)), height = h, width = w)
        self.botao5.pack(side = LEFT)
        
        self.botao6 = Button(self.segundo,text = ' ',command = lambda : self.set_on_pressed(self.botao6,(1,1)), height = h, width = w)
        self.botao6.pack(side = LEFT)

        self.botao7 = Button(self.segundo,text =' ',command = lambda : self.set_on_pressed(self.botao7,(1,2)), height = h, width = w)
        self.botao7.pack(side = LEFT)

        self.botao8 = Button(self.segundo,text = ' ',command = lambda : self.set_on_pressed(self.botao8,(1,3)), height = h, width = w)
        self.botao8.pack(side = LEFT)

        self.botao9 = Button(self.terceiro,text=' ',command = lambda : self.set_on_pressed(self.botao9,(2,0)), height = h, width = w)
        self.botao9.pack(side = LEFT)

        self.botao10 = Button(self.terceiro,text=' ',command = lambda : self.set_on_pressed(self.botao10,(2,1)), height = h, width = w)
        self.botao10.pack(side = LEFT)
        
        self.botao11 = Button(self.terceiro,text=' ',command = lambda : self.set_on_pressed(self.botao11,(2,2)), height = h, width = w)
        self.botao11.pack(side = LEFT)

        self.botao12 = Button(self.terceiro,text=' ',command = lambda : self.set_on_pressed(self.botao12,(2,3)), height = h, width = w)
        self.botao12.pack(side = LEFT)
        '''
        self.botao13 = Button(self.quarto,text=' ',command = lambda : self.set_on_pressed(self.botao13,(3,0)), height = h, width = w)
        self.botao13.pack(side = LEFT)

        self.botao14 = Button(self.quarto,text=' ',command = lambda : self.set_on_pressed(self.botao14,(3,1)), height = h, width = w)
        self.botao14.pack(side = LEFT)

        self.botao15 = Button(self.quarto,text=' ',command = lambda : self.set_on_pressed(self.botao15,(3,2)), height = h, width = w)
        self.botao15.pack(side = LEFT)

        self.botao16 = Button(self.quarto,text=' ',command = lambda : self.set_on_pressed(self.botao16,(3,3)), height = h, width = w)
        self.botao16.pack(side = LEFT)
        '''
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
        self.actual_player = "X"

        self.button_board = [[self.botao1,self.botao2,self.botao3,self.botao4],[self.botao5,self.botao6,self.botao7,self.botao8],[self.botao9,self.botao10,self.botao11,self.botao12]]#,[self.botao13,self.botao14,self.botao15,self.botao16]]
        self.jogada = 0 

        self.pontos_comp = 0 
        self.pontos_player = 0 

    def set_on_pressed(self,button,pos):
        if button['text'] == ' ':
            
            if self.actual_player == 'X':
                
                button['text']='X'
                self.board[pos[0]][pos[1]] = 1
                resultado = self.win_or_tie()
                if resultado[0]:
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
            messagebox.showinfo('Info','Jogada não valida')
    
    def can_be_tie(self,x,iscolumn):
        if iscolumn:
            return x.count(0)<2 and abs(sum(x))<2
        else:
            return x.count(0)<3 and abs(sum(x))<3
    
    def win_or_tie(self):
        
        if self.jogada<=5:
            return True,'_'
        
        tie = []  
        diagonal = []
        diagonal_inv = []
        for i in range(len(self.board)):
            
            coluna = [row[i] for row in self.board]
            linha =self.board[i]
            
            if sum(linha)==4 or sum(coluna)==3:
                return False,"X ganhou"
            elif sum(linha)==-4 or sum(coluna)==-3:
                return False,"O ganhou"
            
            #diagonal.append(self.board[i][i])
            #diagonal_inv.append(self.board[i][len(self.board[i])-1-i])
            
            tie.append(self.can_be_tie(coluna,True))
            tie.append(self.can_be_tie(linha,False))
        
        #if sum(diagonal_inv) == 3 or sum(diagonal)==3 :
        #    return False,"X ganhou"
        
        #elif sum(diagonal_inv)==-3 or sum(diagonal) == -3:
        #    return False,"O ganhou"
        
        #tie.append(self.can_be_tie(diagonal))
        #tie.append(self.can_be_tie(diagonal_inv))
        if all(tie):
            return False,"Empate"
        
        return True,'_'
    
    def clean(self):
        for i in range(len(self.button_board)):
            for j in range(len(self.button_board[0])):
                self.button_board[i][j]['text']=' '
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.actual_player='X'
    
    
    def find_best_pos(self):
        best_score = -10000
        pos = 0
        start_time  = time.time()
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                
                if self.board[i][j]==0:
                    self.board[i][j]=-1
                    score = self.minimax(2,False,2,-2)
                    self.board[i][j] = 0
                    
                    if score > best_score:
                        best_score = score
                        pos = i,j
        
        print(f'O tempo foi de {time.time()-start_time}' )
        
        self.board[pos[0]][pos[1]] = -1

        return pos[0],pos[1]  
    
    def minimax(self,depth,isMaximizing,beta,alpha):
        result = self.win_or_tie()[1]
        is_breaked =False
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
                        score = self.minimax(depth+1,False,beta,alpha)
                        self.jogada-=1
                        self.board[i][j] = 0
                        if score>best_score:
                            best_score = score +10*depth
                            alpha = max(best_score,alpha)
                            if beta<=alpha:
                                is_breaked = True
                                break
                if is_breaked:
                    break
            return best_score
        
        else:
            best_score = 10000
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j]==0:
                        self.board[i][j]= 1
                        self.jogada+=1
                        score = self.minimax(depth+1,True,beta,alpha)
                        self.jogada-=1
                        self.board[i][j] = 0
                        if score<best_score:
                            best_score = score-10*depth 
                            beta = min(beta,best_score)
                            if beta<=alpha:
                                is_breaked = True
                                break 
                    if is_breaked :
                        break
            return best_score     
root = Tk()
app(root)
root.mainloop()