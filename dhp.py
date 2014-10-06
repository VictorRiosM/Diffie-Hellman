#!/usr/bin/python2
from random import randint
from random import SystemRandom
from modularExp import modularExp
from math import sqrt
from person import Person
from sys import argv

def isGenerator(g, p):
   i = 2
   while i < (p - 1):
      if (p - 1) % i == 0 and modularExp(g, i, p) == 1:
         return False
      i += 1
   return True

def createGenerator(p):
   g = randint(2, p-1)
   while not isGenerator(g, p):
      g = randint(2, p-1)
   return g

def createPrime(bits):
   i = 2
   rand = SystemRandom()
   prime = rand.getrandbits(bits)
   while i <= sqrt(prime):
      if prime % i == 0:
         i = 1
         prime = rand.getrandbits(bits)
      i += 1
   return prime
   
def hack(p, g, fx, fy):
   i = 2
   while i < p:
      k = modularExp(g, i, p)
      if k == fx:
         K = modularExp(fy, i, p)
         print "Hacked. The key is: ", K, "| x =", i
         return K
      if k == fy:
         K = modularExp(fx, i, p)
         print "Hacked. The key is: ", K, "| y =", i
         return K
      i += 1

def main():
   try:
      bits = int(argv[1])
   except:
      bits = 16
   p = createPrime(bits)
   g = createGenerator(p)
   print "p =", p, "| g =", g

   Alice = Person(p, g)
   Bob = Person(p, g)

   fx = Alice.getFx()
   fy = Bob.getFx()
   print "Fx = ", fx
   print "Fy = ", fy

   Alice.getKey(Bob.getFx(), p)
   Bob.getKey(Alice.getFx(), p)

   print "Key Alice = ", Alice.showKey()
   print "Key Bob = ", Bob.showKey()

   Key = hack(p, g, fx, fy)

main()

