class Army(object):
	"""docstring for Army"""
	def __init__(self, armylist):
		self.listofships = armylist
	
	def takedmg(self, listofdmg):
		n = len(self.listofships)
		for i in listofdmg:
			j = random.randrange(n)
			self.listofships[j].takedmg(i)
		newlist = []
		for i in self.listofships:
			if i.live():
				newlist.append(i)
		self.listofships = newlist

	def givedmg(self):
		listofdmg = []
		for i in self.listofships:
			listofdmg += i.givedmg()
		return listofdmg

	def dead(self):
		if len(self.listofships) == 0:
			return True
		return False

