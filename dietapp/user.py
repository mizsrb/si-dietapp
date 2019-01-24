#! /usr/bin/env python
# -- coding: utf-8 --

# ULL - Sistemas Inteligentes 2018/2019
#
# User class and functions to create, write and read users


USERS_DATA = "data/users.txt"
LAST_USER_ID = "data/last_user_id"


class User:
    def __init__(self, uid, age = 30, height = 170, weight = 70, sex = "M", exercise_level = 0.5, goal = "maintain"):
        self.uid = uid
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex
        self.exerciseFactor = self.exercise_factor(exercise_level)
        self.goal = goal

    def exercise_factor(self, exercise_level):
        if exercise_level < 0:
            exercise_level = 0
        elif exercise_level > 1:
            exercise_level = 1

        return 1.2 + 0.7 * exercise_level

    def standard_calories(self):
        if sex = "M":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        calories = bmr * exerciseFactor
        if calories / weight < 18:
            calories = weight * 18

        return calories

    def maintain_weight_calories(self):
        std = self.standard_calories()
        return (std * 0.9, std * 1.1)

    def lower_weight_calories(self):
        lower = self.standard_calories() * 0.8
        return (lower * 0.9, lower * 1.1)

    def calories_range(self):
        if goal == "lower":
            return lower_weight_calories()
        else:
            return maintain_weight_calories()


def read_user(uid):
    f = open(USERS_DATA, 'r')
    line = ['-1']
    while int(line[0]) != uid:
        line = f.readline().split()
    f.close()

    return User(int(line[0]), int(line[1]), int(line[2]), int(line[3]), line[4], (float(line[5]) - 1.2) / 0.7)


def create_user(age = 30, height = 170, weight = 70, sex = "M", exercise_level = 0.5, goal = "maintain"):
    f = open(LAST_USER_ID, 'r')
    uid = int(f.readline()) + 1
    f.close()

    f = open(LAST_USER_ID, 'w')
    f.write(uid)
    f.close()

    return User(uid, age, height, weight, sex, exercise_level, goal)


def write_user(user):
    f = open(USERS_DATA, 'r+')
    f.seek(0, 2) # End of the file
    f.write(str(user.uid) + " " + str(user.age) + " " + str(user.height) + " " + str(user.weight) + " " + user.sex
            + " " + str(user.exerciseFactor) + " " + user.goal + "\n")
    f.close()





########
