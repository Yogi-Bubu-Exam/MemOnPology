from pprint import pprint as pp
import pandas as pd
import json

path = "cmm.json"
with open(path, mode="r", encoding="utf-8") as d:
    data = json.load(d)
print(len(data))
df = pd.DataFrame(data)
df["eventuality"] = df["eventuality"].apply(lambda x: f"{x['specific']} ({x['type']})")
query = df[["template", "connotation", "attitude", "opinion"]]
print(query.describe())


    
