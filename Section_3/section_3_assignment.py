#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Section 3 data manipulator!

Created on Tue Jul 25 15:43:37 2023
@author: harrysmith
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
    # Melt the data frame on the 'Gender' column
    melted_df = pd.melt(df, id_vars=['Column1', 'Column2', 'Column3'], value_vars=['Gender'], var_name='Attribute', value_name='Value')
    # Sort the melted data frame
    sorted_melted_df = melted_df.sort_values(by=['Column1', 'Column2', 'Column3'])
    # Filter and return results for males from 'Column1'
    filtered_male_df = sorted_melted_df[(sorted_melted_df['Value'] == 'male')]
    
    print("Final dataframe")
    print(filtered_male_df)

    print("Maximum value from Column 1 is ", df['Column1'].max())
    print("Minimum value from Column 2 is ", df['Column2'].min())
    print("Maximum value from Column 2 is ", df['Column2'].max())

    filtered_male_df.to_csv('ANSWERS/df.csv', index = False, columns = ['Column1'])

if __name__ == "__main__":
    main()