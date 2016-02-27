#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


csv_file = '2016-02-26.csv'
df = pd.read_csv(csv_file)

time_cols = [col for col in df.columns if col.startswith('time')]
df_time = df[time_cols]
df_time_ratio = df_time.div(df_time.sum(axis=1), axis='index')
df_time_ratio.columns = [col.split('time_')[-1] for col in time_cols]
sns.boxplot(x=df_time_ratio, orient='h')
plt.xlabel('Time (ratio to pick and place/return execution)')
plt.show()