# -------------------------------------------------------------------------
#    Main function with CLI for the Habit Tracker App
#    Author: Eder Alois
# -------------------------------------------------------------------------
# This is a simple main program for the Habit Tracker App
import questionary
import utility as util
from database.habit_db import db_init, db_clear
from classes.user import User
from classes.habit import Habit
from classes.habit_tracker import HabitTracker
from datetime import date


def analysing_menu():
    """
    Analysing menu
    :return:
    """
    active_user = User.active_user_id

    stop_loop = False
    select_message = "Analysing Menu for User: " + str(active_user)
    # choice list for the analysing menu
    choice_list = ["Active Habits", "Struggled Habits",
                   "Daily Habits", "Weekly Habits", "Monthly Habits",
                   "Longest run streak of all Habits", "Longest run streak of a Habit",
                   "Exit Analysing Menu"]
    # check whether a user is selected
    if util.check_active_used_id():
        active_user = User.active_user_id
        while not stop_loop:
            choice = questionary.select(message=select_message,
                                        choices=choice_list).ask()
            if choice == choice_list[0]:
                # Active habits
                print(choice_list[0])
                temp_habit = HabitTracker()
                temp_habit.view_active_habits(user_id=active_user)
            elif choice == choice_list[1]:
                # Struggled Habits
                print(choice_list[1])
                temp_habit = HabitTracker()
                temp_habit.view_struggled_habits(user_id=active_user)
            elif choice == choice_list[2]:
                # Daily Habits
                print(choice_list[2])
                temp_habit = HabitTracker()
                temp_habit.view_daily_habits(user_id=active_user)
            elif choice == choice_list[3]:
                # Weekly Habits
                temp_habit = HabitTracker()
                temp_habit.view_weekly_habits(user_id=active_user)
                print(choice_list[3])
            elif choice == choice_list[4]:
                # Monthly Habits
                print(choice_list[4])
                temp_habit = HabitTracker()
                temp_habit.view_monthly_habits(user_id=active_user)
            elif choice == choice_list[5]:
                # Longest run streaks of all habits
                print(choice_list[5])
                temp_habit = HabitTracker()
                temp_habit.view_longest_run_streaks_of_all_habits(user_id=active_user)
            elif choice == choice_list[6]:
                # Longest run streak of a habit
                print(choice_list[6])
                temp_habit = Habit("", "", "", "",
                                   date(2022, 1, 1), date(2022, 1, 1), "")
                temp_habit = Habit.get_all_habits_of_user(temp_habit, user_id=User.active_user_id)
                print("*** List of all habits of the user ***")
                util.print_habit_list(temp_habit)
                habit_id = util.select_habit_id()
                temp_habit = HabitTracker()
                temp_habit.view_longest_run_streak_of_habit(user_id=active_user, habit_id=habit_id)
            elif choice == choice_list[7]:
                print(choice_list[7])
                stop_loop = True
            else:
                print("Please select an action")
    else:
        print("Please select an active User")


