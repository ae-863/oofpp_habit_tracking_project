# -------------------------------------------------------------------------
#    Class User
#    Author: Eder Alois
# -------------------------------------------------------------------------
import database.habit_db as db
from classes.example import import_users


class User:
    # current selected active user
    active_user_id = ""

    def __init__(self, uid="", name="", description=""):
        """
        Constructor for a new user, the user will be written in the db and set as active user
        :param uid: id of the user as integer type
        :param name: name of the user as string type
        :param description: description oof teh user as string type
        """
        self.user_id = uid
        self.user_name = name
        self.user_description = description

    def get_all_users(self) -> list:
        """
        get all users from the db
        :return: list of users
        """
        return db.db_get_all_users()

    def get_user(self, user_id) -> list:
        """
        get a single user from the db
        :param user_id:
        :return: list of user
        """
        return db.db_get_single_user(user_id)

    def add_user(self) -> None:
        """
        add a user to the table users of db
        :return: None
        """
        db.db_add_user(user_id=self.user_id, name=self.user_name, description=self.user_description)

    def modify_user(self, uid: str, name: str, description: str) -> None:
        """
        modifies the data of a user in the db
        :param uid:
        :param name:
        :param description:
        :return: None
        """
        db.db_update_user(user_id=uid, name=name, description=description)

    def delete_user(self, uid: str) -> None:
        """
        deletes a user from the table users of the db
        :param uid:
        :return: None
        """
        db.db_del_user(user_id=uid)

    def get_active_user(self) -> list:
        """
        get the selected active user, if not no one is selected then an empty user
        :return: list of user
        """
        if User.active_user_id != "":
            return db.db_get_single_user(User.active_user_id)
        else:
            return ['', '', '']

    def set_active_user(self, user_id) -> None:
        """
        set the active user
        :param user_id:
        :return: None
        """
        User.active_user_id = user_id

    def import_user_list(self) -> None:
        """
        import users from a list in the file example.py
        this is used for test purpose only
        :return: None
        """
        for user in import_users:
            db.db_add_user(user['user_id'], user['name'], user['description'])
