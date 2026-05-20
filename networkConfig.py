import socket, os, subprocess, sys
from random import randint


class Server:

  def __init__(self):
    try:
        result = subprocess.run(["curl", "-s", "https://ifconfig.me"], capture_output=True, text=True, check=True)
      #find the ip of the system on the network
        localIP = result.stdout.strip()
      #take the output and save it 
    except subprocess.CalledProcessError as e:
      #if there is an error with connecting, print it, then close the program
        priunt( f"Error: {e}")
        sys.end(0)
    open = 1
    while open == 1:
      open = 1
      port = randint(49152,65535)
      #dynamic ports
      
      test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      test.settimeout(2)
      open = test.connect_ex((localIP, port))
      test.close
      #try and connect to that port and see if its open
      #connect_ex will return 0 if it connects
    
      
