# -------------------------------------------------------------------------
#    example file for user, habits and checks
#    Author: Eder Alois
# -------------------------------------------------------------------------
# file contains:
# users: 3
# habits: 7
# check offs: for H_01, H_02, H_03, H04, H_05, H_06

from datetime import date

import_users = [
    {
        "user_id": "U_01",
        "name": "User_01",
        "description":  "des_01"
    },
    {
        "user_id": "U_02",
        "name": "User_02",
        "description": "des_02"
    }
]

import_habits = [
    {   # Habit 01 (H_01) for User 01
        "habit_id": "H_01",
        "user_id":  "U_01",
        "habit_description": "Habit_01 description",
        "habit_category": "Cat_01",
        "habit_start": date(2023, 9, 1),
        "habit_stop": date(2023, 10, 31),
        "habit_period": "d"
    },
    {  # Habit 02 (H_02) for User 01
        "habit_id": "H_02",
        "user_id": "U_01",
        "habit_description": "Habit_02 description",
        "habit_category": "Cat_02",
        "habit_start": date(2023, 9, 5),
        "habit_stop": date(2023, 11, 30),
        "habit_period": "w"
    },
    {  # Habit 03 (H_03) for User 01
        "habit_id": "H_03",
        "user_id": "U_01",
        "habit_description": "Habit_03 description",
        "habit_category": "Cat_03",
        "habit_start": date(2023, 9, 15),
        "habit_stop": date(2023, 10, 31),
        "habit_period": "d"
    },
    {  # Habit 04 (H_04) for User 01
        "habit_id": "H_04",
        "user_id": "U_01",
        "habit_description": "Habit_04 description",
        "habit_category": "Cat_03",
        "habit_start": date(2023, 9, 15),
        "habit_stop": date(2023, 12, 31),
        "habit_period": "w"
    },
    {  # Habit 5 (H_05) for User 01
        "habit_id": "H_05",
        "user_id": "U_01",
        "habit_description": "Habit_05 description",
        "habit_category": "Cat_04",
        "habit_start": date(2023, 10, 1),
        "habit_stop": date(2023, 12, 31),
        "habit_period": "w"
    },
    {  # Habit 1 (H_06) for User 02
        "habit_id": "H_06",
        "user_id": "U_02",
        "habit_description": "Habit_11 description",
        "habit_category": "Cat_02",
        "habit_start": date(2023, 10, 1),
        "habit_stop": date(2023, 12, 15),
        "habit_period": "w"
    },
    {  # Habit 2 (H_07) for User 02
        "habit_id": "H_07",
        "user_id": "U_02",
        "habit_description": "Habit_12 description",
        "habit_category": "Cat_02",
        "habit_start": date(2023, 10, 1),
        "habit_stop": date(2023, 11, 30),
        "habit_period": "d"
    }
]

