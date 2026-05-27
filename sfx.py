from playsound3 import playsound
import os

class sfx:
  '''Create and object from which you can play different sounds, run before changing the directory to anything but the base folder'''
  
  def __init__(self):
    self.src = os.getcwd() + "/sfx/"

  def hit(self):
    playsound(self.src + "hit.wav", block=False)

  def miss(self):
    playsound(self.src + "miss.wav", block=False)

  def sink(self):
    playsound(self.src + "sink.wav", block=False)

  def build(self):
    playsound(self.src + "build.wav", block=False)

  def win(self):
    playsound(self.src + "win.wav", block=False)

  def loss(self):
    playsound(self.src + "loss.wav", block=False)
    
