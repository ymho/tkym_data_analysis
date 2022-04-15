# import matplotlib.pyplot as plt
import pandas as pd

df_heijitsu = pd.read_csv('./timescale-heijitsu.csv',index_col=['dateObserved'], parse_dates=True)
df_heijitsu = df_heijitsu.set_index([df_heijitsu.index.hour, df_heijitsu.index.weekday, df_heijitsu.index])
df_heijitsu.index.names = ['hour', 'weekday', 'day']

df_kyujitsu = pd.read_csv('./timescale-kyujitsu.csv',index_col=['dateObserved'], parse_dates=True)
df_kyujitsu = df_kyujitsu.set_index([df_kyujitsu.index.hour, df_kyujitsu.index.weekday, df_kyujitsu.index])
df_kyujitsu.index.names = ['hour', 'weekday', 'day']

# 週間（平日）
df_heijitsu_weekday = df_heijitsu.groupby(level='weekday').mean()
df_heijitsu_weekday = df_heijitsu_weekday.sort_index(axis=0)
df_heijitsu_weekday.to_csv("df_heijitsu_weekday.csv",header=True, index=True)

# 週間（休日）
df_kyujitsu_weekday = df_kyujitsu.groupby(level='weekday').mean()
df_kyujitsu_weekday = df_kyujitsu_weekday.sort_index(axis=0)
df_heijitsu_weekday.to_csv("df_kyujitsu_weekday.csv",header=True, index=True)

# 時間（平日）
df_heijitsu_hour = df_heijitsu.groupby(level='hour').mean()
df_heijitsu_hour = df_heijitsu_hour.sort_index(axis=0)
df_heijitsu_hour.to_csv("df_heijitsu_hour.csv",header=True, index=True)

# 時間（休日）
df_kyujitsu_hour = df_kyujitsu.groupby(level='hour').mean()
df_kyujitsu_hour = df_kyujitsu_hour.sort_index(axis=0)
df_kyujitsu_hour.to_csv("df_kyujitsu_hour.csv",header=True, index=True)
