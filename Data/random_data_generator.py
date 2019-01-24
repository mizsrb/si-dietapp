import json as js
import pandas as pd
import random

filename = "full_format_recipes.json"

with open(filename, 'r') as f:
    dict = js.load(f)

datafr = pd.DataFrame(dict)

data = datafr[["title", "rating"]]
data["user"] = 0
data = data[["user", "title", "rating"]]

titles = datafr[["title"]]

uid = 1
to_add = pd.DataFrame(columns=["user", "title", "rating"])

for i in range(200):
    to_add.drop(to_add.index, inplace = True)
    for j in random.sample(titles.values.tolist(), 200):
        aux = pd.DataFrame([[uid, ''.join(map(str, j)), random.uniform(0.0, 5.0)]], columns=["user", "title", "rating"])
        to_add = to_add.append(aux)
    data =  data.append(to_add)
    uid += 1

print(data)
data.to_pickle("Rating")


