# -------------------------------------------------------------------------
#    Habit db interface file
#    Author: Eder Alois
# -------------------------------------------------------------------------
import sqlite3
import traceback
import sys

# Database file
DB_FILE = 'database/habit.db'


# **********************************************************************
# general db functions for opening, close and init
# **********************************************************************
def db_open() -> 'conn, c':
    """
    Open the db and returns the connection and the cursor of the db, in case of failures an error message is generated
    :return: connection conn and cursor c of the db
    """
    try:
        # opens connection to db
        conn = sqlite3.connect(DB_FILE)
        # gets the cursor of the connection
        c = conn.cursor()
        return c, conn
    except sqlite3.Error as error:
        print("Failed to get habit data of a single habit for a user from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))


# Used to commit and close database connection
def db_close(conn) -> None:
    """
    Commit and close database connection
    :param conn:
    :return: None
    """
    conn.commit()
    conn.close()


# Initializes the database with the three tables for users, habits and checks
def db_init() -> None:
    """
    Initialize the habit tracker database with the three tables for user, habits and checks.
    :return: None
    """
    try:
        c, conn = db_open()

        # creates the table user in the db with thp primary key user_id
        c.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id text PRIMARY KEY,
                    name text,
                    description text
        )""")

        # creates the table for habits in the db with the primary key habit_id and
        # the foreign key user_id from the user table
        c.execute("""CREATE TABLE IF NOT EXISTS habits (
                    habit_id text PRIMARY KEY,
                    user_id text,
                    description text,
                    category text,
                    start_date date,
                    stop_date date CHECK (stop_date > start_date),
                    periodicity text,
                    last_checkoff date,
                    break_date date,
                    last_completion date,
                    current_streak_period integer DEFAULT 0,
                    longest_streak_period integer DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
        )""")

        # creates the table for checks in the db with the primary key check_id and
        # the foreign keys user_id and habit_id
        c.execute("""CREATE TABLE IF NOT EXISTS checks (
                    check_id int PRIMARY KEY,
                    user_id text,
                    habit_id text,
                    check_date date,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                    FOREIGN KEY (habit_id) REFERENCES habits (habit_id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
        )""")

        c.execute('pragma foreign_keys = on')

        db_close(conn)

    except Exception as e:
        print('[Unable to insert table]', e)


# deletes all database tables for user, habits and checks
def db_clear() -> None:
    try:
        """Drops all tables (user, habit and checks) of the habit tracker database.
        """
        c, conn = db_open()

        c.execute("""DROP TABLE users""")
        c.execute("""DROP TABLE habits""")
        c.execute("""DROP TABLE checks""")

    except Exception as e:
        print('[Unable to clear tables]', e)

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# **********************************************************************
# Habit functions regarding a habit of a user in the db table habits
# **********************************************************************
# Gets a single habit data for a user
def db_get_habit(user_id, habit_id) -> list:
    """
    returns the content of a single habit for a selected user
    :param user_id:
    :param habit_id:
    :return: a list of one habit
    """
    try:
        c, conn = db_open()

        # sqlite command
        sqlite_query = """SELECT * FROM habits WHERE user_id = ? AND habit_id = ?"""
        # sqlite parameters
        column_values = (user_id, habit_id,)
        # execute sqlite command
        c.execute(sqlite_query, column_values)
        # c.execute("""SELECT * FROM habits WHERE user_id = ? AND habit_id = ?""", (user_id, habit_id,))

        habit = c.fetchall()
        return habit

    except sqlite3.Error as error:
        print("Failed to get habit data of a single habit for a user from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# gets all habits for a user
def db_get_all_habits_of_user(user_id) -> list:
    """
    returns the content of all habits for a selected users
    :param user_id:
    :return: a list of all habits from the user
    """
    try:
        c, conn = db_open()

        sqlite_query = """SELECT * From habits WHERE user_id = ?"""
        column_values = (user_id, )
        c.execute(sqlite_query, column_values)

        all_habits = c.fetchall()
        return all_habits

    except sqlite3.Error as error:
        print("Failed to get all habit data of a single user from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# gets all habits for all user
def db_get_all_habits() -> list:
    """
    returns all habits of all users
    :return: a list of all habits
    """
    try:
        c, conn = db_open()

        sqlite_query = """SELECT * From habits"""
        column_values = ()
        c.execute(sqlite_query, column_values)

        all_habits = c.fetchall()
        return all_habits

    except sqlite3.Error as error:
        print("Failed to get all habit data of a single user from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# Insert a habit for a user
def db_add_habit(user_id, habit_id, description, category,
                 start_date, stop_date, periodicity) -> None:
    """
    Inserts a habit for a selected users
    :param user_id:
    :param habit_id:
    :param description:
    :param category:
    :param start_date:
    :param stop_date:
    :param periodicity:
    :return: None
    """
    try:
        c, conn = db_open()

        sqlite_query = """INSERT INTO habits (habit_id, user_id, description, category, 
                       start_date, stop_date, periodicity) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        column_values = (habit_id, user_id, description, category, start_date, stop_date, periodicity)
        c.execute(sqlite_query, column_values)

    except sqlite3.Error as error:
        print("Failed to insert habit data into sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# Update an existing habit for a user
def db_update_habit(habit_id, user_id, description, category,
                    start_date, stop_date, periodicity) -> None:
    """
    updates an existing habit for a selected users
    :param habit_id:
    :param user_id:
    :param description:
    :param category:
    :param start_date:
    :param stop_date:
    :param periodicity:
    :return: None
    """
    try:
        c, conn = db_open()

        sqlite_query = """UPDATE habits SET description = ?, category = ?, start_date = ?, stop_date = ?, 
                                periodicity = ? WHERE user_id =? AND habit_id = ?"""
        column_values = (description, category, start_date, stop_date, periodicity, user_id, habit_id)
        c.execute(sqlite_query, column_values)

    except sqlite3.Error as error:
        print("Failed to update habit data into sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# Updates habit track data for a user
def db_update_habit_track_data(habit_id, user_id, last_checkoff, break_date, last_completion_date,
                               current_streak_period, longest_streak_period) -> None:
    """
    updates habit track data for an existing habit for a selected users
    :param habit_id:
    :param user_id:
    :param last_checkoff:
    :param break_date:
    :param last_completion_date:
    :param current_streak_period:
    :param longest_streak_period:
    :return: None
    """
    try:
        c, conn = db_open()

        sqlite_query = """UPDATE habits SET last_checkoff = ?, break_date = ?, last_completion = ?, 
                            current_streak_period = ?, longest_streak_period = ? WHERE user_id =? AND habit_id = ?"""
        column_values = (last_checkoff, break_date, last_completion_date, current_streak_period, longest_streak_period,
                         user_id, habit_id)
        c.execute(sqlite_query, column_values)

    except sqlite3.Error as error:
        print("Failed to update habit data into sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# Delete a habit for a user
def db_delete_habit(habit_id, user_id) -> None:
    """
    deletes an existing habit for a selected users
    :param habit_id:
    :param user_id:
    :return: None
    """
    try:
        c, conn = db_open()

        sqlite_query = """DELETE FROM habits WHERE user_id = ? AND habit_id = ?"""
        column_values = (user_id, habit_id)
        c.execute(sqlite_query, column_values)

    except sqlite3.Error as error:
        print("Failed to delete habit data from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# **********************************************************************
# User functions regarding the db table users
# **********************************************************************
# get user list
def db_get_all_users() -> list:
    """
    gets the content of all users of the db
    :return: list of users
    """
    try:
        c, conn = db_open()

        # get list of all users from db
        # c.execute("""SELECT * FROM users""")
        sqlite_query = """SELECT * FROM users"""
        column_values = ()
        c.execute(sqlite_query, column_values)
        all_users = c.fetchall()
        return all_users

    except sqlite3.Error as error:
        print("Failed to get all data for a all users from sqlite table user")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# get a single user list
def db_get_single_user(user_id) -> list:
    """
    gets content of a single user from the db
    :param user_id:
    :return: list with data of a single user
    """
    try:
        c, conn = db_open()

        # get list of a user from db
        # c.execute("""SELECT * From users WHERE user_id = ?""", (user_id,))
        sqlite_query = """SELECT * From users WHERE user_id = ?"""
        column_values = (user_id,)
        c.execute(sqlite_query, column_values)
        single_user = c.fetchall()
        return single_user

    except sqlite3.Error as error:
        print("Failed to get user data for a single user from sqlite table user")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# Insert user
def db_add_user(user_id, name, description) -> None:
    """
    Inserts a user into the users-table of the db
    :param user_id:
    :param name:
    :param description:
    :return: None
    """
    try:
        c, conn = db_open()

        # insert user to db
        # c.execute("""INSERT INTO users VALUES(:user_id, :name ,:description)""", (user_id, name, description))
        sqlite_query = """INSERT INTO users VALUES(:user_id, :name ,:description)"""
        column_values = (user_id, name, description)
        c.execute(sqlite_query, column_values)

    except sqlite3.Error as error:
        print("Failed to add user into sqlite table user")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# Update user
def db_update_user(user_id, name, description) -> None:
    """
    updates users in the user table of the db.
    :param user_id:
    :param name:
    :param description:
    :return: None
    """
    try:
        c, conn = db_open()

        # update user to db
        # c.execute(""" UPDATE users SET name = ?, description = ? WHERE user_id = ?""", (name, description, user_id))
        sqlite_query = """UPDATE users SET name = ?, description = ? WHERE user_id = ?"""
        column_values = (name, description, user_id)
        c.execute(sqlite_query, column_values)

    except sqlite3.Error as error:
        print("Failed to update user data into sqlite table user")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# Delete user
def db_del_user(user_id) -> None:
    """
    Deletes a user from the user table of the db
    :param user_id:
    :return: None
    """
    try:
        c, conn = db_open()

        # insert user to db
        c.execute("""DELETE FROM users WHERE user_id = ?""", (user_id,))
        sqlite_query = """DELETE FROM users WHERE user_id = ?"""
        column_values = (user_id,)
        c.execute(sqlite_query, column_values)

    except sqlite3.Error as error:
        print("Failed to delete user from table user")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# **********************************************************************
# Check functions regarding a habit of a user in the db table checks
# **********************************************************************
# Check habit
def db_add_check_habit(check_id, user_id, habit_id, check_datetime) -> None:
    """
    Checks a habit for the active user
    :param check_id:
    :param user_id:
    :param habit_id:
    :param check_datetime:
    :return: None
    """
    try:
        c, conn = db_open()

        # check a habit for the active user
        sqlite_query = """INSERT INTO checks VALUES(:check_id, :user_id, :habit_id, :date)"""
        column_values = (check_id, user_id, habit_id, check_datetime)
        c.execute(sqlite_query, column_values)

    except sqlite3.Error as error:
        print("Failed to put in a check_date for a habit of the selected user to table checks")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


def db_view_checks(user_id, habit_id) -> list:
    """
    view all checks of a user for a habit out of db
    :param user_id:
    :param habit_id:
    :return: list of checks data
    """
    try:
        c, conn = db_open()

        # view all checks for a habit of the active user
        sqlite_query = """SELECT * FROM checks WHERE user_id = ? AND habit_id = ?"""
        column_values = (user_id, habit_id)
        c.execute(sqlite_query, column_values)
        checks = c.fetchall()
        return checks

    except sqlite3.Error as error:
        print("Failed to get all checks for a habit from the active user from sqlite table checks")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


def db_view_all_checks() -> list:
    """
    view all checks of all users for all habits out of db
    :return: list of all check data
    """
    try:
        c, conn = db_open()

        # view all checks for a habit of the active user
        sqlite_query = """SELECT * FROM checks """
        column_values = ()
        c.execute(sqlite_query, column_values)
        checks = c.fetchall()
        return checks

    except sqlite3.Error as error:
        print("Failed to get all checks for a habit from the active user from sqlite table checks")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# **********************************************************************
# track data update function for calculating analysing data
# of a habit of a user in table habits
# **********************************************************************
# gets all habit track data of a user for one habit
def db_get_habit_track_data(user_id, habit_id) -> list:
    """
    returns the content habit track data of a habit for a selected users
    :param user_id:
    :param habit_id:
    :return: list of habit track data
    """
    try:
        c, conn = db_open()

        sqlite_query = """SELECT break_date, last_completion, current_streak_period, longest_streak_period,
        From habits WHERE user_id = ? AND habit_id = ?"""
        column_values = (user_id, habit_id,)
        c.execute(sqlite_query, column_values)

        habit_track_data = c.fetchall()
        return habit_track_data

    except sqlite3.Error as error:
        print("Failed to get habit data of a single habit for a user from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# get all struggled habits of a user
def db_get_struggled_habits(user_id) -> list:
    """
    returns all struggled habits of a user
    :param user_id:
    :return: list of struggled habits
    """
    try:
        c, conn = db_open()

        sqlite_query = """SELECT * FROM habits WHERE (user_id = ? AND 
                          (break_date >= start_date AND break_date <= stop_date))"""
        column_values = (user_id, )
        c.execute(sqlite_query, column_values)

        habit_track_data = c.fetchall()
        return habit_track_data

    except sqlite3.Error as error:
        print("Failed to get habit data of a single habit for a user from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# gets the longest streaks of all habits for a user
def db_get_longest_streaks_of_all_habits(user_id) -> list:
    """
    gets the longest streaks of all habits for a user
    :param user_id:
    :return: list with the longest streaks
    """
    try:
        c, conn = db_open()

        sqlite_query = """SELECT habit_id, user_id, description, category, start_date, stop_date, periodicity, 
                        current_streak_period, longest_streak_period FROM habits WHERE user_id = ?"""
        column_values = (user_id,)
        c.execute(sqlite_query, column_values)

        habit_track_data = c.fetchall()
        return habit_track_data

    except sqlite3.Error as error:
        print("Failed to get habit data of a single habit for a user from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")


# gets the longest streak of one habit for a user
def db_get_longest_streaks_of_habit(user_id, habit_id) -> list:
    """
    gets the longest streak of one habit for a user
    :param user_id:
    :param habit_id:
    :return: list with the longest streak
    """
    try:
        c, conn = db_open()

        sqlite_query = """SELECT habit_id, user_id, description, category, start_date, stop_date, periodicity, 
                        current_streak_period, longest_streak_period FROM habits WHERE user_id = ? AND habit_id = ?"""
        column_values = (user_id, habit_id,)
        c.execute(sqlite_query, column_values)

        habit_track_data = c.fetchall()
        return habit_track_data

    except sqlite3.Error as error:
        print("Failed to get habit data of a single habit for a user from sqlite table habit")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    finally:
        if conn:
            db_close(conn)
            # print(" Sqlite connection closed")
