from Game import TicTacToe
from QLearning import  Qlearning

game = TicTacToe(True) #game instance, True means training
player1= Qlearning() #player1 learning agent
player2 =Qlearning() #player2 learning agent
game.startTraining(player1,player2) #start training
game.train(200000) #train for 200,000 iterations
game.saveStates()  #save Qtable