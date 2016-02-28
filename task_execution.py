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
success_verify = df.query('not (verify == 0 and no_verify == 0) and verify != -1')
need_verify = df.query('no_verify != 0')

print('''
success_graspone: {g}/{n}
    p: {gp} / {np}
    a: {ga} / {na}
    o: {go} / {no}
success_detect: {d}/{n}
    p: {dp} / {np}
    a: {da} / {na}
    o: {do} / {no}
success_verify: {v}/{nv}
    p: {vp} / {nvp}
    a: {va} / {nva}
    o: {vo} / {nvo}'''.format(
    n=n_data,
    np=len(df.query('layout == "p"')),
    na=len(df.query('layout == "a"')),
    no=len(df.query('layout == "o"')),
    g=len(success_graspone),
    gp=len(success_graspone.query('layout == "p"')),
    ga=len(success_graspone.query('layout == "a"')),
    go=len(success_graspone.query('layout == "o"')),
    d=len(success_detect),
    dp=len(success_detect.query('layout == "p"')),
    da=len(success_detect.query('layout == "a"')),
    do=len(success_detect.query('layout == "o"')),
    v=len(success_verify),
    vp=len(success_verify.query('layout == "p"')),
    va=len(success_verify.query('layout == "a"')),
    vo=len(success_verify.query('layout == "o"')),
    nv=len(need_verify),
    nvp=len(need_verify.query('layout == "p"')),
    nva=len(need_verify.query('layout == "a"')),
    nvo=len(need_verify.query('layout == "o"')),
))