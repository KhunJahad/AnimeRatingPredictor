import pandas as pd 
df = pd.DataFrame(columns=['ids', 'names', 'mean', 'description'])
for i in range(1,8):
	filename="dataset{}.csv".format(i)
	df_temp = pd.read_csv(filename)
	df = df.append(df_temp,ignore_index=True)

df.to_csv("anime_rating_dataset.csv",index=False)
print(df)