from Game import TicTacToe, Humanplayer, Randomplayer
from QLearning import  Qlearning

game = TicTacToe() #game instance
player1=Humanplayer() #human player
player2=Randomplayer()  #agent
game.startGame(player1,player2)#player1 is X, player2 is 0
game.reset() #reset
game.render() # render display

