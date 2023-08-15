from section1_solver import get_old_males_with_high_bmi_missing_genotype
import pandas as pd
from io import StringIO


# Common test data
phenotypes_test_data_no_missing = """
Arb_ID	Age	Gender	BMI	Type.II.Diabetes
3669281929	78	1	26.5	1
34610262659	40	1	27.0	1
42673757023	69	1	29.5	0
68012749485	45	1	25.5	1
55979726895	38	0	30.0	1
1549214769	57	0	28.0	0
65306482423	62	0	31.5	1
48931107252	40	0	24.5	0
37662218447	50	1	27.5	0
7718430122	23	1	26.0	0
"""
phenotypes_test_data_all_male = """
Arb_ID	Age	Gender	BMI	Type.II.Diabetes
3669281929	36	1	26.5	1
34610262659	36	1	27.0	1
42673757023	36	1	29.5	0
68012749485	36	1	25.5	1
55979726895	36	1	30.0	1
1549214769	36	1	28.0	0
65306482423	36	1	31.5	1
48931107252	36	1	24.5	0
37662218447	36	1	27.5	0
7718430122	36	1	26.0	0
"""


# TEST 1: Should return 0 as no genotype is missing
def test_filter_patients_basic():

    genotype_merged_test_data_no_missing = """
#IID	rs1421085_1	rs1421085_2	rs7074440_1	rs7074440_2
3669281929	TT	TT	GG	GG
34610262659	CC	CC	AA	AA
42673757023	TT	TT	GG	GG
68012749485	CC	CC	AA	AA
55979726895	CC	TT	AA	GG
1549214769	CC	CC	GG	GG
65306482423	CC	TT	AA	GG
48931107252	CC	CC	GG	GG
37662218447	CC	TT	AA	GG
7718430122	CC	CC	AA	GG
"""
    # Load test data into dataframes
    phenotypes_test_df = pd.read_csv(StringIO(phenotypes_test_data_no_missing), sep="\t")
    genotype_merged_test_df = pd.read_csv(StringIO(genotype_merged_test_data_no_missing), sep="\t")
    
    # Test the filter_patients function
    result = get_old_males_with_high_bmi_missing_genotype(phenotypes_test_df, genotype_merged_test_df)
    
    # Expected results for the test data
    expected_result = 0
    
    assert result == expected_result, f"Expected: {expected_result}, Got: {result}"




# TEST 2: Should return 0 as no male is present
def test_filter_patients_no_male():
    phenotypes_test_data_no_male = """
Arb_ID	Age	Gender	BMI	Type.II.Diabetes
3669281929	78	0	26.5	1
34610262659	40	0	27.0	1
42673757023	69	0	29.5	0
68012749485	45	0	25.5	1
55979726895	38	0	30.0	1
1549214769	57	0	28.0	0
65306482423	62	0	31.5	1
48931107252	40	0	24.5	0
37662218447	50	0	27.5	0
7718430122	23	0	26.0	0
"""

    genotype_merged_test_data_no_male = """
#IID	rs1421085_1	rs1421085_2	rs7074440_1	rs7074440_2
3669281929	TT	TT	GG	
34610262659	CC	CC	AA	
42673757023	TT	TT	GG	
68012749485	CC	CC	AA	
55979726895	CC	TT	AA	
1549214769	CC	CC	GG	
65306482423	CC	TT	AA	
48931107252	CC	CC	GG	
37662218447	CC	TT	AA	
7718430122	CC	CC	AA	
"""
    # Load test data into dataframes
    phenotypes_test_df = pd.read_csv(StringIO(phenotypes_test_data_no_male), sep="\t")
    genotype_merged_test_df = pd.read_csv(StringIO(genotype_merged_test_data_no_male), sep="\t")
    
    # Test the filter_patients function
    result = get_old_males_with_high_bmi_missing_genotype(phenotypes_test_df, genotype_merged_test_df)
    
    # Expected results for the test data
    expected_result = 0
    
    assert result == expected_result, f"Expected: {expected_result}, Got: {result}"





