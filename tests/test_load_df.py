import pandas as pd
from load_df import load_train_df, load_test_df

import pytest


def test_df_train_is_loaded(df_train, train_columns):
    df = df_train
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == train_columns
    assert df.shape == (1460, 81)


def test_df_test_is_loaded(df_test, test_columns):
    df = df_test
    assert isinstance(df, pd.DataFrame)

    assert list(df.columns) == test_columns
    assert df.shape == (1459, 80)

@pytest.mark.skip
def test_maximum_range(test_columns, train_maximums, test_maximums):
    N = len(test_maximums)
    for i in range(N):
        #print(f'Column:{test_columns[i]}')
        assert train_maximums[i] >= test_maximums[i]

@pytest.mark.skip
def test_minimum_range(test_columns, train_minimums, test_minimums):
    N = len(test_minimums)
    for i in range(N):
        #print(f'Column:{test_columns[i]}')
        assert train_minimums[i] <= test_minimums[i]
