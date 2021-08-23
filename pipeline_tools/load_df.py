# %%
import pandas as pd

pd.set_option('display.max_columns', None)


def load_train_df():
    df = pd.read_csv('../tests/data/train.csv')
    return df


def load_test_df():
    df = pd.read_csv('../tests/data/test.csv')
    return df


# %%
if __name__ == '__main__':
    df = load_train_df()
    # print(df.head)
    # %%
    print(df.describe())
