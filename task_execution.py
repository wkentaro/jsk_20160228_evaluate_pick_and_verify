#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


csv_file = '2016-02-26.csv'
df = pd.read_csv(csv_file)
print df[['layout', 'verify', 'no_verify']].groupby('layout').mean()