def habit_menu():
    active_user = User.active_user_id
    stop_loop = False
    select_message = "Habit Menu for User: " + str(active_user)
    choice_list = ["View Habits", "New Habit", "Modify Habit",
                   "Delete Habit", "Check Habit", "View Checks", "Exit Habit Menu"]
    # check whether a user is selected
    if util.check_active_used_id():
        # Menu only possible if active user is set
        while not stop_loop:
            choice = questionary.select(message=select_message,
                                        choices=choice_list).ask()
            if choice == choice_list[0]:
                # View all habits
                print(choice_list[0])
                temp_habit = Habit("", "", "", "",
                                   date(2022, 1, 1), date(2022, 1, 1), "")
                habit_list = Habit.get_all_habits_of_user(temp_habit, user_id=User.active_user_id)
                util.print_habit_list(habit_list)
            elif choice == choice_list[1]:
                # Create new habit
                print(choice_list[1])
                util.create_new_habit()
            elif choice == choice_list[2]:
                # Modify habit
                print(choice_list[2])
                temp_habit = Habit("", "", "", "",
                                   date(2022, 1, 1), date(2022, 1, 1), "")
                # get all habits for the user for the choice list
                temp_habit = Habit.get_all_habits_of_user(temp_habit, user_id=User.active_user_id)
                print("*** List of all Habits ***")
                util.print_habit_list(temp_habit)
                # selects a habit out of a choice from the user and returns the habit that has to be modifies
                modify_habit_id = util.select_habit_id()
                if modify_habit_id != 'Exit':
                    temp_habit = Habit("", "", "", "",
                                       date(2022, 1, 1), date(2022, 1, 1), "")
                    active_user = User.active_user_id
                    # shows the habit that has to be modifies
                    temp_habit = temp_habit.get_single_habit(user_id=active_user, habit_id=modify_habit_id)
                    print("*** Habit to be modified ***")
                    util.print_habit_list(temp_habit)
                    # request and check the format of the new data
                    habit_description = questionary.text("Put in habit description?").ask()
                    habit_category = questionary.text("Put in habit category?").ask()
                    habit_start = util.request_and_check_habit_date("Put in habit start date [yyyy-mm-dd]?")
                    habit_stop = util.request_and_check_habit_date("Put in habit stop date [yyyy-mm-dd]?")
                    habit_period = util.request_and_check_habit_period("Put in habit period [d/w/m]?")
                    # modify the habit and save the new data in the db
                    temp_habit = Habit("", "", "", "",
                                       date(2022, 1, 1), date(2022, 1, 1), "")
                    temp_habit.modify_habit(user_id=active_user, habit_id=modify_habit_id,
                                            description=habit_description, category=habit_category,
                                            start_date=habit_start, stop_date=habit_stop,
                                            periodicity=habit_period)
                    # shows the list of habits with the modified habit
                    temp_habit = Habit("", "", "", "",
                                       date(2022, 1, 1), date(2022, 1, 1), "")
                    temp_habit = Habit.get_all_habits_of_user(temp_habit, active_user)
                    print("*** List of all Habits for the active User ***")
                    util.print_habit_list(temp_habit)
            elif choice == choice_list[3]:
                # deletes a habit form the db
                print(choice_list[3])
                delete_hid = util.select_habit_id()
                user_id = User.active_user_id
                temp_habit = Habit("", "", "", "",
                                   date(2022, 1, 1), date(2022, 1, 1), "")
                temp_habit.delete_habit(user_id, delete_hid)
            elif choice == choice_list[4]:
                # check a habit
                print(choice_list[4])
                # select the habit id from a choice list
                habit_id = util.select_habit_id()
                user_id = User.active_user_id
                temp_habit = Habit("", "", "", "",
                                   date(2022, 1, 1), date(2022, 1, 1), "")
                check_date = date.today()
                temp_habit.check_habit(user_id=user_id, habit_id=habit_id, check_date=check_date)
            elif choice == choice_list[5]:
                # view all checks of a habit
                print(choice_list[5])
                habit_id = util.select_habit_id()
                user_id = User.active_user_id
                temp_habit = Habit("", "", "", "",
                                   date(2022, 1, 1), date(2022, 1, 1), "")
                temp_habit = temp_habit.get_checks(user_id=user_id, habit_id=habit_id)
                util.print_check_list(temp_habit, user_id=user_id, habit_id=habit_id)
            elif choice == choice_list[6]:
                # Exit habit menu
                print(choice_list[6])
                stop_loop = True
            else:
                print("Please select an action")
    else:
        print("Please select an active User")


def user_menu():
    """
    Function for the USER menu with the actions for
    :return:
    """
    temp_user = User("U_00", "", "")
    stop_loop = False
    select_message = "User Menu"
    choice_list = ["View Users", "Create User", "Modify User", "Delete User",
                   "Select User", "Active User", "Exit User Menu"]
    while not stop_loop:
        # User menu is allways possible
        choice = questionary.select(message=select_message,
                                    choices=choice_list).ask()
        if choice == choice_list[0]:
            # View users
            print(choice_list[0])
            user_list = User.get_all_users(temp_user)
            util.print_user_list(user_list)
        elif choice == choice_list[1]:
            # Create new user
            print(choice_list[1])
            util.create_new_user()
        elif choice == choice_list[2]:
            # Modify user
            print(choice_list[2])
            temp_user = User.get_all_users(temp_user)
            print("*** List of all User ***")
            util.print_user_list(temp_user)
            # select user id form a list of users
            modify_userid = util.select_userid()
            temp_user = User("U_00", "", "")
            temp_user = temp_user.get_user(user_id=modify_userid)
            print("*** User to be modified ***")
            util.print_user_list(temp_user)
            # ask new user data ans dave in db
            name = questionary.text("Put in your new user name?").ask()
            description = questionary.text("Put in your new user description?").ask()
            temp_user = User("U_00", "", "")
            temp_user.modify_user(uid=modify_userid, name=name, description=description)
            # print all users with modified user
            temp_user = User("U_00", "", "")
            temp_user = User.get_all_users(temp_user)
            print("*** List of all User ***")
            util.print_user_list(temp_user)
        elif choice == choice_list[3]:
            # delete user
            print(choice_list[3])
            temp_user = User("U_00", "", "")
            # select user which has to be deleted from a list
            delete_userid = util.select_userid()
            print(delete_userid)
            temp_user.delete_user(uid=delete_userid)
        elif choice == choice_list[4]:
            # select user as active user
            print(choice_list[4])
            util.activate_user()
        elif choice == choice_list[5]:
            # list active user data
            print(choice_list[5])
            temp_user = User()
            temp_user = User.get_active_user(temp_user)
            print("*** Selected active User ***")
            if User.active_user_id == '':
                print("No active user selected")
            else:
                util.print_user_list(temp_user)
        elif choice == choice_list[6]:
            # Exit User menu
            print(choice_list[6])
            stop_loop = True
        else:
            print("Please select an action")


