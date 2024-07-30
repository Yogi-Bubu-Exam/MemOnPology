from pprint import pprint as pp
import pandas as pd
import json

path = "data.json"
with open(path, mode="r", encoding="utf-8") as d:
    data = json.load(d)
print(len(data))
pp(data)
df = pd.DataFrame(data)
# print(df["template"].unique())
df["eventuality"] = df["eventuality"].apply(lambda x: f"{x['specific']} ({x['type']})")
query = df[["template", "connotation", "attitude", "opinion"]][df["eventuality"].str.contains("Brexit")]
print(query)


    
