# terminal_app_with_login

Simple terminal app that allows user creation, persistence, and log in / log out functionality with a logged_in_menu_loop() that is only accessible after login and displays user-specific data.

This only provides a framework for adding in more specific relationships/structures/functions/classes, but it gets you off on a good foot!

To get started, make sure you have:

- python 2.X
- cPickle

will also
- import os
- from collections import OrderedDict

Run the app via ./run_app.py

On creation of the first user, a /user_data/ folder is created in the repo, with a folder for each user id (uid) and a user_data.file that contains the user object. Saving and retrieving the data from disk is done via pickle in user.py (and accessible via a UserAccess method).