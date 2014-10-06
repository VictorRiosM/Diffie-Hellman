#!/usr/bin/python2
from random import randint
from modularExp import modularExp

class Person():
   
   def __init__(self, p, g):
      self._x = randint(2, p-1)
      self._function = modularExp(g, self._x, p)

   def getFx(self):
      return self._function

   def getKey(self, fy, p):
      self._key = modularExp(fy, self._x, p)
      
   def showKey(self):
      return self._key
