import pygame
import random
import time
from QLearning import Qlearning

#humman player
class Humanplayer:
    pass

#randomplayer player
class Randomplayer:
    def __init__(self):
        pass
    def move(self,possiblemoves):
        return random.choice(possiblemoves)

class TicTacToe:
    def __init__(self,traning=False):
        self.board = [' ']*9

        self.done = False
        self.humman=None
        self.computer=None
        self.humanTurn=None
        self.training=traning
        self.player1 = None
        self.player2 = None
        self.aiplayer=None
        self.isAI=False
        # if not training display
        if(not self.training):
            pygame.init()
            self.ttt = pygame.display.set_mode((225,250))
            pygame.display.set_caption('Tic-Tac-Toe')

    #reset the game
    def reset(self):
        if(self.training):
            self.board = [' '] * 9
            return

        self.board = [' '] * 9
        self.humanTurn=random.choice([True,False])

        self.surface = pygame.Surface(self.ttt.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((250, 250, 250))
        #horizontal line
        pygame.draw.line(self.surface, (0, 0, 0), (75, 0), (75, 225), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (150, 0), (150, 225), 2)
        # veritical line
        pygame.draw.line(self.surface, (0, 0, 0), (0,75), (225, 75), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,150), (225, 150), 2)

   #evaluate function
    def evaluate(self, ch):
        # "rows checking"
        for i in range(3):
            if (ch == self.board[i * 3] == self.board[i * 3 + 1] and self.board[i * 3 + 1] == self.board[i * 3 + 2]):
                return 1.0, True
        # "col checking"
        for i in range(3):
            if (ch == self.board[i + 0] == self.board[i + 3] and self.board[i + 3] == self.board[i + 6]):
                return 1.0, True
        # diagonal checking
        if (ch == self.board[0] == self.board[4] and self.board[4] == self.board[8]):
            return 1.0, True

        if (ch == self.board[2] == self.board[4] and self.board[4] == self.board[6]):
            return 1.0, True
        # "if filled draw"
        if not any(c == ' ' for c in self.board):
            return 0.5, True

        return 0.0, False

    #return remaining possible moves
    def possible_moves(self):
        return [moves + 1 for moves, v in enumerate(self.board) if v == ' ']

    #take next step and return reward
    def step(self, isX, move):
        if(isX):
             ch = 'X'
        else:
            ch = '0'
        if(self.board[move-1]!=' '): # try to over write
            return  -5, True

        self.board[move-1]= ch
        reward,done = self.evaluate(ch)
        return reward, done


    #draw move on window
    def drawMove(self, pos,isX):
        row=int((pos-1)/3)
        col=(pos-1)%3

        centerX = ((col) * 75) + 32
        centerY = ((row) * 75) + 32

        reward, done= self.step(isX,pos) #next step
        if(reward==-5): #overlap
            #print('Invalid move')
            font = pygame.font.Font(None, 24)
            text = font.render('Invalid move!', 1, (10, 10, 10))
            self.surface.fill((250, 250, 250), (0, 300, 300, 25))
            self.surface.blit(text, (10, 230))

            return reward, done

        if (isX): #playerX so draw x
            font = pygame.font.Font(None, 24)
            text = font.render('X', 1, (10, 10, 10))
            self.surface.fill((250, 250, 250), (0, 300, 300, 25))
            self.surface.blit(text, (centerX, centerY))
            self.board[pos-1] ='X'

            if(self.humman and reward==1): #if playerX is humman and won, display humman won
                #print('Humman won! in X')
                text = font.render('Humman won!', 1, (10, 10, 10))
                self.surface.fill((250, 250, 250), (0, 300, 300, 25))
                self.surface.blit(text, (10, 230))


            elif (self.computer and reward == 1):#if playerX is computer and won, display computer won
                #print('computer won! in X')
                text = font.render('computer won!', 1, (10, 10, 10))
                self.surface.fill((250, 250, 250), (0, 300, 300, 25))
                self.surface.blit(text, (10, 230))




        else:  #playerO so draw O
            font = pygame.font.Font(None, 24)
            text = font.render('O', 1, (10, 10, 10))

            self.surface.fill((250, 250, 250), (0, 300, 300, 25))
            self.surface.blit(text, (centerX, centerY))
            self.board[pos-1] = '0'

            if (not self.humman and reward == 1):  #if playerO is humman and won, display humman won
                #print('Humman won! in O')
                text = font.render('Humman won!', 1, (10, 10, 10))
                self.surface.fill((250, 250, 250), (0, 300, 300, 25))
                self.surface.blit(text, (10, 230))


            elif (not self.computer and reward == 1):  #if playerO is computer and won, display computer won
                #print('computer won! in O')
                text = font.render('computer won!', 1, (10, 10, 10))
                self.surface.fill((250, 250, 250), (0, 300, 300, 25))
                self.surface.blit(text, (10, 230))



        if (reward == 0.5):  # draw, then display draw
            #print('Draw Game! in O')
            font = pygame.font.Font(None, 24)
            text = font.render('Draw Game!', 1, (10, 10, 10))
            self.surface.fill((250, 250, 250), (0, 300, 300, 25))
            self.surface.blit(text, (10, 230))
            return reward, done

        return reward,done

    # mouseClick position
    def mouseClick(self):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        if (mouseY < 75):
            row = 0
        elif (mouseY < 150):
            row = 1
        else:
            row = 2

        if (mouseX < 75):
            col = 0
        elif (mouseX < 150):
            col = 1
        else:
            col = 2
        return row * 3 + col + 1


     #update state
    def updateState(self,isX):
        pos=self.mouseClick()
        reward,done = self.drawMove(pos,isX)
        return reward, done

    #show display
    def showboard(self):
        self.ttt.blit(self.surface, (0, 0))
        pygame.display.flip()


    #begin training
    def startTraining(self,player1,player2):
        if(isinstance(player1,Qlearning) and isinstance(player2, Qlearning)):
            self.training = True
            self.player1=player1
            self.player2=player2

    #tarin function
    def train(self,iterations):
        if(self.training):
            for i in range(iterations):
                print("trainining", i)
                self.player1.game_begin()
                self.player2.game_begin()
                self.reset()
                done = False
                isX = random.choice([True, False])
                while not done:
                    if isX:
                        move = self.player1.epslion_greedy(self.board, self.possible_moves())
                    else:
                        move = self.player2.epslion_greedy(self.board, self.possible_moves())


                    reward, done = self.step(isX, move)

                    if (reward == 1):  # won
                        if (isX):
                            self.player1.updateQ(reward, self.board, self.possible_moves())
                            self.player2.updateQ(-1 * reward, self.board, self.possible_moves())
                        else:
                            self.player1.updateQ(-1 * reward, self.board, self.possible_moves())
                            self.player2.updateQ(reward, self.board, self.possible_moves())

                    elif (reward == 0.5):  # draw
                        self.player1.updateQ(reward, self.board, self.possible_moves())
                        self.player2.updateQ(reward, self.board, self.possible_moves())


                    elif (reward == -5):  # illegal move
                        if (isX):
                            self.player1.updateQ(reward, self.board, self.possible_moves())
                        else:
                            self.player2.updateQ(reward, self.board, self.possible_moves())

                    elif (reward == 0):
                        if (isX):  # update opposite
                            self.player2.updateQ(reward, self.board, self.possible_moves())
                        else:
                            self.player1.updateQ(reward, self.board, self.possible_moves())

                    isX = not isX  #

    #save Qtables
    def saveStates(self):
        self.player1.saveQtable("player1states")
        self.player2.saveQtable("player2states")


    #start game human vs AI or human vs random
    def startGame(self, playerX, playerO):
        if (isinstance(playerX, Humanplayer)):
            self.humman, self.computer = True, False
            if (isinstance(playerO, Qlearning)): #if AI
                self.ai = playerO
                self.ai.loadQtable("player2states") # load saved Q table
                self.ai.epsilon = 0 #set eps to 0 so always choose greedy step
                self.isAI = True
            elif (isinstance(playerO, Randomplayer)): #if random
                self.ai = playerO
                self.isAI = False

        elif (isinstance(playerO, Humanplayer)):
            self.humman, self.computer = False, True
            if (isinstance(playerX, Qlearning)): #if AI
                self.ai = playerX
                self.ai.loadQtable("player1states") # load saved Q table
                self.ai.epsilon = 0 #set eps to 0 so always choose greedy step
                self.isAI = True
            elif(isinstance(playerX, Randomplayer)):#if random
                self.ai=playerX
                self.isAI = False


    def render(self):
        running = 1
        done = False
        pygame.event.clear()
        while (running == 1):
            if (self.humanTurn): #humman click
                print("Human player turn")
                event = pygame.event.wait()
                while event.type != pygame.MOUSEBUTTONDOWN:
                    event = pygame.event.wait()
                    self.showboard()
                    if event.type == pygame.QUIT:
                        running = 0
                        print("pressed quit")
                        break

                reward, done = self.updateState(self.humman) #if random
                self.showboard()
                if (done): #if done reset
                    time.sleep(1)
                    self.reset()
            else:  #AI or random turn
                if(self.isAI):
                    moves = self.ai.epslion_greedy(self.board, self.possible_moves())
                    reward, done = self.drawMove(moves, self.computer)
                    print("computer's AI player turn")
                    self.showboard()
                else: #random player
                    moves = self.ai.move(self.possible_moves()) #random player
                    reward, done = self.drawMove(moves, self.computer)
                    print("computer's random player turn")
                    self.showboard()

                if (done): #if done reset
                    time.sleep(1)
                    self.reset()

            self.humanTurn = not self.humanTurn




