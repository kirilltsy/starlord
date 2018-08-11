import random
from army import Army
from ship import Ship
import numpy

TICKPERDAY = 100.
DISTPERDAY = 10.
DISTPERTICK = DISTPERDAY/TICKPERDAY
MINDIST = DISTPERDAY/3



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
		self.planets = self.genplanets(numberofplanets)

	def genplanets(self,numberofplanets):
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



	def battle(pl1,army1,pl2,army2):
		while len(army2)>0:
			army2.takedmg(army1.givedmg())
			(pl1,army1,pl2,army2) = (pl2,army2,pl1,army1)
		return (pl1, army1)

