# -------------------------------------------------------------------------
#    Class Habit Analysing functions
#    Author: Eder Alois
# -------------------------------------------------------------------------
import database.habit_db as db
from datetime import date, datetime


def hba_get_habit_list_with_period(user_id, periodicity) -> list:
    """
    generates a list of habits for a user with the periodicity
    :param user_id:
    :param periodicity:
    :return: list of habits
    """
    return_list = []
    # get a list of all habits of user user_id
    temp_list = db.db_get_all_habits_of_user(user_id)
    # generates a list of habits with requested periodicity
    for habit in temp_list:
        habit_period = habit[6]
        if habit_period == periodicity:
            return_list.append(habit)
    return return_list


def hba_get_active_habits(user_id) -> list:
    """
    Get all habits of user user_id which are started before and not finished till the actual day
    :param user_id:
    :return: list of active habits
    """
    return_list = []
    # get a list of all habits of user user_id
    temp_list = db.db_get_all_habits_of_user(user_id)
    # get current date time and append habit to a list if actual date is between start day and stop day
    current_date = datetime.now()
    date_format = '%Y-%m-%d'
    for habit in temp_list:
        # print(type(habit))
        habit_start_day = datetime.strptime(habit[4], date_format)
        habit_stop_day = datetime.strptime(habit[5], date_format)
        if habit_start_day < current_date < habit_stop_day:
            return_list.append(habit)
    return return_list


def hba_get_struggled_habits(user_id) -> list:
    """
    get a list of struggled habits of a user
    struggled: if break date between start and stop date
    one time struggled the habit is marked as struggled
    :param user_id:
    :return: list of habits
    """
    temp_list = db.db_get_struggled_habits(user_id)
    return temp_list


def hba_get_daily_habits(user_id) -> list:
    """
    get a list of daily habits for a user
    :param user_id:
    :return: list of habits
    """
    periodicity = "d"
    return hba_get_habit_list_with_period(user_id, periodicity)


def hba_get_weekly_habits(user_id) -> list:
    """
    get a list of weekly habits for a user
    :param user_id:
    :return: list of habits
    """
    periodicity = "w"
    return hba_get_habit_list_with_period(user_id, periodicity)


def hba_get_monthly_habits(user_id) -> list:
    """
    get a list of monthly habits for a user
    :param user_id:
    :return: list of habits
    """
    periodicity = "m"
    return hba_get_habit_list_with_period(user_id, periodicity)


def hba_get_streaks_of_habit(user_id, habit_id) -> list:
    """
    get the streaks (longest and current) for a habit of one user (active user)
    :param user_id:
    :param habit_id:
    :return: list of habit data
    """
    # get a habit of user user_id and habit habit_id
    temp_list = db.db_get_longest_streaks_of_habit(user_id=user_id, habit_id=habit_id)
    return temp_list


def hba_get_longest_run_streaks_of_all_habits(user_id) -> list:
    """
    get the streaks (longest and current) off all habits for a user (active user)
    :param user_id:
    :return: list of habits data
    """
    return_list = []
    # get a list of all habits of user user_id
    temp_list = db.db_get_longest_streaks_of_all_habits(user_id)
    for habit in temp_list:
        return_list.append(habit)

    return return_list


def hba_get_longest_run_streak_of_habit(user_id, habit_id) -> list:
    """
    get the streak (longest) for a habit of one user (active user)
    :param user_id:
    :param habit_id:
    :return: list of habit data
    """
    print(f"Longest run streak of habit: {habit_id} of User: {user_id}")

    # get a habits of user user_id and habit habit_id
    temp_list = db.db_get_longest_streaks_of_habit(user_id=user_id, habit_id=habit_id)

    return temp_list


def hba_check_periodicity(period, current_date, last_check) -> bool:
    """
    checks the periodicity of between the current_date and last_check and return True if correct, otherwise False
    period could be daily (d), weekly (w) or monthly (m)
    :param period:
    :param current_date:
    :param last_check:
    :return:
    """
    periodicity = False
    # select the days for the different periods
    if period == "d":
        period_time = 1
    elif period == "w":
        period_time = 7
    else:
        period_time = 30

    # calculate the difference between current_date and last_check in days
    period_days = current_date - last_check
    if int(period_days.days) <= period_time:
        periodicity = True
    return periodicity


