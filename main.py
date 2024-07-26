from pprint import pprint as pp
import pandas as pd
import json

if __name__ == "__main__":
    with open("data.json", mode="r", encoding="utf-8") as d:
        data = json.load(d)
    print(len(data))
    df = pd.DataFrame(data)
    df["eventuality"] = df["eventuality"].apply(lambda x: f"{x['specific']} ({x['type']})")
    print(df[df["eventuality"].str.contains("politician")])
    

    
