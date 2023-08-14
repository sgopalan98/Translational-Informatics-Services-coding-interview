#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:43:37 2023

@author: harrysmith
"""

import pandas as pd
import numpy as np

np.random.seed(42) # Do not edit this line!

df = pd.DataFrame(np.random.randint(a,b,size=(10, 3)), columns=list('abc'))
df['d'] = np.random.randint(c,d,size=(10,1))
df['d'].replace(0, 'female')
df['d'].replace(1, 'male')


df.rename(columns={"a": "Col1"}) 
df.rename(columns={"b": "Col2"})
df.rename(columns={"c": "col3"})


for col in df.columns:
    mean = df[col].mean() 
    if df['Col1'].mean() > 10: 
        for col in df.columns:
            print(df['Col2'].min()) 
    else:
        for col in df.columns:
            print(df[col].max())



# hard coded file path
df.to_csv('/Documents/smiharry/project1/results/df.csv', index=False)
