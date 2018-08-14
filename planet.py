from config import BUILDPERTICK
from ship import Ship
from army import Army
class Planet():
	def __init__(self, player, cord, name):
		self.player = player
		self.cord = cord
		self.name = name

		self.size = 5
		self.buildtype = None
		self.buildtime = 0.
		self.army = []

	def tick(self):
		if self.buildtype != None:
			self.buildtime += BUILDPERTICK*self.size
		while self.buildtime>1:
			self.buildtime -= 1
			self.army.append(Ship(self.buildtype))

	def changebuildtype(self, types):
		if self.buildtype != types:
			self.buildtime = 0
			self.buildtype = types

	def attack(self):
		attack = Army(self.army)
		self.army = []
		return attack

	def come(self,player,army):
		if player == self.player:
			self army += army
		else:
			(newplayer,newarmy) = battle(self.player,Army(self.army),player,Army(army))
			self.army = newarmy
			if newplayer != self.player:
				self.buildtype = None
				self.buildtime = 0
				self.player =newplayer


def battle(pl1,army1,pl2,army2):
	while not army2.dead():
		army2.takedmg(army1.givedmg())
		(pl1,army1,pl2,army2) = (pl2,army2,pl1,army1)
	return (pl1, army1.listofships)




