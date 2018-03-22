#!/usr/bin/env python
import os

from collections import OrderedDict
from user_access import UserAccess


user_access = UserAccess()

# miscellaneous functions (clearing screen, etc)
def clear_screen(*args, **kwargs):
	"""clear the screen"""
	os.system("cls" if os.name == "nt" else "clear")


# log_in_menu_loop functions and menu options 
def log_in_user():
	"""log in as an existing user"""

	username = raw_input("username: ")
	password = raw_input("password: ")

	user = user_access.login(username, password)
	return user


def create_user():
	"""create a new user"""
	
	username = raw_input("Choose a username: ").lower().strip()
	email = raw_input("Enter your email: ").lower().strip()
	password = raw_input("Select a password: ").strip()

	try:
		user = user_access.create(username, email, password)
		return user
	except AttributeError:
		print "that username or password already exists"


log_in_menu = OrderedDict([
	("l", log_in_user),
	("c", create_user)
	])


# logged_in_menu functions and menu options
nested_logged_in_menu = OrderedDict([
	("a", "Example 1"),
	("b", "Example 2"),
	("c", "Example 3")
])

def log_out(user):
	"""log out of app"""
	user = None
	return user

def add_some_data(user):
	"""add some new user information"""
	
	first_name = raw_input("first name: ")
	middle_name = raw_input("middle name: ")
	last_name = raw_input("last name: ")
	date_of_birth = raw_input("date of birth: ")

	updates = {
		"first_name": first_name,
		"middle_name": middle_name,
		"last_name": last_name,
		"dob": date_of_birth
	}

	user = user_access.addInput(user, **updates)

	return user

def do_a_thing(user):
	"""some function"""
	print "this function is not yet initiatied"
	return user

def nested_menu_example(user):
 	"""check portals for updated data, calls via user_access"""
 	print "Select some information to add: "
	for key, value in nested_logged_in_menu.items():
		print "'" + key + "' " + value
	
	choice = raw_input(" > ").lower().strip()
	if choice in nested_logged_in_menu:
		returned_object = nested_logged_in_menu[choice]
		print "You selected " + returned_object + " this menu does not do anything (yet)"

	return user

def print_user_data(user):
 	"""print out all user data"""
 	user_access.printAll(user)


logged_in_menu = OrderedDict([
	("o", log_out),
	("a", add_some_data),
	("b", do_a_thing), 
	("c", nested_menu_example),
	("p", print_user_data),
	("c", clear_screen)
	])


# app / menu loops
def log_in_menu_loop():
	"""Show the log in menu and handle user log in, user creation, and quitting"""
	choice = None
	while choice != 'q':
		clear_screen()
		print "'q' to quit"
		for key, value in log_in_menu.items():
			print "'" + key + "' " + value.__doc__
		choice = raw_input(" > ").lower().strip()

		if choice in log_in_menu:
			clear_screen()
			user = log_in_menu[choice]()
			return user 

		elif choice == 'q':
			quit()


def logged_in_menu_loop(user):
	"""Takes a logged in user and lets them access and update their data"""
	choice = None

	while choice != 'o':
		for key, value in logged_in_menu.items():
			print "'" + key + "' " + value.__doc__
		choice = raw_input(" > ").lower().strip()

		if choice in logged_in_menu:
			logged_in_menu[choice](user)

		elif choice == 'o':
			return None


def run_app():
	logged_in_user = None

	while logged_in_user == None:
		logged_in_user = log_in_menu_loop()

		while logged_in_user:
			logged_in_user = logged_in_menu_loop(logged_in_user)


if __name__ == '__main__':
	run_app()


