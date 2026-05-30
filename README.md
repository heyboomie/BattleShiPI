# BattleShiPI

Hello. Thank you for installing BattleShiPI.

The classic Battleship game intended to run between two Raspberry Pis on the same network using TCP. Written as a Technology Engineering class final assignment, this project is open for anyone who is sufficiently bored to download and use. 

A connection to the internet is required as should be clear since it transmits data over TCP. There is a 60 second time out, just be aware of that.
To run the game, download every file in this repo and save them all in the same folder. Then, simply running “BattleShiPI.py” will properly execute the whole program (Python >= 3.10 Required).

This project also includes sound files, for these you will need to run:
$pip install playsound3

When you start the game, you will be prompted to run the game in Host or Client mode. In host mode, your IP and Port on the network will be given so the client is able to connect to you. In client mode you require the IP and Port of the host. Besides some minor ordering things when initializing the game, the role each RPi takes does not matter when playing, the names are more a formality.

If in Client mode, the IP is entered as "gronk" this will change it to a PvAI mode where you will battle the built in AI Captain

When selecting boat positions, RMB to select a tile, Esc to deselect a tile, R to rotate the position of the ship, and Enter to confirm the position. Alternativly, hitting the spacebar then RMB will let a hyper intellegent AI program to select the location of your boats for you. Be patient though, it has some quirks

Once in the game, when prompted (which is when the message box says the enemy has fired somewhere), RMB on a tile to fire there, until all of your boats are destroyed, or you destroy all of theirs.

When a game is finished both games will create a file with the time in seconds since Unix Epoch in seconds. This will contain the position of both ships, as well as each move played in that game. That was you have a record for each game you play. This file will save into the file with BattleShiPI.py in it.

After a game, you will be prompted to hit enter to play another game, this will clear the board and start a new game without having to reenter IP or do any other networking stuff. Or hitting litereally anything else on the keyboard will cause the game to end and close

Sorry in advance about the sound effects, I tried my best.

If something is not working as intended, that's actually a secret feature. Do not contact me about any “bugs” you find.
# BattleShiPI

Hello. Thank you for installing BattleShiPI.

The classic Battleship game intended to run between two Raspberry Pis on the same network using TCP. Written as a Technology Engineering class final assignment, this project is open for anyone who is sufficiently bored to download and use. 

A connection to the internet is required as should be clear since it transmits data over TCP. There is a 60 second time out, just be aware of that.
To run the game, download every file in this repo and save them all in the same folder. Then, simply running “BattleShiPI.py” will properly execute the whole program (Python >= 3.10 Required).

This project also includes sound files, for these you will need to run:
$pip install playsound3

When you start the game, you will be prompted to run the game in Host or Client mode. In host mode, your IP and Port on the network will be given so the client is able to connect to you. In client mode you require the IP and Port of the host. Besides some minor ordering things when initializing the game, the role each RPi takes does not matter when playing, the names are more a formality.

When selecting boat positions, RMB to select a tile, Esc to deselect a tile, R to rotate the position of the ship, and Enter to confirm the position. Or if you're feeling lucky, hit space and let random chance choose your boats for you

Once in the game, when prompted (which is when the message box says the enemy has fired somewhere), RMB on a tile to fire there, until all of your boats are destroyed, or you destroy all of theirs.

When a game is finished both games will create a file with the time in seconds since Unix Time in seconds. This will contain the position of both ships, as well as each move played in that game. That was you have a record for each game you play. This file will save into the file with BattleShiPI.py in it.

Sorry in advance about the sound effects, I tried my best.

If something is not working as intended, that's actually a secret feature. Do not contact me about any “bugs” you find.
