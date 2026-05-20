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
        print( f"Error: {e}")
        sys.end(0)
    open = 1
    while open == 1:
      open = 1
      port = randint(49152,65535)
      #dynamic ports
      #generate a random port 
      test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      test.settimeout(2)
      open = test.connect_ex((localIP, port))
      test.close
      #try and connect to that port and see if its open
      #connect_ex will return 0 if it connects
    #once an ip and port are validated 
    try:
       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((localIP, port))
        s.listen()
        cl, addr = s.accept()
        print("Connected to ", addr)
        return(cl)
    except:
       print("An error with the connection has occured. Please check your connection then try again")
       sys.end(0)
       
    #then open the server and make the conncetion 
  
  def tmBoard(self, boatMap, cl):
    #send the boat maps over
    packet = str(boatMap).encode()
    #turn the boatMap into sendable data
    cl.sendall(packet)
    #send that data to the client
    mapString = (cl.revc(1024)).decode()
    return(mapString)

  def tmTurn(self, move, cl):
    #send the shot
    packet = str(move).encode()
    #turn the shot location into sendable data
    cl.sendall(packet)

    incoming = (cl.revc(1024)).decode()
    return(incoming)

class Client:

  def __init__(self):
    
    ip = input("Please input the IP address of the Host: ")
    port = input("Please input the port of the Host: ")
    try:
        cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s, addr = cl.connect((ip, port))
        print("Connected to ", addr)
        return(s)
    except:
       print("An error with the connection has occured. Please check your connection then try again")
       sys.end(0)
    
    #then open the server and make the conncetion 
  
  def tmBoard(self, boatMap, s):
    #send the boat maps over
    packet = str(boatMap).encode()
    #turn the boatMap into sendable data
    s.sendall(packet)
    #send that data to the client
    mapString = (s.revc(1024)).decode()
    return(mapString)

  def tmTurn(self, move, s):
    #send the shot
    packet = str(move).encode()
    #turn the shot location into sendable data
    s.sendall(packet)

    incoming = (s.revc(1024)).decode()
    return(incoming)
