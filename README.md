# BattleShiPI

Hello. Thank you for installing BattleShiPI

The classic Battleship game intended to run between two Raspberry Pis on the same network using TCP. Written as a Technology Engineering class final assignment, this project is open for anyone who is sufficiently bored to download and use. 

A connection to the internet is required as should be clear since it transmits data over TCP.
To run the game, download every file in this repo and save them all in the same folder. Then, simply running “BattleShiPI.py” will properly execute the whole program

This project also includes sound files, for these you will need to run:
$pip install playsound3

When you start the game, you will be prompted to run the game in Host or Client mode. In host mode, your IP and Port on the network will be given so the client is able to connect to you. In client mode you require the IP and Port of the host. Besides some minor ordering things when initializing the game, the role each RPi takes does not matter when playing, the names are more a formality. 

If something is not working as intended, that's actually a secret feature. Do not contact me about any “bugs” you find
