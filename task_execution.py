#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


csv_file = 'data.csv'
df = pd.read_csv(csv_file)
print df[['layout', 'verify', 'no_verify']].groupby('layout').mean()