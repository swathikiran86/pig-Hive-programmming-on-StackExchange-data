import pandas as pd
data = pd.read_csv('/home/vagrant/4639.txt', sep="\t", names = ["words", "TF-IDF"])
data["words"] = data["words"].str.split(" ",n=1,expand=True)
#.str.split("t", n = 1, expand = True)
final = data.sort_values(by = ["TF-IDF"], ascending=False).head(10)
print(final)
