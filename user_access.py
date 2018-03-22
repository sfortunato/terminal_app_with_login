import cPickle as pickle
import os

from user import User


class UserAccess:
	def __init__(self):
		self.n = ""

	def assignNewUID(self):
		"""finds highest known UID, assigns a higher one, maintains preceding 0s and can set first UID if none exist"""
		d = './user_data/'
		os.system("mkdir -p " + d)
		uids_exist = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
		if len(uids_exist) == 0:
			return "000000001"
		uids_exist = [o.split("user_data/")[1] for o in uids_exist]
		uids_exist = sorted(uids_exist)
		highest_known_uid = uids_exist[-1]
		new_uid = int(highest_known_uid) + 1
		new_uid = str(new_uid).zfill(9) #turns into string, fills in leading zeros
		print new_uid
		return new_uid

	def create(self, username, email, password):
		"""checks if username or email exist for another account, if does, returns None; else creates user data folder, assigns a UID, and saves data to folder"""
		d = './user_data/'
		os.system("mkdir -p " + d)
		uids_exist = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
		for i in uids_exist:
			user_file = i + "/" + "user_data.file"
			with open(user_file, "rb") as f:
				user = pickle.load(f)
			if user.username == username:
				return None
			if user.email == email:
				return None

		new_uid = self.assignNewUID()
		new_user = User(new_uid, username, email, password)
		new_user.persistToFile()
		new_user.printAll()
		return new_user


	def login(self, username, password):
		"""finds existing user and returns user object, if password incorrect it returns None"""
		d = './user_data/'
		os.system("mkdir -p " + d)
		uids_exist = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
		for i in uids_exist:
			user_file = i + "/" + "user_data.file"
			with open(user_file, "rb") as f:
				user = pickle.load(f)
			if user.username == username:
				if user.password == password:
					user.printAll()
					return user
				else:
					return None


	def printAll(self, user):
		"""prints all user data"""
		user.printAll()


	def persistToFile(self, user):
		"""saves user object to file via User class"""
		user.persistToFile()


	def addInput(self, user, **kwargs):
		user.addInput(**kwargs)
		return user



