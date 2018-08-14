from config import DISTPERTICK

class Shipgroup():
	def __init__(self, player, dest, dist, army):
		self.player = player
		self.dest = dest
		self.army = army
		self.dist = dist

	def tick(self):
		self.dist -= DISTPERTICK

	def come(self):
		if self.dist < 0:
			return True
		return False

