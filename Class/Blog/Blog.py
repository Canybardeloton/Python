class Forum :
	def	__init__(self):
		self.users = []
	def	register(self, users):
		self.users.append(users)

class Thread :
	def	__init__(self, title, time):
		self.title = title
		self.time = time
		self.posts = []

class Post :
	def	__init__(self, text, user, time):
		self.text = text
		self.user = user
		self.time = time
		self.image = []
	def	get_image(self, img):
		self.image.append(img)

class User :
	def __init__(self):
		pass
