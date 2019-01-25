from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import surprise as sp
import json as js
import pandas as pd
import numpy as np

def best_recipes(uid, n):
    test_user_id = uid
    n_best_values = n
    filename = "full_format_recipes.json"

    with open(filename, 'r') as f:
        dict = js.load(f)

    recipeInfo = pd.DataFrame(dict)
    recipeInfo = recipeInfo.astype({"title": str})

    rating = pd.read_pickle("Rating")

    reader = sp.Reader(line_format = "user item rating", sep = "\t")
    data = sp.Dataset.load_from_df(rating, reader = reader)

    trainset = data.build_full_trainset()

    algorithm = sp.KNNWithMeans(k = 50, sim_options={'name': 'pearson_baseline', 'user_based': False})
    algorithm.fit(trainset)

    titles = recipeInfo[["title"]]

    user_x_titles = rating.loc[rating['user'] == test_user_id, 'title']

    titles_to_pred = np.setdiff1d(titles, user_x_titles)

    testset = [[test_user_id, title, 0.] for title in titles_to_pred]

    predictions = algorithm.test(testset)

    pred_ratings = []
    for pred in predictions:
        pred_ratings.append([pred.est, pred.iid])

    for i in range(n_best_values + 1):
        max = 0
        for j in range(i, len(predictions)):
            if(pred_ratings[j][0] > pred_ratings[max][0]):
                max = j
        pred_ratings[i], pred_ratings[max] = pred_ratings[max], pred_ratings[i]

    return pred_ratings[:n_best_values + 1]
