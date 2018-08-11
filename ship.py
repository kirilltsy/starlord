class Ship(object):
	"""docstring for Ship"""
	def __init__(self, type):
		if type == 1:
			self.hp = 3
			self.dmg = [1]
		else:
			self.hp = 2
			self.dmg = [1,1]

	def givedmg(self):
		return self.dmg

	def takedmg(self,takendmg):
		self.hp = self.hp - takendmg

	def live(self):
		if self.hp>0:
			return True
		else:
			return False