# TEST 3: Should return 0 as no male is above 35
def test_filter_patients_no_age():
    phenotypes_test_data_no_age = """
Arb_ID	Age	Gender	BMI	Type.II.Diabetes
3669281929	10	0	26.5	1
34610262659	10	0	27.0	1
42673757023	10	0	29.5	0
68012749485	10	0	25.5	1
55979726895	10	0	30.0	1
1549214769	10	0	28.0	0
65306482423	10	0	31.5	1
48931107252	10	0	24.5	0
37662218447	10	0	27.5	0
7718430122	10	0	26.0	0
"""

    genotype_merged_test_data_no_age = """
#IID	rs1421085_1	rs1421085_2	rs7074440_1	rs7074440_2
3669281929	TT	TT	GG	
34610262659	CC	CC	AA	
42673757023	TT	TT	GG	
68012749485	CC	CC	AA	
55979726895	CC	TT	AA	
1549214769	CC	CC	GG	
65306482423	CC	TT	AA	
48931107252	CC	CC	GG	
37662218447	CC	TT	AA	
7718430122	CC	CC	AA	
"""
    # Load test data into dataframes
    phenotypes_test_df = pd.read_csv(StringIO(phenotypes_test_data_no_age), sep="\t")
    genotype_merged_test_df = pd.read_csv(StringIO(genotype_merged_test_data_no_age), sep="\t")
    
    # Test the filter_patients function
    result = get_old_males_with_high_bmi_missing_genotype(phenotypes_test_df, genotype_merged_test_df)
    
    # Expected results for the test data
    expected_result = 0
    
    assert result == expected_result, f"Expected: {expected_result}, Got: {result}"



# TEST 4: Should return many as only many is < third quartile and has one of the genotypes missing
def test_filter_patients_missing():
    genotype_merged_test_data_many_missing = """
#IID	rs1421085_1	rs1421085_2	rs7074440_1	rs7074440_2
3669281929		TT	GG	GG
34610262659		CC	AA	AA
42673757023	TT	TT	GG	AA
68012749485	CC		AA	AA
55979726895	CC	TT	AA	GG
1549214769	CC		GG	GG
65306482423	CC	TT	AA	GG
48931107252	CC	CC	GG	GG
37662218447	CC	TT	AA	GG
7718430122	CC	CC	AA	GG
"""
    # Load test data into dataframes
    phenotypes_test_df = pd.read_csv(StringIO(phenotypes_test_data_all_male), sep="\t")
    genotype_merged_test_df = pd.read_csv(StringIO(genotype_merged_test_data_many_missing), sep="\t")
    
    # Test the filter_patients function
    result = get_old_males_with_high_bmi_missing_genotype(phenotypes_test_df, genotype_merged_test_df)
    
    # Expected results for the test data
    expected_result = 4
    
    assert result == expected_result, f"Expected: {expected_result}, Got: {result}"





# TEST 5: Should return all values >= 3rd quantile (all data - male, above 35)
def test_filter_patients_all():

    genotype_merged_test_data_all = """
#IID	rs1421085_1	rs1421085_2	rs7074440_1	rs7074440_2
3669281929	TT	TT	GG	
34610262659	CC	CC	AA	
42673757023	TT	TT	GG	
68012749485	CC	CC	AA	
55979726895	CC	TT	AA	
1549214769	CC	CC	GG	
65306482423	CC	TT	AA	
48931107252	CC	CC	GG	
37662218447	CC	TT	AA	
7718430122	CC	CC	AA	
"""
    # Load test data into dataframes
    phenotypes_test_df = pd.read_csv(StringIO(phenotypes_test_data_all_male), sep="\t")
    genotype_merged_test_df = pd.read_csv(StringIO(genotype_merged_test_data_all), sep="\t")
    
    # Test the filter_patients function
    result = get_old_males_with_high_bmi_missing_genotype(phenotypes_test_df, genotype_merged_test_df)
    
    # Expected results for the test data
    expected_result = 7
    
    assert result == expected_result, f"Expected: {expected_result}, Got: {result}"
