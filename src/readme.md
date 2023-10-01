# IU-Akademie: OOFPP Project

# A simple Backend for a Habit Tracker Appy Counter App


## Overview
This is a small description  of a Habit Tracker Backend with a small CLI interface. 
It can be run in a Python3 environment with some libraries shown in the requirement.txt file
It has three main classes (Habit _Tracker, Habit and User), a database module for storing the data
and an interface module for analysing the habits.
A small CLI interface module is implemented for the User interface.
The menue structure is shown in the picture.
![](images/Development_HabitFlow_05.jpg?raw=true "Habit CLI structure")

## Class and interface diagram
The base parts are the three classes for the user handling, habit tracking and habits. 
I choose to realize this functionalities by three classes.
The database and his interfaces are realized as interface modules similar was done with the analyzing module.
The small interface module for the user is not realized as a graphical user interface, 
it is just a simple command line base interface. 
This is the class and interface module structure.

![Alt text](images/Development_Habit_Classes_Interfaces_05.jpg?raw=true "Habit Classes and Interfaces")

Testing is done by pytest.

## generate Requirements file
````shell
pip freeze > requirements.txt
````

## Installation
A Python 3 version must be used.
I prefer to use the PyCharm development environment.
Installation of the used libraries is done with the  shell command base on the requirements.txt files.

````shell
git clone https://github.com/ae-863/habit_tracker_oofpp.git

cd habit-tracker

pip install -r requirements.txt
````

## Usage
The program can be started in a shell environment.
Start
````shell
python main.py
````

## Tests
Module and basic testing is done with the pytest module.
````shell
pytest .
````

# User Interface
### Start Menu
###### View Users: shows a list of all users of the db
###### Select User: select a user for habit generation and tracking
###### Create User: creates a new user
###### Exit: exit Start Menu

###  Main Menu
#### Habit Menu (only if a user is selected)
###### View Habits: views a list of all habits of a user
###### New Habit: generates a new habit for a user in the db
###### Modify Habit: changes the data of a habit for a user in the db
###### Delete Habit: deletes a habit for a user in the db
###### Check Habit: checkoffs a selected habit for a user in the db
###### View Checks: views a list of all checks of a habit for a user
###### Exit Habit Menu: exits the habit menu an goes back to the main menu


#### Analysing Menu
###### Active Habits: shows a list of all active habits of a user
###### Struggled Habits: shows a list of all struggled habits of a user
###### Daily Habits: shows a list of all daily habits of a user
###### Weekly Habits: shows a list  of all weekly habits of a user
###### Monthly Habits: shows a list of all monthly habits of a user
###### Longest run streak of all Habits: shows a list with the longest run streaks of all habits for a user
###### Longest run streak of a Habits: shows a list with the longest run streaks of a habits for a user
###### Exit Analysing Menu: exits the analysing menu and goes back to the mein menu

#### User Menu
###### View Users: views a list of all users
###### Create User: creates a new User in the db
###### Modify User: modifies a user in the db
###### Delete User: deletes a user in the db
###### Select User: selects a user as active user for the habit and analysing
###### Active User: shows the active user in a list 
###### Exit User Menu: exits the user menu and goes back to the mein menu

#### Admin Menu (requests password to start the admin menu)
###### Import User List: imports the user list of the example.py module
###### Import Habit List: imports the habit list of the example.py module
###### Import check List: imports the checklist of the example.py module
###### Clear DB: clears the content of the db
###### Init DB: initialises the DB and tables of the DB
###### Exit Admin Menu: exits the admin menu and goes back to the main menu

#### Exit Main Menu

# Disclaimer
The developed application is licensed under the GNU General Public License.