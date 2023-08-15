from Section_1.section1_solver import merge_alleles

# TEST 1: It should merge the alleles
def test_merge_alleles_basic():
    genotypes_test_data = """
    #IID    rs1421085_1 rs1421085_2 rs7074440_1 rs7074440_2
    3669281929	T	T	G	G
    34610262659	C	C	A	A
    42673757023	T	T	G	G
    68012749485	C	C	A	A
    55979726895	C	T	A	G
    1549214769	C	C	G	G
    65306482423	C	T	A	G
    48931107252	C	C	G	G
    37662218447	C	T	A	G
    7718430122	C	C	G	G
    """
    genotypes =  genotypes_test_data.split('\n')[1:-1]
    # Test the merge_alleles function
    result = merge_alleles(genotypes)
    
    # Expected results for the test data
    expected_result = [
        ['#IID', 'rs1421085', 'rs7074440'], 
        ['3669281929', 'TT', 'GG'], 
        ['34610262659', 'CC', 'AA'], 
        ['42673757023', 'TT', 'GG'], 
        ['68012749485', 'CC', 'AA'], 
        ['55979726895', 'CT', 'AG'], 
        ['1549214769', 'CC', 'GG'], 
        ['65306482423', 'CT', 'AG'], 
        ['48931107252', 'CC', 'GG'], 
        ['37662218447', 'CT', 'AG'], 
        ['7718430122', 'CC', 'GG'], 
        ]
    print(result)
    print(expected_result)
    assert len(result) == len(expected_result)
    compare_results(result, expected_result)


# TEST 2: It should merge the alleles leaving the blanks
def test_merge_alleles_missing():
    genotypes_test_data_missing = """
    #IID    rs1421085_1 rs1421085_2 rs7074440_1 rs7074440_2
    3669281929	T	T       
    34610262659	C	C	A	A
    42673757023	T	T	G	G
    68012749485	C	C	A	A
    55979726895	C	T	A	G
    1549214769	C	C	G	G
    65306482423	C	T	A	G
    48931107252	C	C	G	G
    37662218447	C	T	A	G
    7718430122	C	C	G	G
    """
    genotypes =  genotypes_test_data_missing.split('\n')[1:-1]
    # Test the merge_alleles function
    result = merge_alleles(genotypes)
    
    # Expected results for the test data
    expected_result = [
        ['#IID', 'rs1421085', 'rs7074440'], 
        ['3669281929', 'TT', ''], 
        ['34610262659', 'CC', 'AA'], 
        ['42673757023', 'TT', 'GG'], 
        ['68012749485', 'CC', 'AA'], 
        ['55979726895', 'CT', 'AG'], 
        ['1549214769', 'CC', 'GG'], 
        ['65306482423', 'CT', 'AG'], 
        ['48931107252', 'CC', 'GG'], 
        ['37662218447', 'CT', 'AG'], 
        ['7718430122', 'CC', 'GG'], 
        ]
    print(result)
    print(expected_result)
    assert len(result) == len(expected_result)
    compare_results(result, expected_result)




def compare_results(actual, expected):
    assert len(actual) == len(expected)
    for row1, row2 in zip(actual, expected):
        assert all([a == b for a, b in zip(row1, row2)])