def admin_menu():
    """
    Function for the USER menu with the actions
    menu is password protected
    :return:
    """
    exp_password = "1469"  # Password for admin menus
    select_message = "Please put in the Admin key"
    password = questionary.password(message=select_message,
                                    default="").ask()
    print(exp_password)
    print(password)
    if password == exp_password:
        stop_loop = False
        select_message = "Admin Menu"
        choice_list = ["Import User List", "Import Habit List", "Import check List", "Clear DB", "Init DB",
                       "Exit Admin Menu"]
        while not stop_loop:
            choice = questionary.select(message=select_message,
                                        choices=choice_list).ask()
            if choice == choice_list[0]:
                # Import a user list
                print(choice_list[0])
                temp_user = User("U_00", "", "")
                temp_user.import_user_list()
            elif choice == choice_list[1]:
                # Import a habit list
                print(choice_list[1])
                temp_habit = Habit("", "", "", "",
                                   date(2022, 1, 1), date(2022, 1, 1), "")
                temp_habit.import_habit_list()
            elif choice == choice_list[2]:
                # import a checkoff list
                print(choice_list[2])
                temp_habit = Habit("", "", "", "",
                                   date(2022, 1, 1), date(2022, 1, 1), "")
                temp_habit.import_check_list()
            elif choice == choice_list[3]:
                # clear the db
                print(choice_list[3])
                db_clear()
            elif choice == choice_list[4]:
                # initialize the db
                print(choice_list[4])
                db_init()
            elif choice == choice_list[5]:
                # Exit Admin menu
                print(choice_list[5])
                stop_loop = True
            else:
                print("Please select an action")
    else:
        print("Password is not correct")


def main_menu():
    """
    Main menu function
    :return:
    """
    stop_loop = False
    select_message = "Main Menu"
    choice_list = ["Habit Menu", "Analysing Menu", "User Menu", "Admin Menu", "Exit Program"]
    while not stop_loop:
        choice = questionary.select(message=select_message,
                                    choices=choice_list).ask()
        if choice == choice_list[0]:
            print(choice_list[0])
            habit_menu()
        elif choice == choice_list[1]:
            print(choice_list[1])
            analysing_menu()
        elif choice == choice_list[2]:
            print(choice_list[2])
            user_menu()
        elif choice == choice_list[3]:
            print(choice_list[3])
            admin_menu()
        elif choice == choice_list[4]:
            print(choice_list[4])
            stop_loop = True
        else:
            print("Please select an action")


def cli():
    """
    Command line interface (CLI) for using the Habit Tracker App Backend
    :return:
    """
    stop_loop = False
    db_init()
    select_message = "Start Menu"
    choice_list = ["View Users", "Select User", "Create new User", "Exit Start Menu"]
    while not stop_loop:
        choice = questionary.select(message=select_message,
                                    choices=choice_list).ask()
        if choice == choice_list[0]:
            print(choice_list[0])
            temp_user = User("U_00", "", "")
            user_list = User.get_all_users(temp_user)
            util.print_user_list(user_list)
        elif choice == choice_list[1]:
            print(choice_list[1])
            util.activate_user()
        elif choice == choice_list[2]:
            print(choice_list[2])
            util.create_new_user()
        elif choice == choice_list[3]:
            print(choice_list[3])
            stop_loop = True
        else:
            print("Please select an action")

    main_menu()


if __name__ == '__main__':
    cli()
