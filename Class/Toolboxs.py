class	Toolbox:
	def	__init__(self):
		self.tool = []
	def	add_tool(self, tool):
		self.tool.append(tool)
	def	remove_tool(self, tool):
		self.tool.remove(tool)

class	Hammers :
	def	__init__(self, color):
		self.color = color
	def	painting(self, color):
		self.color = color
	def	hammer_in(self, nail):
		nail.nail_in()
	def	remove_nails(self, nail):
		nail.remove()


class	Screwdrivers :
	def	__init__(self, size):
		self.size = size
	def	thighten_screw(self, screw):
		screw.tighten()
	def	loosen_screw(self, screw):
		screw.loosen()

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

def	main():
	toolbox = Toolbox()
	screwdriver = Screwdrivers(10)
	hammer = Hammers("red")
	screw = Screw()
	nail = Nail()

	toolbox.add_tool(screwdriver)
	toolbox.add_tool(hammer)
	print(screw.__str__)
	screwdriver.thighten_screw(screw)
	print(screw.__str__)
	print(nail.__str__)
	hammer.hammer_in(nail)
	print(nail.__str__)


if __name__ == "__main__":
	main()