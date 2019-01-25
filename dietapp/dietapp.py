#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

import user as usr
import json as js
import pandas as pd
from best_recipes import best_recipes

ratingFile = "../Data/Rating"

#-----------------------------------------------------------------------------------------------
def register_user(age = 30, height = 170, weight = 70, sex = "M", exercise_level = 0.5, goal = "maintain"):
    user = usr.create_user(age, height, weight, sex, exercise_level, goal)
    usr.write_user(user)
    return user.uid

def recommended_recipe(uid):
    user = usr.read_user(uid)
    calories_range = user.calories_range()
    print(calories_range)
    best_rec = best_recipes(uid, 50)
    for recipe in best_rec:
        recipe_calories = get_calories(datafr, recipe[1]) * 3   # Calories for the day, puede que haya error aqui
        print(recipe_calories)
        if(recipe_calories > calories_range[0]) and (recipe_calories < calories_range[1]):
            index = get_index(datafr, recipe[1])
            return (datafr.at[index, 'title'], datafr.at[index, 'directions'])

    return -1

def rate_recipe(uid, title, rating):
    ratings = pd.read_pickle(ratingFile)
    aux = pd.DataFrame([[uid, ''.join((map(str, title))), rating]], columns=["user", "title", "rating"])
    ratings = ratings.append(aux)
    ratings.to_pickle("../Data/Rating")

def get_index(datafr, title):
    for i in range(len(datafr)):
        if(datafr.at[i, 'title'] == title):
            index = i
            break
    return index

def get_calories(datafr, title):
    return datafr.at[get_index(datafr, title), 'calories']

#------------------------------------------------------------------------------------------------

filename = "../Data/full_format_recipes.json"

with open(filename, 'r') as f:
    dict = js.load(f)

datafr = pd.DataFrame(dict)
datafr = datafr.astype({'title': str})

#register_user()

#print(recommended_recipe(201))

#rate_recipe(201, 'Lentil, Apple, and Turkey Wrap', 3.)

#rating = pd.read_pickle(ratingFile)
#print(rating)
#print(rating.tail(1)['rating'])
