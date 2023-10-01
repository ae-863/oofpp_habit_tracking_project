from datetime import date
from database import habit_db as habit_db
from classes import user as user
from classes import habit as habit
from classes import habit_tracker as habit_tracker

import sys
sys.path.append("../../oofpp_habit_tracking_project/src")  # folder that contains database


class TestHabit:
    def setup_method(self):
        # setting up db
        habit_db.db_clear()
        habit_db.db_init()
        # setup a user 1
        user01 = user.User("U_01", "Test_User_01", "desc_01")
        user01.add_user()

        # add 2 Habits
        # Add Habit 1 for User 1
        habit01 = habit.Habit('H_01', 'U_01', 'H_01_descr', 'Cat_01',
                              date(2023, 9, 20), date(2023, 12, 31),
                              'd')
        habit01.add_habit()
        # Add habit 2 for User 1
        habit02 = habit.Habit('H_02', 'U_01', 'H_02_descr', 'Cat_02',
                              date(2024, 1, 1), date(2024, 2, 28),
                              'w')
        habit02.add_habit()
        # Add habit 3 for User 1
        habit03 = habit.Habit('H_03', 'U_01', 'H_03_descr', 'Cat_03',
                              date(2023, 9, 1), date(2023, 12, 31),
                              'w')
        habit03.add_habit()
        # Add habit 4 for User 1
        habit04 = habit.Habit('H_04', 'U_01', 'H_04_descr', 'Cat_03',
                              date(2023, 9, 1), date(2023, 12, 31),
                              'd')
        habit04.add_habit()

        # set user 1 active
        user01.set_active_user('U_01')
        active_user_id = user.User.active_user_id
        assert active_user_id == 'U_01'

    # Testfunction with 1 habit, checks with period daily for an active habit
    def test_check_habit1(self):
        temp_habit = habit.Habit("", "", "", "",
                                 date(2022, 1, 1), date(2022, 1, 1), "")
        temp_habit_tracker = habit_tracker.HabitTracker()

        # get active habit of user 01 and check data
        temp_list = temp_habit_tracker.view_active_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period

        # check dates for Habit 1 (Start: 2023-09-20; Stop 2023-10-31; daily
        # check 2023-09-20 - 2023-09-26
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 20))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 21))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 22))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 23))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 24))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 25))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 26))
        # verify habit data
        temp_list = temp_habit_tracker.view_active_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][10] == 7  # current streak period
        assert temp_list[0][11] == 7  # longest streak period

        # check 2023-09-28 - 2023-09-29
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 28))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 29))
        # verify habit streak data
        temp_list = temp_habit_tracker.view_streaks_of_habit('U_01', 'H_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][7] == 2  # current streak period
        assert temp_list[0][8] == 7  # longest streak period

        # check 2023-10-01: --> current streak = 1
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 1))
        # verify habit streak data
        temp_list = temp_habit_tracker.view_streaks_of_habit('U_01', 'H_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][7] == 1  # current streak period
        assert temp_list[0][8] == 7  # longest streak period

        # check 2023-10-03 - 2023-10-11: --> current streak = 9, longest streak = 9
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 3))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 4))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 5))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 6))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 7))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 8))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 9))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 10))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 11))
        # verify habit track data
        temp_list = temp_habit_tracker.view_streaks_of_habit('U_01', 'H_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][7] == 9  # current streak period
        assert temp_list[0][8] == 9  # longest streak period

        # check 2023-10-13: --> current streak = 1, longest streak = 9
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 10, 13))
        # verify habit streak data
        temp_list = temp_habit_tracker.view_streaks_of_habit('U_01', 'H_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][7] == 1  # current streak period
        assert temp_list[0][8] == 9  # longest streak period

    # Testfunction with 1 habit, checks with different periods for an inactive habit
    def test_check_habit2(self):
        temp_habit = habit.Habit("", "", "", "",
                                 date(2022, 1, 1), date(2022, 1, 1), "")
        # temp_habit_tracker = habit_tracker.HabitTracker()

        # get not active habit of user 01 and check data
        temp_list = temp_habit.get_single_habit('U_01', 'H_02')
        assert temp_list[0][0] == 'H_02'  # habit_id
        assert temp_list[0][4] == '2024-01-01'  # start date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period

        # check dates for Habit 2 (Start: 2023-10-01; Stop 2023-12-31; daily
        # check 2023-09-20 - 2023-09-26
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_02', date(2023, 9, 20))

        # get not active habit of user 01 and check data
        temp_list = temp_habit.get_single_habit('U_01', 'H_02')
        assert temp_list[0][0] == 'H_02'  # habit_id
        assert temp_list[0][4] == '2024-01-01'  # start date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period

    # Testfunction with 1 habit, checks with period daily for a break date and last completion on an active habit
    def test_check_habit3(self):
        temp_habit = habit.Habit("", "", "", "",
                                 date(2022, 1, 1), date(2022, 1, 1), "")
        temp_habit_tracker = habit_tracker.HabitTracker()

        # get active habit of user 01 and check data
        temp_list = temp_habit_tracker.view_active_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period

        # check dates for Habit 1 (Start: 2023-09-20; Stop 2023-10-31; daily
        # check 2023-09-20 - 2023-09-21
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 20))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 21))
        # verify habit data
        temp_list = temp_habit_tracker.view_active_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][7] == '2023-09-21'  # last check date
        assert temp_list[0][8] == '1900-01-01'  # break date
        assert temp_list[0][9] == '2023-09-21'  # last completion date
        assert temp_list[0][10] == 2  # current streak period
        assert temp_list[0][11] == 2  # longest streak period

        # check dates for Habit 1 (Start: 2023-09-20; Stop 2023-10-31; daily
        # check 2023-09-23
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 23))
        # verify habit data
        temp_list = temp_habit_tracker.view_active_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][7] == '2023-09-23'  # last check date
        assert temp_list[0][8] == '2023-09-23'  # break date
        assert temp_list[0][9] == '2023-09-21'  # last completion date
        assert temp_list[0][10] == 1  # current streak period
        assert temp_list[0][11] == 2  # longest streak period

        # check 2023-09-24
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 24))
        # verify habit data
        temp_list = temp_habit_tracker.view_active_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][7] == '2023-09-24'  # last check date
        assert temp_list[0][8] == '2023-09-23'  # break date
        assert temp_list[0][9] == '2023-09-24'  # last completion date
        assert temp_list[0][10] == 2  # current streak period
        assert temp_list[0][11] == 2  # longest streak period

        # check 2023-09-25
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 25))
        # verify habit data
        temp_list = temp_habit_tracker.view_active_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][7] == '2023-09-25'  # last check date
        assert temp_list[0][8] == '2023-09-23'  # break date
        assert temp_list[0][9] == '2023-09-25'  # last completion date
        assert temp_list[0][10] == 3  # current streak period
        assert temp_list[0][11] == 3  # longest streak period

    # Testfunction 4 with 1 inactive habit, checks with period daily for a not active habit --> no update done
    def test_check_habit4(self):
        temp_habit = habit.Habit("", "", "", "",
                                 date(2022, 1, 1), date(2022, 1, 1), "")

        # get inactive habit of user 01 and check data
        temp_list = temp_habit.get_single_habit('U_01', 'H_02')
        assert temp_list[0][0] == 'H_02'  # habit_id
        assert temp_list[0][4] == '2024-01-01'  # start date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period

        # check dates for Habit 2 (Start: 2024-01-01; Stop 2024-02-28; daily
        # check 2023-09-20
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_02', date(2023, 9, 20))
        # verify habit data
        temp_list = temp_habit.get_single_habit('U_01', 'H_02')
        assert temp_list[0][0] == 'H_02'  # habit_id
        assert temp_list[0][4] == '2024-01-01'  # start date
        assert temp_list[0][7] == '1900-01-01'  # last check date
        assert temp_list[0][8] == '1900-01-01'  # break date
        assert temp_list[0][9] == '1900-01-01'  # last completion date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period
    # Testfunction with 1 habit, checks with period weekly for an active habit

    # Testfunction 5 with 1 active habit, checks with period weekly for an active habit --> update on weekly basis
    def test_check_habit5(self):
        temp_habit = habit.Habit("", "", "", "",
                                 date(2022, 1, 1), date(2022, 1, 1), "")
        # temp_habit_tracker = habit_tracker.HabitTracker()

        # get active habit of user 01 and check data
        temp_list = temp_habit.get_single_habit('U_01', 'H_03')
        assert temp_list[0][0] == 'H_03'  # habit_id
        assert temp_list[0][4] == '2023-09-01'  # start date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period

        # check dates for Habit 3 (Start: 2023-09-01; Stop 2023-12-31; weekly
        # check 2023-09-02 - 2023-09-29
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 1))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 6))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 13))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 19))
        # verify habit data
        temp_list = temp_habit.get_single_habit('U_01', 'H_03')
        assert temp_list[0][0] == 'H_03'  # habit_id
        assert temp_list[0][4] == '2023-09-01'  # start date
        assert temp_list[0][7] == '2023-09-19'  # last check date
        assert temp_list[0][8] == '1900-01-01'  # break date
        assert temp_list[0][9] == '2023-09-19'  # last completion date
        assert temp_list[0][10] == 4  # current streak period
        assert temp_list[0][11] == 4  # longest streak period

    # Testfunction 6 with 1 active habit, checks with period weekly for an active habit
    # --> update with break on weekly basis
    def test_check_habit6(self):
        temp_habit = habit.Habit("", "", "", "",
                                 date(2022, 1, 1), date(2022, 1, 1), "")
        # temp_habit_tracker = habit_tracker.HabitTracker()

        # get active habit of user 01 and check data
        temp_list = temp_habit.get_single_habit('U_01', 'H_03')
        assert temp_list[0][0] == 'H_03'  # habit_id
        assert temp_list[0][4] == '2023-09-01'  # start date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period

        # check dates for Habit 3 (Start: 2023-09-01; Stop 2023-12-31; weekly
        # check 2023-09-02 - 2023-09-29
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 1))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 6))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 13))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 21))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 26))
        # verify habit data
        temp_list = temp_habit.get_single_habit('U_01', 'H_03')
        assert temp_list[0][0] == 'H_03'  # habit_id
        assert temp_list[0][4] == '2023-09-01'  # start date
        assert temp_list[0][7] == '2023-09-26'  # last check date
        assert temp_list[0][8] == '2023-09-21'  # break date
        assert temp_list[0][9] == '2023-09-26'  # last completion date
        assert temp_list[0][10] == 2  # current streak period
        assert temp_list[0][11] == 3  # longest streak period

    # Testfunction 7 with 1 active habit, checks with period weekly for an active habit ang give struggled habit
    # --> update with break on weekly basis
    def test_check_habit7(self):
        temp_habit = habit.Habit("", "", "", "",
                                 date(2022, 1, 1), date(2022, 1, 1), "")
        temp_habit_tracker = habit_tracker.HabitTracker()

        # get active habit of user 01 and check data
        temp_list = temp_habit.get_single_habit('U_01', 'H_03')
        assert temp_list[0][0] == 'H_03'  # habit_id
        assert temp_list[0][4] == '2023-09-01'  # start date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period

        # check dates for Habit 3 (Start: 2023-09-01; Stop 2023-12-31; weekly
        # check 2023-09-02 - 2023-09-29
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 1))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 6))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 13))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 21))
        # habit.Habit.check_habit(temp_habit, 'U_01', 'H_03', date(2023, 9, 26))
        # verify habit data
        temp_list = temp_habit.get_single_habit('U_01', 'H_03')
        assert temp_list[0][0] == 'H_03'  # habit_id
        assert temp_list[0][4] == '2023-09-01'  # start date
        assert temp_list[0][7] == '2023-09-21'  # last check date
        assert temp_list[0][8] == '2023-09-21'  # break date
        assert temp_list[0][9] == '2023-09-13'  # last completion date
        assert temp_list[0][10] == 1  # current streak period
        assert temp_list[0][11] == 3  # longest streak period

        temp_list = temp_habit_tracker.view_struggled_habits('U_01')
        assert temp_list[0][0] == 'H_03'  # habit_id
        assert temp_list[0][4] == '2023-09-01'  # start date
        assert temp_list[0][7] == '2023-09-21'  # last check date
        assert temp_list[0][8] == '2023-09-21'  # break date
        assert temp_list[0][9] == '2023-09-13'  # last completion date
        assert temp_list[0][10] == 1  # current streak period
        assert temp_list[0][11] == 3  # longest streak period

    # Testfunction 7 view check daily habits
    def test_check_habit8(self):
        temp_habit = habit.Habit("", "", "", "",
                                 date(2022, 1, 1), date(2022, 1, 1), "")
        temp_habit_tracker = habit_tracker.HabitTracker()

        # get daily habits of user 01 and check data
        # Habit 1
        temp_list = temp_habit_tracker.view_daily_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][1] == 'U_01'  # user_id
        assert temp_list[0][2] == 'H_01_descr'  # description
        assert temp_list[0][3] == 'Cat_01'  # category
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][5] == '2023-12-31'  # stop date
        assert temp_list[0][6] == 'd'  # periodicity
        assert temp_list[0][7] == None  # last check date
        assert temp_list[0][8] == None  # break date
        assert temp_list[0][9] == None  # last completion date
        assert temp_list[0][10] == 0  # current streak period
        assert temp_list[0][11] == 0  # longest streak period
        # Habit 4
        assert temp_list[1][0] == 'H_04'  # habit_id
        assert temp_list[1][1] == 'U_01'  # user_id
        assert temp_list[1][2] == 'H_04_descr'  # description
        assert temp_list[1][3] == 'Cat_03'  # category
        assert temp_list[1][4] == '2023-09-01'  # start date
        assert temp_list[1][5] == '2023-12-31'  # stop date
        assert temp_list[1][6] == 'd'  # periodicity
        assert temp_list[1][7] == None  # last check date
        assert temp_list[1][8] == None  # break date
        assert temp_list[1][9] == None  # last completion date
        assert temp_list[1][10] == 0  # current streak period
        assert temp_list[1][11] == 0  # longest streak period

        # check dates for Habit 1 (Start: 2023-09-20; Stop 2023-12-31; weekly
        # check 2023-09-21 - 2023-09-22
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 20))
        habit.Habit.check_habit(temp_habit, 'U_01', 'H_01', date(2023, 9, 21))
        # verify habit data
        temp_list = temp_habit_tracker.view_daily_habits('U_01')
        assert temp_list[0][0] == 'H_01'  # habit_id
        assert temp_list[0][1] == 'U_01'  # user_id
        assert temp_list[0][2] == 'H_01_descr'  # description
        assert temp_list[0][3] == 'Cat_01'  # category
        assert temp_list[0][4] == '2023-09-20'  # start date
        assert temp_list[0][5] == '2023-12-31'  # stop date
        assert temp_list[0][6] == 'd'  # periodicity
        assert temp_list[0][7] == '2023-09-21'  # last check date
        assert temp_list[0][8] == '1900-01-01'  # break date
        assert temp_list[0][9] == '2023-09-21'  # last completion date
        assert temp_list[0][10] == 2  # current streak period
        assert temp_list[0][11] == 2  # longest streak period

    def teardown_method(self):
        # Clear database
        # pass
        habit_db.db_clear()
