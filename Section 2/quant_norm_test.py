from workflow_runner import quant_norm
import pandas as pd
import random

# TEST 1: same distribution should not be transformed
def test_same():
    row = {}
    for col in ['A', 'B',  'C', 'D']:
        row[col] = random.random() * 100
    same_example = pd.DataFrame({'C1': row,
                   'C2': row})
    actual = quant_norm(same_example)
    
    pd.testing.assert_frame_equal(actual, same_example)


# TEST 2: 1s and 2s must be transformed to 1.5s
def test_one_and_two():
    one_two_example = pd.DataFrame({'C1': {'A': 1, 'B': 1, 'C': 1, 'D': 1},
                   'C2': {'A': 2, 'B': 2, 'C': 2, 'D': 2}})
    actual = quant_norm(one_two_example)

    expected = pd.DataFrame({'C1': {'A': 1.5, 'B': 1.5, 'C': 1.5, 'D': 1.5},
                   'C2': {'A': 1.5, 'B': 1.5, 'C': 1.5, 'D': 1.5}})
    
    pd.testing.assert_frame_equal(actual, expected)

# TEST 3: Wikipedia example - Should match wikipedia output
def test_wikipedia():
    wikipedia_example = pd.DataFrame({'C1': {'A': 5, 'B': 2, 'C': 3, 'D': 4},
                   'C2': {'A': 4, 'B': 1, 'C': 4, 'D': 2},
                   'C3': {'A': 3, 'B': 4, 'C': 6, 'D': 8}})
    actual = quant_norm(wikipedia_example)

    expected = pd.DataFrame({'C1': {'A': 5.666667, 'B': 2.000000, 'C': 3.000000, 'D': 4.666667},
                   'C2': {'A': 4.666667, 'B': 2.000000, 'C': 4.666667, 'D': 3.000000},
                   'C3': {'A': 2.000000, 'B': 3.000000, 'C': 4.666667, 'D': 5.666667}})
    
    pd.testing.assert_frame_equal(actual, expected)
