# -------------------------------------------------------------------------
#    Utility modul for Habit Tracker App
#    This module contains all utility functions which are necessary
#    Author: Eder Alois
# -------------------------------------------------------------------------
import questionary
import pandas as pd
from classes.user import User
from classes.habit import Habit
from datetime import date, datetime

def check_date_format(date_str) -> bool:
    """
    function checks the input format of the date
    :param date_str:
    :return: True, if format is correct, otherwise False
    """
    # initializing date format
    date_format = "%Y-%m-%d"
    res = True
    # checking if format matches the date
    # using try-except to check for truth value
    try:
        res = bool(datetime.strptime(date_str, date_format))
        # print(date_str, date_format, str(res))
    except ValueError:
        print("Format of input date is not correct, try again")
        res = False
    finally:
        return res

def check_periodicity_format(period) -> bool:
    """
    function checks the input format for the periodicity
    allowed values: 'd' (for daily), 'w' (for weekly), 'm' (for monthly)
    :param period:
    :return: True, if format is correct, otherwise False
    """
    # initializing res
    res = True

    # checking if format matches the periodicity "d", "w", or "m"
    # using try-except to check for truth value
    if (period == "d") or (period == "w") or (period == "m"):
        res = True
    else:
        print("Format of periodicity is not correct, try again")
        res = False
    return res

def request_and_check_habit_date(question_str) -> str:
    """
    requests a date from the user and checks the format and repeats if format is not correct
    :param question_str:
    :return: correct string of date
    """
    check_date_state = False
    while not check_date_state:
        habit_date = questionary.text(question_str).ask()
        check_date_state = check_date_format(str(habit_date))
    return habit_date

def request_and_check_habit_period(question_str) -> str:
    """
    requests a period from the user and checks the format and repeats if format is not correct
    :param question_str:
    :return: correct string of period
    """
    correct_period_state = False
    while not correct_period_state:
        habit_period = questionary.text(question_str).ask()
        correct_period_state = check_periodicity_format(str(habit_period))
    return habit_period

def generate_id(temp_list, init_value) -> str:
    """
    generates a unique id for the nest entry in the temp_list (format: X_yy)
    :param temp_list:
    :param init_value: of the id for the temp_list (starting point as str)
    :return: next unique id for the temp_list
    """
    if not (len(temp_list)):
        ident = init_value
    else:
        id_temp = (max(temp_list)[0]).split('_')
        if int(id_temp[1]) < 9:
            ident = id_temp[0] + "_" + "0" + str(int(id_temp[1]) + 1)
        else:
            ident = id_temp[0] + "_" + str(int(id_temp[1]) + 1)
    return ident

def print_user_list(user_list) -> None:
    """
    print out the user list
    the user_list is generated with panda data Frame format
    :param user_list:
    :return: None
    """
    df = pd.DataFrame(user_list, columns=['User_id', 'Username', 'Description'], index=None)
    print(df)

def create_new_user() -> None:
    """
    This function generates a new user:
    It generates the uid automatically in the format of "U_xy"
    The username and the user description has to be put in
    The new user will be stored in the database in table users
    :return: None
    """
    # Ask for user data
    temp_user = User("U_00", "", "")
    user_list = User.get_all_users(temp_user)
    # generation of UID in the format "U_xy" automatically
    uid = generate_id(user_list, "U_00")

    if uid != "None":
        temp_user.user_id = uid
        # request username and description from user and adds the user to the db
        temp_user.user_name = questionary.text("Put in your user name?").ask()
        temp_user.user_description = questionary.text("Put in your user description?").ask()
        User.add_user(temp_user)

    # print("*** New User created")

def select_userid() -> str:
    """
    generates the selection list of al users of the db
    :return: choice of the selected user
    """
    choice_list = []
    temp_user = User("U_00", "", "")
    user_list = User.get_all_users(temp_user)
    # generate list for the questionary ask table
    for user in user_list:
        choice_list.append(str(user[0]))
    # ask for a choice of user
    choice_list.append("Exit")
    choice = questionary.select("Select User",
                                choice_list).ask()
    print("selected User")
    return choice

