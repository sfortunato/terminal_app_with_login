import cPickle as pickle 
import os


class User:
	def __init__(self, uid, username, email, password, **kwargs):
		"""initializes new user, should only be called via user_access.create() which will generate the uid"""
		self.uid = uid
		self.username = username
		self.email = email
		self.password = password
		self.first_name = "not initiated"
		self.middle_name = "not initiated"
		self.last_name = "not initiated"
		self.dob = "not initiated"


	def printAll(self):
		"""prints all user data, abstracts sensitive information"""
		print "uid          ", self.uid
		print "username:    ", self.username
		print "email:       ", self.email
		print "password:    ", "#######"
		print "first name:  ", self.first_name
		print "middle name: ", self.middle_name
		print "last name:   ", self.last_name
		print "DOB:         ", self.dob
		print ""
		# note: printAll does not print out additional inputs added via user.addInput()


	def persistToFile(self):
		"""soft creates / finds user's user_data folder, persists using pickle"""
		path_to_uid_dir = "user_data/" + self.uid
		os.system("mkdir -p " + path_to_uid_dir)
		user_file = path_to_uid_dir + "/" + "user_data.file"
		with open(user_file, "wb") as f:
				pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)


	@staticmethod 		
	def loadFromFile(uid):
		"""finds a user's user_data folder, loads using pickle, returns user object"""
		path_to_uid_dir = "user_data/" + uid
		user_file = path_to_uid_dir + "/" + "user_data.file"
		with open(user_file, "rb") as f:
			user = pickle.load(f)
		return user


	def addInput(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)
		persistToFile(self)
		return user
		# note: inputs added do not print as part of user.printAll() or user_access.printAll(user)



