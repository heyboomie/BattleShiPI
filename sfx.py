from ps3 import playsound
import os

class sfx:
  '''Create and object from which you can play different sounds, run before changing the directory to anything but the base folder'''
  
  def __init__(self):
    self.src  = os.path.dirname(os.path.abspath(__file__)) + "/sfx/"

  def hit(self):
    playsound(self.src + "hit.wav", block=False)
    #whistle then an explosion

  def miss(self):
    playsound(self.src + "miss.wav", block=False)
    #whistle then a plop

  def sink(self):
    playsound(self.src + "sink.wav", block=False)
    #blaring alarm

  def build(self):
    playsound(self.src + "build.wav", block=False)
    #3 hammer hitting noises

  def win(self):
    playsound(self.src + "win.wav", block=False)
    #trumpet fanfair

  def loss(self):
    playsound(self.src + "loss.wav", block=False)
    #trumpet bwah bwah bwahhhh 

  def ping(self):
    playsound(self.src + "ping.wav", block=False)
    #this one is the sound when you select server mode, or enter a host address, sonar ping

  def load(self):
    playsound(self.src + "load.wav", block=False)
    #load the cannons
    
