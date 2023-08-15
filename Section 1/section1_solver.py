import matplotlib.pyplot as plt
import pandas as pd

def merge_alleles(input_text):
    output_text = []
    # Extract header line
    header = input_text[0].strip().split()

    # Process each line of data and merge alleles into genotype calls
    genotype_calls = []
    for line in input_text[1:]:
        parts = line.strip().split("\t")
        iid = parts[0]
        genotypes = [f"{parts[i]}{parts[i+1]}" for i in range(1, len(parts), 2)]
        genotype_calls.append([iid] + genotypes)

    # Modify the header to remove "_1" and "_2" suffixes
    modified_header = ["#IID"] + [rs.split("_")[0] for rs in header[1::2]]
    output_text.append(modified_header)
    for call in genotype_calls:
        output_text.append(call)
    return output_text

def form_genotypes():
    # Read the input genotypes.txt file
    with open("genotypes.txt", "r") as input_file:
        lines = input_file.readlines()
    
    output_text = merge_alleles(lines)
    with open("ANSWERS/genotype_merged.txt", "w") as output_file:
        for row in output_text:
            output_file.write("\t".join(row) + "\n")

    print("Genotype calls merged and saved as genotype_merged.txt")

def get_female_patients_under_60(phenotypes, genotypes):
    # Filter female patients under 60 with Type II Diabetes
    filtered_phenotypes = phenotypes[(phenotypes["Gender"] == 0) & (phenotypes["Age"] < 60) & (phenotypes["Type.II.Diabetes"] == 1)]
    # Extract the relevant IDs
    selected_ids = filtered_phenotypes["Arb_ID"].tolist()

     # Get the genotypes for this demographic
    selected_genotypes = genotypes[genotypes["#IID"].isin(selected_ids)]
    # Remove IID column from selected_genotypes
    selected_genotypes = selected_genotypes.drop(columns=["#IID"])
    return selected_genotypes


def generate_plots():
    # Read phenotypes data
    phenotypes = pd.read_csv("phenotypes.txt", sep="\t")

    # Read genotypes data
    genotypes = pd.read_csv("ANSWERS/genotype_merged.txt", sep="\t")

    selected_genotypes = get_female_patients_under_60(phenotypes, genotypes)

    print("Number of female (Gender = 0) patients under the age of 60 that have type II diabetes (cases = 1):", len(selected_genotypes))
    # Plot genotype distribution for each variant
    for col in selected_genotypes.columns:
        plt.figure(figsize=(8, 6))
        plt.title(f"TYPE II Diabetes - Genotype distribution for {col}")
        selected_genotypes[col].value_counts().plot(kind="bar")
        plt.xlabel("Genotype")
        plt.ylabel("Frequency")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(f"ANSWERS/{col}_plot.png")
        plt.close()

def get_old_males_with_high_bmi_missing_genotype(phenotypes, genotype_merged):

    # Define the conditions
    male_patients = phenotypes[(phenotypes["Gender"] == 1)]
    age_condition = male_patients["Age"] > 35

    # Calculate the quartiles for BMI
    bmi_quartiles = phenotypes["BMI"].quantile([0.25, 0.5, 0.75])
    third_quantile_bmi = bmi_quartiles[0.75]

    # Filter for patients with BMI in the 3rd quartile
    bmi_3rd_quartile_condition = male_patients["BMI"] < third_quantile_bmi

    # Find out patients with missing genotypes
    missing_genotype_patients = genotype_merged[genotype_merged.isnull().any(axis=1)]["#IID"]

    # Apply the conditions
    filtered_patients = male_patients[age_condition & bmi_3rd_quartile_condition & male_patients["Arb_ID"].isin(missing_genotype_patients)]

    # Display the count of such patients
    num_patients = len(filtered_patients)
    return num_patients

if __name__ == '__main__':
    # Q2
    form_genotypes()
    # Q3
    generate_plots()
    # Q4

    # Read phenotypes data
    phenotypes = pd.read_csv("phenotypes.txt", sep="\t")

    # Read genotype merged data
    genotype_merged = pd.read_csv("ANSWERS/genotype_merged.txt", sep="\t")
    num_patients = get_old_males_with_high_bmi_missing_genotype(phenotypes, genotype_merged)
    print(f"Number of male patients over 35 with 3rd quartile BMI and missing genotypes: {num_patients}")


