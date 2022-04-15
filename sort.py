import pandas as pd
df = pd.read_csv('./result.csv',header=None, names=['dateObserved', 'pepleCount'])
df["dateObserved"] = pd.to_datetime(df["dateObserved"],infer_datetime_format=True)
df.sort_values(by="dateObserved", ascending = True, inplace = True) 
df.drop_duplicates(inplace = True)
df.to_csv("timescale.csv",header=True, index=False)

df = pd.read_csv('./generated/heijitsu.csv',header=None, names=['dateObserved', 'pepoleCount'])
df["dateObserved"] = pd.to_datetime(df["dateObserved"],infer_datetime_format=True)
df.sort_values(by="dateObserved", ascending = True, inplace = True)
df.drop_duplicates(inplace = True) 
df.to_csv("timescale-heijitsu.csv",header=True, index=False)

df = pd.read_csv('./generated/kyujitsu.csv',header=None, names=['dateObserved', 'pepoleCount'])
df["dateObserved"] = pd.to_datetime(df["dateObserved"],infer_datetime_format=True)
df.sort_values(by="dateObserved", ascending = True, inplace = True) 
df.drop_duplicates(inplace = True)
df.to_csv("timescale-kyujitsu.csv",header=True, index=False)