#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:43:37 2023

@author: harrysmith, Santy
"""

import pandas as pd
import numpy as np

np.random.seed(42) # Do not edit this line!


def main():
    # Create the data frame
    num_rows = 10
    data = {
        'Column1': np.random.randint(0, 101, size=num_rows),
        'Column2': np.random.randint(0, 101, size=num_rows),
        'Column3': np.random.randint(0, 101, size=num_rows),
        'Gender': np.random.choice(['female', 'male'], size=num_rows, p=[0.5, 0.5])
    }

    df = pd.DataFrame(data)
    # Melt the data frame on the 'Gender' column
    melted_df = pd.melt(df, id_vars=['Column1', 'Column2', 'Column3'], value_vars=['Gender'], var_name='Attribute', value_name='Value')
    # Sort the melted data frame
    sorted_melted_df = melted_df.sort_values(by=['Column1', 'Column2', 'Column3'])
    # Filter and return results for males from 'Column1'
    filtered_male_df = sorted_melted_df[(sorted_melted_df['Value'] == 'male') & (sorted_melted_df['Attribute'] == 'Gender')]
    
    print("Final dataframe")
    print(filtered_male_df)

    print("Maximum value from Column 1 is ", filtered_male_df['Column1'].max())
    print("Minimum value from Column 2 is ", filtered_male_df['Column2'].min())
    print("Maximum value from Column 2 is ", filtered_male_df['Column2'].max())

    filtered_male_df['Column1'].to_csv('df.csv', index = False)

if __name__ == "__main__":
    main()