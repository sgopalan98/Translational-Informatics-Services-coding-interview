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
    # Male female values - shuffled
    male_female_arrays = np.array(['male'] * 5 + ['female'] * 5)
    np.random.shuffle(male_female_arrays)
    # Create the data frame
    num_rows = 10
    data = {
        'Column1': np.random.randint(0, 101, size=num_rows),
        'Column2': np.random.randint(0, 101, size=num_rows),
        'Column3': np.random.randint(0, 101, size=num_rows),
        'Gender': male_female_arrays
    }

    df = pd.DataFrame(data)
    print(df)
    # Melt the data frame using 'Gender' - 4th column as ID (Assumption: Melting on a column)
    melted_df = pd.melt(df, id_vars=['Gender'], var_name='Attribute', value_name='Value')
    # Sort the melted data frame (Assumption: Sorting by Value)
    sorted_melted_df = melted_df.sort_values(by = ['Value'])
    # Filter and return results for males from 'Column1'
    filtered_male_df = sorted_melted_df[(sorted_melted_df["Attribute"] == "Column1") & (sorted_melted_df["Gender"] == "male")]
    
    print("Final dataframe")
    print(filtered_male_df)

    print("Maximum value from Column 1 is ", melted_df[(melted_df["Attribute"] == "Column1")]['Value'].max())
    print("Minimum value from Column 2 is ", melted_df[(melted_df["Attribute"] == "Column2")]['Value'].min())
    print("Maximum value from Column 2 is ", melted_df[(melted_df["Attribute"] == "Column2")]['Value'].max())

    filtered_male_df.to_csv('ANSWERS/df.csv', index = False)

if __name__ == "__main__":
    main()