import_checks = [
    # checkins for User 01 and Habit 01 (start: 2023-09-01, stop: 2023-10-31, period: d), struggled
    {"check_id": 0, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 1)},
    {"check_id": 1, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 2)},
    {"check_id": 2, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 3)},
    {"check_id": 3, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 4)},
    {"check_id": 4, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 5)},
    {"check_id": 5, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 6)},
    {"check_id": 6, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 7)},
    {"check_id": 7, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 8)},
    {"check_id": 8, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 9)},
    {"check_id": 9, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 10)},
    {"check_id": 10, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 13)},
    {"check_id": 11, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 14)},
    {"check_id": 12, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 15)},
    {"check_id": 13, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 16)},
    {"check_id": 14, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 20)},
    {"check_id": 15, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 21)},
    {"check_id": 16, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 22)},
    {"check_id": 17, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 23)},
    {"check_id": 18, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 24)},
    {"check_id": 19, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 25)},
    {"check_id": 20, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 26)},
    {"check_id": 21, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 27)},
    {"check_id": 22, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 28)},
    {"check_id": 23, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 29)},
    {"check_id": 24, "user_id": "U_01", "habit_id": "H_01", "check_date": date(2023, 9, 30)},

    # checkins for User 01 and Habit 02 (start: 2023-09-05, stop: 2023-11-30, period: w), struggled
    {"check_id": 25, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 9, 5)},
    {"check_id": 26, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 9, 12)},
    {"check_id": 27, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 9, 18)},
    {"check_id": 28, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 9, 26)},
    {"check_id": 29, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 10, 1)},
    {"check_id": 30, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 10, 12)},
    {"check_id": 31, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 10, 16)},
    {"check_id": 32, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 10, 23)},
    {"check_id": 33, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 10, 31)},
    {"check_id": 34, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 11, 5)},
    {"check_id": 35, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 11, 11)},
    {"check_id": 36, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 11, 25)},
    {"check_id": 37, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 11, 30)},
    {"check_id": 38, "user_id": "U_01", "habit_id": "H_02", "check_date": date(2023, 12, 3)},

    # checkins for User 01 and Habit 3 (start: 2023-09-15, stop: 2023-10-31, period: d), not struggled
    {"check_id": 39, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 15)},
    {"check_id": 40, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 16)},
    {"check_id": 41, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 17)},
    {"check_id": 42, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 18)},
    {"check_id": 43, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 19)},
    {"check_id": 44, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 20)},
    {"check_id": 45, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 21)},
    {"check_id": 46, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 22)},
    {"check_id": 47, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 23)},
    {"check_id": 48, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 24)},
    {"check_id": 49, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 25)},
    {"check_id": 50, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 26)},
    {"check_id": 51, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 27)},
    {"check_id": 52, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 28)},
    {"check_id": 53, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 29)},
    {"check_id": 54, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 9, 30)},
    {"check_id": 55, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 1)},
    {"check_id": 56, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 2)},
    {"check_id": 57, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 3)},
    {"check_id": 58, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 4)},
    {"check_id": 59, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 5)},
    {"check_id": 60, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 6)},
    {"check_id": 61, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 7)},
    {"check_id": 62, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 8)},
    {"check_id": 63, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 9)},
    {"check_id": 64, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 10)},
    {"check_id": 65, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 11)},
    {"check_id": 66, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 12)},
    {"check_id": 67, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 13)},
    {"check_id": 68, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 14)},
    {"check_id": 69, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 15)},
    {"check_id": 70, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 16)},
    {"check_id": 71, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 17)},
    {"check_id": 72, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 18)},
    {"check_id": 73, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 19)},
    {"check_id": 74, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 20)},
    {"check_id": 75, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 21)},
    {"check_id": 76, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 22)},
    {"check_id": 77, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 23)},
    {"check_id": 78, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 24)},
    {"check_id": 79, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 25)},
    {"check_id": 80, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 26)},
    {"check_id": 81, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 27)},
    {"check_id": 82, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 28)},
    {"check_id": 83, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 29)},
    {"check_id": 84, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 30)},
    {"check_id": 85, "user_id": "U_01", "habit_id": "H_03", "check_date": date(2023, 10, 31)},

    # checkins for User 01 and Habit 04 (start: 2023-09-15, stop: 2023-12-31, period: w), not struggled
    {"check_id": 86, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 9, 15)},
    {"check_id": 87, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 9, 22)},
    {"check_id": 88, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 9, 29)},
    {"check_id": 89, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 10, 6)},
    {"check_id": 90, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 10, 13)},
    {"check_id": 91, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 10, 20)},
    {"check_id": 92, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 10, 27)},
    {"check_id": 93, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 11, 2)},
    {"check_id": 94, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 11, 9)},
    {"check_id": 95, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 11, 15)},
    {"check_id": 96, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 11, 21)},
    {"check_id": 97, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 11, 26)},
    {"check_id": 98, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 12, 3)},
    {"check_id": 99, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 12, 10)},
    {"check_id": 100, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 12, 16)},
    {"check_id": 101, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 12, 23)},
    {"check_id": 102, "user_id": "U_01", "habit_id": "H_04", "check_date": date(2023, 12, 30)},

    # checkins for User 01 and Habit 05 (start: 2023-10-01, stop: 2023-12-31, period: w), struggled
    {"check_id": 103, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 10, 1)},
    {"check_id": 104, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 10, 6)},
    {"check_id": 105, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 10, 13)},
    {"check_id": 106, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 10, 19)},
    {"check_id": 107, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 10, 25)},
    {"check_id": 108, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 11, 2)},
    {"check_id": 109, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 11, 9)},
    {"check_id": 110, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 11, 15)},
    {"check_id": 111, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 11, 25)},
    {"check_id": 112, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 10, 30)},
    {"check_id": 113, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 12, 6)},
    {"check_id": 114, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 12, 13)},
    {"check_id": 115, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 12, 19)},
    {"check_id": 116, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 12, 25)},
    {"check_id": 117, "user_id": "U_01", "habit_id": "H_05", "check_date": date(2023, 12, 31)},

    # checkins for User 02 and Habit 06 (start: 2023-10-01, stop: 2023-12-15, period: w), struggled
    {"check_id": 118, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 10, 1)},
    {"check_id": 119, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 10, 7)},
    {"check_id": 120, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 10, 15)},
    {"check_id": 121, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 10, 25)},
    {"check_id": 122, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 10, 30)},
    {"check_id": 123, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 11, 8)},
    {"check_id": 124, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 11, 15)},
    {"check_id": 125, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 11, 21)},
    {"check_id": 126, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 11, 29)},
    {"check_id": 127, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 12, 6)},
    {"check_id": 128, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 12, 13)},
    {"check_id": 129, "user_id": "U_02", "habit_id": "H_06", "check_date": date(2023, 12, 21)}
]
