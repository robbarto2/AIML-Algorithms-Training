# Tic-Tac-Toe-Reinforcement-learning
Agent learns to play Tic-Tac-Toe using Reinforcement-learning (Q-learning). The agent was trained by playing against itself. Human can also play against trained Agent.

![Alt text](https://github.com/Rohithkvsp/Tic-Tac-Toe-Reinforcement-learning/blob/master/Game.jpg)<br />
<b>Requirements:</b><br />
python 3.5.2 and pygame

Run <b>Play.py</b> to play game.<br />
```
py -3 Play.py
```
Run <b>Train.py</b> to train the agent.<br />
```
py -3 Train.py
```

<b>Training:</b><br />
It took 200,000 iterations to master the game.
```
game = TicTacToe(True) #game instance, True means training
player1= Qlearning() #player1 learning agent 
player2 =Qlearning() #player2 learning agent 
game.startTraining(player1,player2) #start training
game.train(200000) #train for 200,000 iterations
game.saveStates()  #save Qtable
```

<b>Playing</b><br />

Human player vs AI agent
```
game = TicTacToe() #game instance
player1=Humanplayer() #human player
player2=Qlearning()  #agent
game.startGame(player1,player2)#player1 is X, player2 is 0
game.reset() #reset
game.render() # render display
```
Random player instead of AI agent

```
#change player1 or player2 to Randomplayer()
player2 =Randomplayer()
```
