"""Homwork 4 is all about PEP8 compliance"""
# (1 pt). Create a python module called test_dataframe.py that
# has a test that replicates what was done in item
# (2) for HW2

import hw2Module as hw2

URL = 'https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD'
DATA = hw2.create_dataframe(URL)
COL_NAMES = list(DATA.columns)

# this test SHOULD FAIL because the column
# values do not all have the same data type


def test_rep_hw2():
    '''Function 1: Atest that replicates what was done in item
    (2) for HW2'''
    test_match_col_names = list(DATA.columns)

    if test_match_col_names == COL_NAMES:
        next
    else:
        raise ValueError("specified columns: false")

    if len(DATA) < 10:
        raise ValueError("desired num rows: false")

    trues = []
    for column in DATA.columns:
        value_type = (DATA[column].apply(lambda x: type(x)).nunique())
        trues.append(value_type)

    if sum(trues) > len(DATA.columns):
        raise ValueError("Column values all have same data type: false")

# this test SHOULD FAIL because the column
# values do not all have the same data type


def test_correct_types():
    '''Creates a test that checks that each column has values of the
    correct type'''
    trues = []
    for column in DATA.columns:
        value_type = (DATA[column].apply(lambda x: type(x)).nunique())
        trues.append(value_type)
    if sum(trues) > len(DATA.columns):
        raise ValueError("Values in columns do not all have same type")

# this test SHOULD FAIL because there are nans in the data frame


def test_nans():
    '''Creates a tests that checks for NANs in dataframe'''
    if any(DATA.isnull()):
        raise ValueError(
            "Nans exist in data set. Use fxn data[column].isnull()\
            to test presence of NaNs")

# this test SHOULD PASS because there are more
# than 1 rows in the data frame


def test_rows_dataframe():
    '''Creates a test that checks that the dataframe has more than 1 row'''
    if len(DATA) < 1:
        raise ValueError("Data does not have at least 1 row")
