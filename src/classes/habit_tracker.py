# -------------------------------------------------------------------------
#    Class Habit Tracker
#    Author: Eder Alois
# -------------------------------------------------------------------------
import pandas as pd
import database.habit_analyse as hba


class HabitTracker:
    # column frame for the panda library for all habit data
    columns_frame = ['Habit_id', 'User_id', 'habit_description', 'habit_category',
                     'habit_start', 'habit_stop', 'habit_period',
                     'Last Check', 'Break', 'last_completion',
                     'streak_periods', 'longest_streak_period']

    # column frame for the panda library for habit streak data
    columns_streak_data = ['Habit_id', 'User_id', 'habit_description', 'habit_category',
                           'habit_start', 'habit_stop', 'habit_period',
                           'streak_periods', 'longest_streak_period']

    def view_active_habits(self, user_id) -> list:
        """
        views and gets all active habits of a user
        :param user_id:
        :return: list of habits
        """
        print(f"Active habits of user: {user_id}")
        habit_list = hba.hba_get_active_habits(user_id)
        # use of panda data frame function to show the habit list
        df = pd.DataFrame(habit_list, columns=HabitTracker.columns_frame, index=None)
        print(df)
        return habit_list

    def view_struggled_habits(self, user_id) -> list:
        """
        views and gets all struggled habits of a user
        :param user_id:
        :return: list of habits
        """
        print(f"Struggled habits of user: {user_id}")
        habit_list = hba.hba_get_struggled_habits(user_id)
        # use of panda data frame function to show the habit list
        df = pd.DataFrame(habit_list, columns=HabitTracker.columns_frame, index=None)
        print(df)
        return habit_list

    def view_daily_habits(self, user_id) -> list:
        """
        views and gets all daily habits of a user
        :param user_id:
        :return: list of habits
        """
        print(f"Daily habits of user: {user_id}")
        habit_list = hba.hba_get_daily_habits(user_id)
        # use of panda data frame function to show the habit list
        df = pd.DataFrame(habit_list, columns=HabitTracker.columns_frame, index=None)
        print(df)
        return habit_list

    def view_weekly_habits(self, user_id) -> list:
        """
        views and gets all weekly habits of a user
        :param user_id: 
        :return:  list of habits
        """
        print(f"Weekly habits of user: {user_id}")
        habit_list = hba.hba_get_weekly_habits(user_id)
        # use of panda data frame function to show the habit list
        df = pd.DataFrame(habit_list, columns=HabitTracker.columns_frame, index=None)
        print(df)
        return habit_list

    def view_monthly_habits(self, user_id) -> list:
        """
        views and gets all monthly habits of a user
        :param user_id:
        :return: list of habits
        """
        print(f"Monthly habits of user: {user_id}")
        habit_list = hba.hba_get_monthly_habits(user_id)
        # use of panda data frame function to show the habit list
        df = pd.DataFrame(habit_list, columns=HabitTracker.columns_frame, index=None)
        print(df)
        return habit_list

    def view_streaks_of_habit(self, user_id, habit_id) -> list:
        """
        views and gets current streak and habit data of one habit for a user
        :param user_id:
        :param habit_id:
        :return: list of habit data
        """
        print(f"Streaks of habits: {habit_id} of user: {user_id}")
        habit_list = hba.hba_get_streaks_of_habit(user_id=user_id, habit_id=habit_id)
        # use of panda data frame function to show the habit list
        df = pd.DataFrame(habit_list, columns=HabitTracker.columns_streak_data, index=None)
        print(df)
        return habit_list

    def view_longest_run_streaks_of_all_habits(self, user_id) -> list:
        """
        views and gets the longest streak, current streak and habit data of all habit for a user
        :param user_id:
        :return: list of habit data
        """
        print(f"Longest run streak of all habits of User: {user_id}")
        habit_list = hba.hba_get_longest_run_streaks_of_all_habits(user_id)
        # use of panda data frame function to show the habit list
        df = pd.DataFrame(habit_list, columns=HabitTracker.columns_streak_data, index=None)
        print(df)
        return habit_list

    def view_longest_run_streak_of_habit(self, user_id, habit_id) -> list:
        """
        views and gets the longest streak, current streak and habit data of a habit for a user
        :param user_id:
        :param habit_id:
        :return:
        """
        print(f"Longest run streak of habit: {habit_id} of User: {user_id}")
        habit_list = hba.hba_get_longest_run_streak_of_habit(user_id=user_id, habit_id=habit_id)
        # use of panda data frame function to show the habit list
        df = pd.DataFrame(habit_list, columns=HabitTracker.columns_streak_data, index=None)
        print(df)
        return habit_list
