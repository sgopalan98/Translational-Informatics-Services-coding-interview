import pandas as pd
from section1_solver import get_female_patients_under_60

# Sample data for testing
sample_phenotypes = pd.DataFrame({
    "Arb_ID": [1, 2, 3, 4, 5],
    "Gender": [0, 1, 0, 0, 0],
    "Age": [45, 70, 55, 58, 30],
    "Type.II.Diabetes": [1, 0, 1, 1, 0]
})

sample_genotypes = pd.DataFrame({
    "#IID": [1, 2, 3, 4, 5, 6],
    "rs1": ["AA", "AG", "GG", "AA", "AG", "TT"],
    "rs2": ["CC", "CT", "TT", "CC", "CC", "CT"],
    "rs3": ["GG", "AG", "CC", "TT", "GG", "TT"]
})



# Test case 1: Basic scenario with valid data
def test_basic_case():
    result = get_female_patients_under_60(sample_phenotypes, sample_genotypes)
    assert len(result) == 3  # Number of expected rows
    assert list(result.columns) == ["rs1", "rs2", "rs3"]  # Expected columns
    
    # Check if genotype distributions are correct
    rs1_counts = result["rs1"].value_counts()
    print(rs1_counts)
    assert rs1_counts["AA"] == 2
    assert rs1_counts["GG"] == 1

    rs2_counts = result["rs2"].value_counts()
    print(rs2_counts)
    assert rs2_counts["CC"] == 2
    assert rs2_counts["TT"] == 1

    rs3_counts = result["rs3"].value_counts()
    print(rs3_counts)
    assert rs3_counts["GG"] == 1
    assert rs3_counts["CC"] == 1
    assert rs3_counts["TT"] == 1



# Test case 2: No matching patients
def test_no_matching():
    phenotypes = sample_phenotypes.copy()
    phenotypes["Type.II.Diabetes"] = 0
    result = get_female_patients_under_60(phenotypes, sample_genotypes)
    assert len(result) == 0

# Test case 3: No female patients
def test_no_patients():
    phenotypes = sample_phenotypes.copy()
    phenotypes["Gender"] = 1
    result = get_female_patients_under_60(phenotypes, sample_genotypes)
    assert len(result) == 0

# Test case 4: No patients under 60
def test_no_patients_under_60():
    phenotypes = sample_phenotypes.copy()
    phenotypes["Age"] = 65
    result = get_female_patients_under_60(phenotypes, sample_genotypes)
    assert len(result) == 0
