import sys
sys.path.append("../../oofpp_habit_tracking_project/src")  # folder that contains database

from datetime import date
from database import habit_db as habit_db
from classes import user as user
from classes import habit as habit
import pytest

class TestHabit:
    def setup_method(self):
        # setting up db
        habit_db.db_clear()
        habit_db.db_init()
        # setting up a user 1
        user01 = user.User("U_01", "Test_User_01", "desc_01")
        user01.add_user()
        # setting up a user 2
        user01 = user.User("U_02", "Test_User_02", "desc_02")
        user01.add_user()
        # set user 1 active
        user01.set_active_user('U_01')
        active_user_id = user.User.active_user_id
        assert active_user_id == 'U_01'

    # Testfunction with 1 habit, insert single habit, check single habit
    def test_single_habit(self):
        habit01 = habit.Habit('H_01', 'U_01', 'H_01_descr','Cat_01',
                              date(2023, 9, 15), date(2023, 9, 30),
                              'd')
        habit01.add_habit()
        # read new habit 1 of User 1
        temp_habit = habit.Habit.get_single_habit(habit01, 'U_01', 'H_01')

        assert temp_habit[0][0] == 'H_01'
        assert temp_habit[0][1] == 'U_01'
        assert temp_habit[0][2] == 'H_01_descr'
        assert temp_habit[0][3] == 'Cat_01'
        assert temp_habit[0][4] == '2023-09-15'
        assert temp_habit[0][5] == '2023-09-30'
        assert temp_habit[0][6] == 'd'

    # Testfunction with 3 habit, insert single habit, check all habits
    def test_3_habit(self):
        habit01 = habit.Habit('H_01', 'U_01', 'H_01_descr', 'Cat_01',
                              date(2023, 9, 15), date(2023, 9, 30),
                              'd')
        habit01.add_habit()
        # read new habit 1 of User 1
        temp_habit = habit.Habit.get_single_habit(habit01, 'U_01', 'H_01')

        assert temp_habit[0][0] == 'H_01'
        assert temp_habit[0][1] == 'U_01'
        assert temp_habit[0][2] == 'H_01_descr'
        assert temp_habit[0][3] == 'Cat_01'
        assert temp_habit[0][4] == '2023-09-15'
        assert temp_habit[0][5] == '2023-09-30'
        assert temp_habit[0][6] == 'd'

        # Add habit 2
        habit02 = habit.Habit('H_02', 'U_01', 'H_02_descr', 'Cat_02',
                              date(2023, 9, 20), date(2023, 10, 31),
                              'd')
        habit02.add_habit()

        # Add habit 3
        habit03 = habit.Habit('H_03', 'U_01', 'H_03_descr', 'Cat_03',
                              date(2023, 10, 1), date(2023, 12, 31),
                              'w')
        habit03.add_habit()

        # read all habits of User 1 (3 Habits)
        temp_habit = habit.Habit.get_all_habits_of_user(habit03, 'U_01')
        # Check Habit 1
        assert temp_habit[0][0] == 'H_01'
        assert temp_habit[0][1] == 'U_01'
        assert temp_habit[0][2] == 'H_01_descr'
        assert temp_habit[0][3] == 'Cat_01'
        assert temp_habit[0][4] == '2023-09-15'
        assert temp_habit[0][5] == '2023-09-30'
        assert temp_habit[0][6] == 'd'
        # Check Habit 2
        assert temp_habit[1][0] == 'H_02'
        assert temp_habit[1][1] == 'U_01'
        assert temp_habit[1][2] == 'H_02_descr'
        assert temp_habit[1][3] == 'Cat_02'
        assert temp_habit[1][4] == '2023-09-20'
        assert temp_habit[1][5] == '2023-10-31'
        assert temp_habit[1][6] == 'd'
        # Check Habit 3
        assert temp_habit[2][0] == 'H_03'
        assert temp_habit[2][1] == 'U_01'
        assert temp_habit[2][2] == 'H_03_descr'
        assert temp_habit[2][3] == 'Cat_03'
        assert temp_habit[2][4] == '2023-10-01'
        assert temp_habit[2][5] == '2023-12-31'
        assert temp_habit[2][6] == 'w'

    # Testfunction with 3 habit from test 3, insert 1 habit, modify and delete the habit, check all habits
    def test_4_habit_modify_delete(self):
        # Add Habit 1
        habit01 = habit.Habit('H_01', 'U_01', 'H_01_descr', 'Cat_01',
                              date(2023, 9, 15), date(2023, 9, 30),
                              'd')
        habit01.add_habit()

        # Add habit 2
        habit02 = habit.Habit('H_02', 'U_01', 'H_02_descr', 'Cat_02',
                              date(2023, 9, 20), date(2023, 10, 31),
                              'd')
        habit02.add_habit()

        # Add habit 3
        habit03 = habit.Habit('H_03', 'U_01', 'H_03_descr', 'Cat_03',
                              date(2023, 10, 1), date(2023, 12, 31),
                              'w')
        habit03.add_habit()

        # Add Habit 4
        habit04 = habit.Habit('H_04', 'U_01', 'H_04_descr', 'Cat_04',
                              date(2023, 9, 15), date(2023,  12, 31),
                              'w')
        habit04.add_habit()

        # read new habit 4 of User 1
        tmp_habit = habit.Habit.get_single_habit(habit04, 'U_01', 'H_04')
        # Check Habit 4
        assert tmp_habit[0][0] == 'H_04'
        assert tmp_habit[0][1] == 'U_01'
        assert tmp_habit[0][2] == 'H_04_descr'
        assert tmp_habit[0][3] == 'Cat_04'
        assert tmp_habit[0][4] == '2023-09-15'
        assert tmp_habit[0][5] == '2023-12-31'
        assert tmp_habit[0][6] == 'w'

        # read all habits of User 1 (4 Habits)
        temp_habit = habit.Habit.get_all_habits_of_user(habit04, 'U_01')
        # Check Habit 1
        assert temp_habit[0][0] == 'H_01'
        assert temp_habit[0][1] == 'U_01'
        assert temp_habit[0][2] == 'H_01_descr'
        assert temp_habit[0][3] == 'Cat_01'
        assert temp_habit[0][4] == '2023-09-15'
        assert temp_habit[0][5] == '2023-09-30'
        assert temp_habit[0][6] == 'd'
        # Check Habit 2
        assert temp_habit[1][0] == 'H_02'
        assert temp_habit[1][1] == 'U_01'
        assert temp_habit[1][2] == 'H_02_descr'
        assert temp_habit[1][3] == 'Cat_02'
        assert temp_habit[1][4] == '2023-09-20'
        assert temp_habit[1][5] == '2023-10-31'
        assert temp_habit[1][6] == 'd'
        # Check Habit 3
        assert temp_habit[2][0] == 'H_03'
        assert temp_habit[2][1] == 'U_01'
        assert temp_habit[2][2] == 'H_03_descr'
        assert temp_habit[2][3] == 'Cat_03'
        assert temp_habit[2][4] == '2023-10-01'
        assert temp_habit[2][5] == '2023-12-31'
        assert temp_habit[2][6] == 'w'
        # Check Habit 4
        assert temp_habit[3][0] == 'H_04'
        assert temp_habit[3][1] == 'U_01'
        assert temp_habit[3][2] == 'H_04_descr'
        assert temp_habit[3][3] == 'Cat_04'
        assert temp_habit[3][4] == '2023-09-15'
        assert temp_habit[3][5] == '2023-12-31'
        assert temp_habit[3][6] == 'w'

        # modify habit 4
        habit04.modify_habit('U_01', 'H_04', 'H_04_description', 'Cat_03',
                             date(2023, 9, 30), date(2024, 3,31),
                             'w')
        # read modified habit 4 of User 1
        temp_habit = habit.Habit.get_single_habit(habit04, 'U_01', 'H_04')
        # Check modified Habit 4
        assert temp_habit[0][0] == 'H_04'
        assert temp_habit[0][1] == 'U_01'
        assert temp_habit[0][2] == 'H_04_description'
        assert temp_habit[0][3] == 'Cat_03'
        assert temp_habit[0][4] == '2023-09-30'
        assert temp_habit[0][5] == '2024-03-31'
        assert temp_habit[0][6] == 'w'

        # delete habit 3
        habit04.delete_habit('U_01', 'H_03')
        # read all habits of User 1
        temp_habit = habit.Habit.get_all_habits_of_user(habit04, 'U_01')
        # Check all Habits
        # Check Habit 1
        assert temp_habit[0][0] == 'H_01'
        assert temp_habit[0][1] == 'U_01'
        assert temp_habit[0][2] == 'H_01_descr'
        assert temp_habit[0][3] == 'Cat_01'
        assert temp_habit[0][4] == '2023-09-15'
        assert temp_habit[0][5] == '2023-09-30'
        assert temp_habit[0][6] == 'd'
        # Check Habit 2
        assert temp_habit[1][0] == 'H_02'
        assert temp_habit[1][1] == 'U_01'
        assert temp_habit[1][2] == 'H_02_descr'
        assert temp_habit[1][3] == 'Cat_02'
        assert temp_habit[1][4] == '2023-09-20'
        assert temp_habit[1][5] == '2023-10-31'
        assert temp_habit[1][6] == 'd'
        # No check of Habit 3 (deleted)
        # Check Habit 4
        assert temp_habit[2][0] == 'H_04'
        assert temp_habit[2][1] == 'U_01'
        assert temp_habit[2][2] == 'H_04_description'
        assert temp_habit[2][3] == 'Cat_03'
        assert temp_habit[2][4] == '2023-09-30'
        assert temp_habit[2][5] == '2024-03-31'
        assert temp_habit[2][6] == 'w'

    # Testfunction with 3 habit for 2 users, insert 3 habit, read all habits for all users, check all habits
    def test_5_habit_for_2_users(self):
        # Add Habit 1
        habit01 = habit.Habit('H_01', 'U_01', 'H_01_descr', 'Cat_01',
                              date(2023, 9, 15), date(2023, 9, 30),
                              'd')
        habit01.add_habit()

        # Add habit 2
        habit02 = habit.Habit('H_02', 'U_01', 'H_02_descr', 'Cat_02',
                              date(2023, 9, 20), date(2023, 10, 31),
                              'd')
        habit02.add_habit()

        # Add habit 3
        habit03 = habit.Habit('H_03', 'U_02', 'H_03_descr', 'Cat_03',
                              date(2023, 10, 1), date(2024, 12, 31),
                              'w')
        habit03.add_habit()

        temp_habit = habit.Habit.get_all_habits(habit03)
        # Check all Habits
        # Check Habit 1
        assert temp_habit[0][0] == 'H_01'
        assert temp_habit[0][1] == 'U_01'
        assert temp_habit[0][2] == 'H_01_descr'
        assert temp_habit[0][3] == 'Cat_01'
        assert temp_habit[0][4] == '2023-09-15'
        assert temp_habit[0][5] == '2023-09-30'
        assert temp_habit[0][6] == 'd'
        # Check Habit 2
        assert temp_habit[1][0] == 'H_02'
        assert temp_habit[1][1] == 'U_01'
        assert temp_habit[1][2] == 'H_02_descr'
        assert temp_habit[1][3] == 'Cat_02'
        assert temp_habit[1][4] == '2023-09-20'
        assert temp_habit[1][5] == '2023-10-31'
        assert temp_habit[1][6] == 'd'
        # No check of Habit 3 (deleted)
        # Check Habit 4
        assert temp_habit[2][0] == 'H_03'
        assert temp_habit[2][1] == 'U_02'
        assert temp_habit[2][2] == 'H_03_descr'
        assert temp_habit[2][3] == 'Cat_03'
        assert temp_habit[2][4] == '2023-10-01'
        assert temp_habit[2][5] == '2024-12-31'
        assert temp_habit[2][6] == 'w'

    def teardown_method(self):
        # Clear database
        habit_db.db_clear()

