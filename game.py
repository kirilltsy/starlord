import random
from army import Army
from ship import Ship
from planet import Planet
import numpy
import name
from config import *
from shipgroup import Shipgroup


class Game(object):
	"""docstring for Game"""
	def __init__(self):
		self.planets = []
		self.playres = {}
		self.tick = 0
		self.day = 0
		self.shipgroups = []

	def startgame(self,dictofplayers,numberofplanets):
		self.players = dictofplayers
		cordplanets = self.cordplanets(numberofplanets)
		nameplanets = name.manynames(len(cordplanets))
		for i in range(len(cordplanets)):
			self.planets.append(Planet(None,cordplanets[i],nameplanets[i]))



	def cordplanets(self,numberofplanets):
		width = (numpy.sqrt(numberofplanets)*DISTPERDAY)/2
		listofcord = numpy.random.uniform(-width, width, size=(numberofplanets,2))
		circle = [a for a in listofcord if numpy.linalg.norm(a)<width]
		i = 0
		while i<len(circle):
			k = i+1
			while k<len(circle):
				if numpy.linalg.norm(circle[k]-circle[i]) < MINDIST:
					circle.pop(k)
				else:
					k += 1
			i += 1
		return circle


