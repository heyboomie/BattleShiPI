import socket, os, subprocess, sys, GUI
from random import randint


class Server:

  def __init__(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  #basically you connect to google.com and see what ip you have
    self.localIP = s.getsockname()[0]
    s.close()
    #print(self.localIP)
    open = 1
    while open == 1:
      self.port = randint(49152,65535)
      #dynamic ports
      #generate a random port 
      test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      test.settimeout(2)
      open = test.connect_ex((self.localIP, self.port))
      test.close
      #print(self.port, open)
      #try and connect to that port and see if its open
      #connect_ex will return 0 if it connects
      #once an ip and port are validated 
    try:
       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', self.port))
        s.listen()
        self.cl, self.addr = s.accept()
        print("Connected to", self.addr)

    except Exception as e:
       print("An error with the connection has occured. Please check your connection then try again: ", e)
       sys.exit(0)
       
    #then open the server and make the conncetion 

  def ownName(self):
    return(self.localIP, self.port)
  
  def pairName(self):
    return(self.addr)
  
  def tmBoard(self, boatMap):
    #send the boat maps over
    packet = str(boatMap).encode()
    #turn the boatMap into sendable data
    self.cl.sendall(packet)
    #send that data to the client
    mapString = (self.cl.recv(1024)).decode()
    return(mapString)

  def tmTurn(self, move):
    #send the shot
    packet = str(move).encode()
    #turn the shot location into sendable data
    self.cl.sendall(packet)

  def rcTurn(self):
    incoming = (self.cl.recv(1024)).decode()
    return(incoming)

class Client:

  def __init__(ip, port, self):
    
    # ip = input("Please input the IP address of the Host: ")
    # port = input("Please input the port of the Host: ")
    try:
        cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s, self.addr = cl.connect((ip, port))
        print("Connected to ", self.addr)
    except Exception as e:
       print("An error with the connection has occured. Please check your connection then try again:", e)
       sys.exit(0)
    
    #then open the server and make the conncetion 
  
  def pairName(self):
    return(self.addr)

  def tmBoard(self, boatMap):
    #send the boat maps over
    packet = str(boatMap).encode()
    #turn the boatMap into sendable data
    self.s.sendall(packet)
    #send that data to the client
    mapString = (self.s.recv(1024)).decode()
    return(mapString)

  def tmTurn(self, move):
    #send the shot
    packet = str(move).encode()
    #turn the shot location into sendable data
    self.s.sendall(packet)

  def rcTurn(self):
    incoming = (self.s.recv(1024)).decode()
    return(incoming)

# me = Server()
# print(vars(me))import socket, os, subprocess, sys
