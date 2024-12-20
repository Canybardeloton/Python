class Screw:
	MAX_TIGHTNESS = 5
	def __init__(self):
		self.tightness = 0
	def loosen(self):
		if (self.tightness > 0):
			self.tightness -= 1
	def tighten(self):
		if (self.tightness < self.MAX_TIGHTNESS):
			self.tightness += 1
	def __str__(self):
		return "Screw with tightness {}".format(self.tightness)

class Nail:
	def __init__(self):
		self.in_wall = False
	def nail_in(self):
		if (not self.in_wall):
			self.in_wall = True
	def remove(self):
		if (self.in_wall):
			self.in_wall = False
	def __str__(self):
		return "Nail {}in wall.".format("" if self.in_wall else "not ")