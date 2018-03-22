#!/usr/bin/env python
import os

from collections import OrderedDict
from user_access import UserAccess
from portal_login import PortalLogin


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

portal_organization_menu = OrderedDict([
	("f", "Fenway Health"),
	("b", "BIDMC"),
	("g", "GHC South Central Wisconsin")
])

def log_out(user):
	"""log out of app"""
	user = None
	return user

def add_new_portal(user):
	"""add a new patient portal"""

	print "Select a patient portal to connect with: "
	for key, value in portal_organization_menu.items():
		print "'" + key + "' " + value
	
	choice = raw_input(" > ").lower().strip()
	if choice in portal_organization_menu:
		portal_organization = portal_organization_menu[choice]
		print portal_organization_menu[choice]

	portal_username = raw_input("portal username: ")
	portal_password = raw_input("portal password: ")

	new_portal = PortalLogin(portal_username, portal_password)
	new_portal.organization = portal_organization
	user.portal_list.addPortal(new_portal)
	user.persistToFile()
	
	print ""
	print "Portal added successfully!"

	return None

def print_med_list(user):
	"""print out your med list"""
	user_access.printMedList(user)

def crawl_portals(user):
 	"""check portals for updated data, calls via user_access"""
 	user_access.crawl(user)

def print_all_user_data(user):
 	"""print out all user data"""
 	user_access.printAll(user)

logged_in_menu = OrderedDict([
	("o", log_out),
	("a", add_new_portal),
	("m", print_med_list), 
	("u", crawl_portals),
	("p", print_all_user_data),
	("c", clear_screen)
	])


# menu loops

def log_in_menu_loop():
	"""Show the log in menu and handle user log in, user creation, and quitting"""
	choice = None
	while choice != 'q':
		# clear_screen()
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
		# clear_screen()
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


