# BattleShiPI

Hello. Thank you for installing BattleShiPI

The classic Battleship game intended to run between two Raspberry Pis on the same network using TCP. Written as a Technology Engineering class final assignment, this project is open for anyone who is sufficiently bored to download and use. 

This project is written for Linux primarily, but is compatible with Windows. If you are using MacOs YMMV.
For the GUI the, this project uses graphics.py, which will be included in this zip folder. Nothing special will need to be done to install this, just make sure that the graphics.py file is unedited and in the same folder as the main python file.
A connection to the internet is also required as should be clear since it transmits data over TCP.
Other than that, simply running “BattleShiPI.py” will properly execute the whole program

When you open the file, you will be prompted to run the game in Host or Client mode. In host mode, your IP on the network will be given so the client is able to connect to you. In client mode you require the IP of the host. Besides some minor ordering things when initializing the game, the role each RPi takes does not matter when playing, the names are more a formality. 

If something is not working as intended, that's actually a secret feature. Do not contact me about any “bugs” you find
