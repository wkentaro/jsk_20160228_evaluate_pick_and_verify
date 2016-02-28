#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import pandas as pd


csv_file = 'data.csv'
df = pd.read_csv(csv_file)

print df.groupby('layout')[['verify', 'no_verify']].mean()

n_data = len(df)
success_graspone = df.query('not (verify == 0 and no_verify == 0)')
success_detect = df.query('no_verify == 1')
success_verify = df.query('verify == 0 and no_verify == -1')

print('''
success_graspone: {1}/{0}
success_detect: {2}/{0}
success_verify: {3}/{0}'''.format(
    n_data,
    len(success_graspone),
    len(success_detect),
    len(success_verify),
))