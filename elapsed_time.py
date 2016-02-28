#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


csv_file = 'data.csv'
df = pd.read_csv(csv_file)

time_cols = [col for col in df.columns if col.startswith('time')]
df_time = df[time_cols]
df_time_ratio = df_time.div(df_time.sum(axis=1), axis='index')
df_time_ratio.columns = [col.split('time_')[-1] for col in time_cols]
time_rows = []
for i, row in df_time_ratio.iterrows():
    for action in ['detect', 'pick', 'verify', 'place', 'return']:
        time_rows.append((action, row[action]))

df = pd.DataFrame(time_rows)
df.columns = ['action', 'time']
sns.stripplot(y='action', x='time', data=df, jitter=True, linewidth=1)
plt.ylabel('Part of Task')
plt.xlabel('Time (Ratio to Whole Task Execution)')
plt.show()