def hba_calculate_streak_status(start_date, stop_date, period, current_date,
                                last_checkoff, break_date, last_completion_date,
                                current_streak_period, longest_streak_period):
    """
    calculates the new streak status of a habit after a new check is received
    :param start_date:
    :param stop_date:
    :param period:
    :param current_date:
    :param last_checkoff:
    :param break_date:
    :param last_completion_date:
    :param current_streak_period:
    :param longest_streak_period:
    :return: habit date
    """
    # check if current day == start day, then first check off, last completion set, streak_data set to 1
    # Check if current day is within start and stop
    # check if current day is within the periodicity, if so update all data break date is not set
    # if not break day is set , update other values
    # if break_day is set

    if current_date < start_date:
        # Habit is not started, checkoff is not possible
        print("**** Sorry, habit not started: Please check habit data ****")
    elif current_date == start_date:
        # start of habit, and first checkoff
        last_checkoff = current_date
        break_date = date(1900, 1, 1)  # default value for break date
        last_completion_date = current_date
        # both streak counter set to 1
        current_streak_period = 1
        longest_streak_period = 1
    elif start_date < current_date <= stop_date:
        # habit checks between start and stop day
        if hba_check_periodicity(period=period, current_date=current_date, last_check=last_checkoff):
            # periodicity check true
            last_checkoff = current_date
            # break_date = date(1900, 1, 1)
            last_completion_date = current_date
            current_streak_period += 1  # increment current streak
            # set longest_streak to current streak only if current_streak greater than longest_streak
            longest_streak_period = longest_streak_period
            if current_streak_period > longest_streak_period:
                longest_streak_period = current_streak_period
        else:
            # periodicity check false
            last_checkoff = current_date
            break_date = current_date  # set break date to current date
            last_completion_date = last_completion_date
            current_streak_period = 1  # set current streak to 1
            longest_streak_period = longest_streak_period
    elif current_date > stop_date:
        # Habit is not stopped, checkoff is not possible
        print("**** Sorry, habit finished: Please check habit data ****")
    return last_checkoff, break_date, last_completion_date, current_streak_period, longest_streak_period


def update_habit_track_data(habit_id, user_id, current_date, check_state) -> None:
    """
    Updates the db-data for check status, last completion and streaks
    calls the function for calculation of streaks
    :param habit_id:
    :param user_id:
    :param current_date:
    :param check_state:
    :return:
    """
    # get start day, stop_day, periodicity, last completion of habit for selected user
    habit_data = db.db_get_habit(user_id=user_id, habit_id=habit_id)

    date_format = '%Y-%m-%d'
    # extract the start date to the correct format
    temp = habit_data[0][4]
    start_date = datetime.strptime(temp, date_format)
    start_date = date(year=start_date.year,
                      month=start_date.month,
                      day=start_date.day)
    # extract the stop date to the correct format
    temp = habit_data[0][5]
    stop_date = datetime.strptime(temp, date_format)
    stop_date = date(year=stop_date.year,
                     month=stop_date.month,
                     day=stop_date.day)
    # extract the periodicity
    periodicity = habit_data[0][6]
    # extract the last_checkOff date to the correct format, if empty, set to default date
    temp = habit_data[0][7]
    if not temp:
        last_checkoff = date(1900, 1, 1)
    else:
        last_checkoff = datetime.strptime(temp, date_format)
        last_checkoff = date(year=last_checkoff.year,
                             month=last_checkoff.month,
                             day=last_checkoff.day)
    # extract the break date to the correct format, if empty, set to default date
    temp = habit_data[0][8]
    if not temp:
        break_date = date(1900, 1, 1)
    else:
        break_date = datetime.strptime(temp, date_format)
        break_date = date(year=break_date.year,
                          month=break_date.month,
                          day=break_date.day)
    # extract the last_completion date to the correct format, if empty, set to default date
    temp = habit_data[0][9]
    if not temp:
        last_completion = date(1900, 1, 1)
    else:
        last_completion = datetime.strptime(temp, date_format)
        last_completion = date(year=last_completion.year,
                               month=last_completion.month,
                               day=last_completion.day)
    # extract the streak values
    current_streak_period = habit_data[0][10]
    longest_streak_period = habit_data[0][11]

    current_date = date(
        year=current_date.year,
        month=current_date.month,
        day=current_date.day)

    # calculate current and longest streak
    (last_checkoff, break_date, last_completion,
     current_streak_period,
     longest_streak_period) = hba_calculate_streak_status(start_date=start_date, stop_date=stop_date,
                                                          current_date=current_date, period=periodicity,
                                                          last_checkoff=last_checkoff, break_date=break_date,
                                                          last_completion_date=last_completion,
                                                          current_streak_period=current_streak_period,
                                                          longest_streak_period=longest_streak_period)

    # put last completion, current streak period and longest streak period in db
    db.db_update_habit_track_data(user_id=user_id, habit_id=habit_id, last_checkoff=last_checkoff,
                                  break_date=break_date, last_completion_date=last_completion,
                                  current_streak_period=current_streak_period,
                                  longest_streak_period=longest_streak_period)
