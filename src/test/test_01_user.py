import sys
sys.path.append("../../oofpp_habit_tracking_project/src")  # folder that contains database

from database import habit_db as habit_db
from classes import user as User
import pytest

class TestUser:
    def setup_method(self):
        # setting up db
        habit_db.db_clear()
        habit_db.db_init()

    # Testfunction with 1 user, insert single user, check single user
    def test_single_user(self):
        user01 = User.User("U_01", "Test_User_01", "desc_01")
        user01.add_user()
        assert user01.user_id == "U_01"

        assert user01.get_user("U_01")[0][0] == 'U_01'
        assert user01.get_user("U_01")[0][1] == 'Test_User_01'
        assert user01.get_user("U_01")[0][2] == 'desc_01'

    # Testfunction with 2 users, insert single users, check single user
    def test_2_user(self):
        user01 = User.User("U_01", "Test_User_01", "desc_01")
        user01.add_user()
        assert user01.user_id == "U_01"

        assert user01.get_user("U_01")[0][0] == 'U_01'
        assert user01.get_user("U_01")[0][1] == 'Test_User_01'
        assert user01.get_user("U_01")[0][2] == 'desc_01'

        user02 = User.User("U_02", "Test_User_02", "desc_02")
        user02.add_user()
        assert user02.user_id == "U_02"

        assert user02.get_user("U_02")[0][0] == 'U_02'
        assert user02.get_user("U_02")[0][1] == 'Test_User_02'
        assert user02.get_user("U_02")[0][2] == 'desc_02'

    # Testfunction with 3 users, insert single users, check single user, check all users
    def test_3_user(self):
        """
        Testfunction with 3 users, insert  single users, check single user, check all users
        :return:
        """
        user01 = User.User("U_01", "Test_User_01", "desc_01")
        user01.add_user()
        assert user01.user_id == "U_01"

        assert user01.get_user("U_01")[0][0] == 'U_01'
        assert user01.get_user("U_01")[0][1] == 'Test_User_01'
        assert user01.get_user("U_01")[0][2] == 'desc_01'

        user02 = User.User("U_02", "Test_User_02", "desc_02")
        user02.add_user()
        assert user02.user_id == "U_02"

        user03 = User.User("U_03", "Test_User_03", "desc_03")
        user03.add_user()
        assert user03.user_id == "U_03"

        user_all = User.User()
        user_all = User.User.get_all_users(user_all)
        assert user_all[0][0] == 'U_01'
        assert user_all[0][1] == 'Test_User_01'
        assert user_all[0][2] == 'desc_01'
        assert user_all[1][0] == 'U_02'
        assert user_all[1][1] == 'Test_User_02'
        assert user_all[1][2] == 'desc_02'
        assert user_all[2][0] == 'U_03'
        assert user_all[2][1] == 'Test_User_03'
        assert user_all[2][2] == 'desc_03'

    # Testfunction with 3 users, add 3 users, modify 1 user, check users and delete 1 user and check users
    def test_3_user_modify_delete(self):
        """
        Testfunction with 3 users, add 3 users, modify 1 user, check users and delete 1 user and check users
        :return:
        """
        user01 = User.User("U_01", "Test_User_01", "desc_01")
        user01.add_user()
        user02 = User.User("U_02", "Test_User_02", "desc_02")
        user02.add_user()
        user03 = User.User("U_03", "Test_User_03", "desc_03")
        user03.add_user()

        # check all 3 users
        user_all = User.User()
        user_all = User.User.get_all_users(user_all)
        assert user_all[0][0] == 'U_01'
        assert user_all[0][1] == 'Test_User_01'
        assert user_all[0][2] == 'desc_01'
        assert user_all[1][0] == 'U_02'
        assert user_all[1][1] == 'Test_User_02'
        assert user_all[1][2] == 'desc_02'
        assert user_all[2][0] == 'U_03'
        assert user_all[2][1] == 'Test_User_03'
        assert user_all[2][2] == 'desc_03'

        # modify user2
        user02.modify_user('U_02', 'Test_User_x2', 'desc_x2')

        # check all 3 users
        user_all = User.User()
        user_all = User.User.get_all_users(user_all)
        assert user_all[0][0] == 'U_01'
        assert user_all[0][1] == 'Test_User_01'
        assert user_all[0][2] == 'desc_01'
        assert user_all[1][0] == 'U_02'
        assert user_all[1][1] == 'Test_User_x2'
        assert user_all[1][2] == 'desc_x2'
        assert user_all[2][0] == 'U_03'
        assert user_all[2][1] == 'Test_User_03'
        assert user_all[2][2] == 'desc_03'

        # delete user 2
        user02.delete_user('U_02')

        # check remain users
        assert user_all[0][0] == 'U_01'
        assert user_all[0][1] == 'Test_User_01'
        assert user_all[0][2] == 'desc_01'
        assert user_all[2][0] == 'U_03'
        assert user_all[2][1] == 'Test_User_03'
        assert user_all[2][2] == 'desc_03'

    # Testfunction with 3 users, set user 2 active check active user, set user 3 active and check active user
    def test_4_active_user(self):
        """
        Testfunction with 3 users, add 3 users, modify 1 user, check users and delete 1 user and check users
        :return:
        """
        user01 = User.User("U_01", "Test_User_01", "desc_01")
        user01.add_user()
        user02 = User.User("U_02", "Test_User_02", "desc_02")
        user02.add_user()
        user03 = User.User("U_03", "Test_User_03", "desc_03")
        user03.add_user()

        # check all 3 users
        user_all = User.User()
        user_all = User.User.get_all_users(user_all)
        assert user_all[0][0] == 'U_01'
        assert user_all[0][1] == 'Test_User_01'
        assert user_all[0][2] == 'desc_01'
        assert user_all[1][0] == 'U_02'
        assert user_all[1][1] == 'Test_User_02'
        assert user_all[1][2] == 'desc_02'
        assert user_all[2][0] == 'U_03'
        assert user_all[2][1] == 'Test_User_03'
        assert user_all[2][2] == 'desc_03'

        # get active user, no active user is set
        temp_user = User.User()
        active_user = User.User.active_user_id
        assert active_user == ''

        # set user 2 active, check active user, active user is user 2
        temp_user = User.User()
        temp_user.set_active_user('U_02')
        active_user = User.User.active_user_id
        assert active_user == 'U_02'

        temp_user = User.User()
        temp_user = User.User.get_active_user(temp_user)
        assert temp_user[0][0] == 'U_02'
        assert temp_user[0][1] == 'Test_User_02'
        assert temp_user[0][2] == 'desc_02'

    def teardown_method(self):
        # Clear database
        habit_db.db_clear()
