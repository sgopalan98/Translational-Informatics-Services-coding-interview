#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Section 2 workflow runner!

@author: Santy
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import qnorm

def quant_norm(df_input):
    df = df_input.copy()
    #Sort the columns
    data_dic = {}
    for col in df:
        data_dic.update({col : sorted(df[col])})
    sorted_df = pd.DataFrame(data_dic)

    
    # Compute mean across data of the same rank
    mean = sorted_df.mean(axis = 1).tolist()

    # Sort and replace with means 
    for col in df:
        ordered_indices = np.searchsorted(np.sort(df[col]), df[col])
        df[col] = [mean[index] for index in ordered_indices]
    return df

def generate_quant_normalization(data_path):
    # Load the data from the file
    df = pd.read_csv(data_path, sep="\t")
    quant_norm_df = qnorm.quantile_normalize(df.iloc[:, 1:])
    quant_norm_df.insert(0, "Gene", df['Gene'].values)
    quant_norm_df.to_csv('ANSWERS/qnorm.txt', index = False, sep = '\t')
    print("Quantitaive normalized data generated in qnorm.txt")
    return

def generate_violet_plot_wrt_regulation(data_path, regulation_path):
    # Read the data file
    data_df = pd.read_csv(data_path, delimiter="\t")
    # Read the regulation file
    regulation_df = pd.read_csv(regulation_path, delimiter="\t")

    # Merge the two dataframes based on the "Gene" column
    merged_df = pd.merge(data_df, regulation_df, on="Gene")

    # Set style
    sns.set(style="whitegrid")

    # Create the violin plot
    plt.figure(figsize=(10, 6))
    sns.violinplot(x="Regulation_status", y="expression7", data=merged_df, palette="Set3")

    # Add labels and title
    plt.xlabel("Regulation Status")
    plt.ylabel("Expression 7")
    plt.title("Distribution of Gene Expression 7 Across Regulation Status")

    # Save the plot as a PNG file
    plt.savefig("ANSWERS/violin_plot.png")
    return


def run():
    generate_quant_normalization('TIS_raw_input1.txt')
    generate_violet_plot_wrt_regulation('TIS_raw_input1.txt', 'TIS_raw_input2_regulation_status.txt')
    return

if __name__ == "__main__":
    run()