def activate_user() -> None:
    """
    function to set a user activ, it shows a selection list with all user
    the user can select a user to set him active
    :return: None
    """
    temp_user = User("U_00", "", "")
    # select user id from the choice function
    selected_userid = select_userid()
    print(selected_userid)
    # sets the selected user active and shows the new active user
    temp_user.set_active_user(user_id=selected_userid)
    temp_user = temp_user.get_active_user()
    print("*** Selected active User ***")
    print_user_list(temp_user)

def check_active_used_id() -> bool:
    """
    checks if a user is active user is
    :return: True is a user is active, False if not
    """
    try:
        temp_user = User("U_00", "", "")
        temp_u = temp_user.get_active_user()
        if temp_u[0] == "":
            return False
        else:
            return True
    except:
        print("no user available, please create user")

def print_habit_list(habit_list) -> None:
    """
    print out the habit list
    The format is generated with panda data Frame format
    :param habit_list:
    :return: None
    """
    df = pd.DataFrame(habit_list, columns=['Habit_id', 'User_id', 'habit_description', 'habit_category',
                                           'habit_start', 'habit_stop', 'habit_period',
                                           'CheckOff', 'Break', 'last_completion',
                                           'current streak period', 'longest streak period'], index=None)

    print(df)

def create_new_habit():
    """
    This function generates a new habit for the active user:
    It generates the uid automatically in the format of "H_xy"
    All other parameter has to be put in
    The new habit will be stored in the database in table habits

    :return: None
    """
    # initialise intern variables for date check and active user
    user_id = User.active_user_id

    # Ask for user data
    temp_habit = Habit("", "", "", "",
                       date(2022, 1, 1), date(2022, 1, 1), "")

    # get all habits to extract last habit id over all habits and users an generate new unique habit id
    habit_list = Habit.get_all_habits(temp_habit)
    # generation of new habit id in the format "H_xy" automatically
    print_habit_list(habit_list)
    hid = generate_id(habit_list, "H_00")

    # if habit id is generated, ask all other information for the new habit and check format of dates
    if hid != "None":
        temp_habit.user_id = user_id
        temp_habit.habit_id = hid
        temp_habit.habit_description = questionary.text("Put in habit description?").ask()
        temp_habit.habit_category = questionary.text("Put in habit category?").ask()
        temp_habit.habit_start = request_and_check_habit_date("Put in habit start date [yyyy-mm-dd]?")
        temp_habit.habit_stop = request_and_check_habit_date("Put in habit stop date [yyyy-mm-dd]?")
        temp_habit.habit_period = request_and_check_habit_period("Put in habit period [d/w/m]?")
        Habit.add_habit(temp_habit)

    print("*** New Habit created")
    temp_habit = Habit.get_single_habit(temp_habit, user_id=user_id, habit_id=hid)
    print_habit_list(temp_habit)

def select_habit_id() -> str:
    """
    generates the selection list of all habits of users of the db
    :return: choice of the selected habit
    """
    user_id = User.active_user_id
    # print(user_id)

    choice_list = []
    temp_habit = Habit("", "", "", "",
                       date(2022, 1, 1), date(2022, 1, 1), "")
    habit_list = Habit.get_all_habits_of_user(temp_habit, user_id)
    # generate list for the questionary ask table
    for habit in habit_list:
        choice_list.append(str(habit[0]))
    choice_list.append("Exit")
    choice = questionary.select("Select Habit",
                                choice_list).ask()
    return choice

def print_check_list(check_list, user_id, habit_id) -> None:
    """
    print out the check_list of the active user for a selected habit
    The format is generated with panda data Frame format
    :param check_list:
    :param user_id:
    :param habit_id:
    :return: None
    """
    df = pd.DataFrame(check_list, columns=['Check_id', 'User_id', 'Habit_id', 'Check dates'], index=None)

    print(df)
