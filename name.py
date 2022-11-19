# open /home/paritosh/My Projects/CRS/movies.txt
import pandas as pd

df = pd.read_csv("/home/paritosh/My Projects/CRS/movies.txt", sep="::", engine='python', header=None)
name = df[1]
# get only first 2 words from name
name = name.str.split(" ", n=2, expand=True)
print(name[0])
print(name[1].str)
name_list = []
for i in range(len(name)):
    name_list.append(name[0][i] + " " + name[1][i])

# save name_list to csv
df = pd.DataFrame(name_list)
df.to_csv("name_list.txt", index=False, header=False)
