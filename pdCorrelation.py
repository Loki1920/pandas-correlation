# corr() method give relationship between columns
import pandas as pd
df = pd.read_csv("data.csv")
print(df.corr())