from Game import Player
from Game import Game


player1 = Player(input("Enter first player's name : "))
player2 = Player(input("Enter second player's name : "))
newGame = Game(player1, player2)
newGame.gameInstance()
newGame.play()