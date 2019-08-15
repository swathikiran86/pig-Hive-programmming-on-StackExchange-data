import pandas as pd
g = pd.read_csv('hivetable.csv', sep=',', names = ["UserId", "Body", "Title"])
import re
g["Body"] = g.Body.apply(lambda x: re.sub(r"[^a-zA-Z0-9]+",' ', x))
g["Title"] = g.Title.apply(lambda x: re.sub(r"[^a-zA-Z0-9]+",' ', x))
g=g.groupby('UserId')
g.apply(lambda x: x.to_csv(r'{}.txt'.format(x.name),header=False, index = False))
