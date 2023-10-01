# -------------------------------------------------------------------------
#    Class Habit
#    Author: Eder Alois
# -------------------------------------------------------------------------
import database.habit_db as db
from datetime import date
from classes.example import import_habits, import_checks
from database.habit_analyse import update_habit_track_data


class Habit:
    def __init__(self, habit_id: str,
                 user_id: str, habit_description: str, habit_category: str,
                 habit_start: date, habit_stop: date, habit_period: str,
                 # habit_status: int, habit_last_completed: str,
                 # habit_streak_days: int, habit_longest_streak_days: int
                 ):
        """
        Constructor for a new habit, the habit will be written in the db for the active user

        :param user_id:
        :param habit_id:
        :param habit_description:
        :param habit_category:
        :param habit_start:
        :param habit_stop:
        :param habit_period:
        """
        self.habit_id = habit_id
        self.user_id = user_id
        self.habit_description = habit_description
        self.habit_category = habit_category
        self.habit_start = habit_start
        self.habit_stop = habit_stop
        self.habit_period = habit_period

    def get_all_habits_of_user(self, user_id) -> list:
        """
        get all hab habits for a user
        :param user_id:
        :return: list of habits
        """
        return db.db_get_all_habits_of_user(user_id=user_id)

    def get_all_habits(self) -> list:
        """
        get all habits for all user
        :return: list of habits
        """
        return db.db_get_all_habits()

    def get_single_habit(self, user_id, habit_id) -> list:
        """
        get a single habit for a user
        :param user_id:
        :param habit_id:
        :return:
        """
        return db.db_get_habit(user_id=user_id, habit_id=habit_id)

    def add_habit(self) -> None:
        """
        add a habit to the tables of the db
        :return: None
        """
        # def add_habit(self, user_id, habit_id, description, category,
        #               start_date, duration, periodicity):
        db.db_add_habit(user_id=self.user_id, habit_id=self.habit_id, description=self.habit_description,
                        category=self.habit_category, start_date=self.habit_start, stop_date=self.habit_stop,
                        periodicity=self.habit_period)

    def modify_habit(self, user_id, habit_id, description, category,
                     start_date, stop_date, periodicity) -> None:
        """
        modifies an existing habit of a user in the db
        :param user_id:
        :param habit_id:
        :param description:
        :param category:
        :param start_date:
        :param stop_date:
        :param periodicity:
        :return: None
        """
        db.db_update_habit(user_id=user_id, habit_id=habit_id, description=description, category=category,
                           start_date=start_date, stop_date=stop_date, periodicity=periodicity)

    def delete_habit(self, user_id, habit_id) -> None:
        """
        deletes a habit of a user in the db
        :param user_id:
        :param habit_id:
        :return: None
        """
        db.db_delete_habit(user_id=user_id, habit_id=habit_id)

    def check_habit(self, user_id, habit_id, check_date) -> None:
        """
        checks a habit for a user the in the table checks of the db,
        calculates the new tracking data and stores the new tracking values in the habit table of the db
        :param user_id:
        :param habit_id:
        :param check_date:
        :return: None
        """
        # generate a new unique Check_id
        temp_list = db.db_view_all_checks()
        if not temp_list:
            ident = 0
        else:
            id_temp = (max(temp_list)[0])
            ident = id_temp + 1

        # add the new check to the db
        db.db_add_check_habit(check_id=ident, user_id=user_id, habit_id=habit_id, check_datetime=check_date)
        # calculates the new tracking data and store the new values in the db
        update_habit_track_data(user_id=user_id, habit_id=habit_id,
                                current_date=check_date, check_state=True)

    def get_checks(self, user_id, habit_id) -> list:
        """
        reads a check data for a habit of a user
        :param user_id:
        :param habit_id:
        :return:  list of check data
        """
        return db.db_view_checks(user_id=user_id, habit_id=habit_id)

    def import_habit_list(self) -> None:
        """
        import habits from a list in the file example.py
        this is used for test purpose only
        :return: None
        """
        for habit in import_habits:
            print(habit)
            db.db_add_habit(habit_id=habit['habit_id'], user_id=habit['user_id'],
                            description=habit['habit_description'], category=habit['habit_category'],
                            start_date=habit['habit_start'], stop_date=habit['habit_stop'],
                            periodicity=habit['habit_period'])

    def import_check_list(self) -> None:
        """
        import checks from a list in the file example.py and stores it in the db
        this is used for test purpose only
        calculates the new tracking data and stores the new tracking values in the habit table of the db
        :return: None
        """
        for check in import_checks:
            print(check)
            db.db_add_check_habit(check_id=check['check_id'], user_id=check['user_id'], habit_id=check['habit_id'],
                                  check_datetime=check['check_date'])
            # calculates the new tracking data and store the new values in the db
            update_habit_track_data(user_id=check['user_id'], habit_id=check['habit_id'],
                                    current_date=check['check_date'], check_state=True)
