from pprint import pprint as pp
import pandas as pd
import json

if __name__ == "__main__":
    with open("data.json", mode="r", encoding="utf-8") as d:
        data = json.load(d)
    df = pd.DataFrame(data)


    
