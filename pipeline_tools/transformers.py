import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class CategoriclalQuantileEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, features=None, ignored_features=None, p=0.5, m=1, remove_original=True, return_df=True,
                 handle_missing_or_unknown='value'):
        super().__init__()
        self.features = features  # selected categorical features
        self.ignored_features = ignored_features
        self.columns = None  # all columns in df
        self.column_target = None
        self.p = p
        self.m = m
        self.remove_original = remove_original
        self.return_df = return_df
        self.handle_missing_or_unknown = handle_missing_or_unknown  # 'value' or ‘return_nan’

        self.features_unique = {}  # dict with unique values lists for specified feature, key form (feature)
        self.global_quantiles = {}  # stored quantiles for whole dataset, key form (p)
        self.value_quantiles = {}  # stored quantiles for all values, key form (feature, value, p)
        self.value_counts = {}  # stored counts of every value in train data key form (feature, value)

        # convert p and m to lists for iteration available
        if isinstance(p, int) or isinstance(p, float):
            self.p = [self.p]
        if isinstance(m, int) or isinstance(m, float):
            self.m = [self.m]

        # convert feature lists for iteration available
        if not isinstance(self.features, list) and self.features is not None:
            self.features = [self.features]

        if not isinstance(self.ignored_features, list) and self.ignored_features is not None:
            self.ignored_features = [self.ignored_features]

    def fit(self, X, y=None):
        y = y.to_frame().copy()
        Xy = pd.concat([X, y], axis=1)
        print(Xy)
        self.columns = X.columns
        # Find only categorical columns if not defines
        if self.features is None:
            self.features = [col for col in self.columns if X[col].dtypes == 'O']
        else:
            if isinstance(self.features, str):  # convert single feature name to list for iteration possibility
                self.features = [self.features]
        # Remove ignored features
        if self.ignored_features is not None:
            for ignored_feature in self.ignored_features:
                self.features.remove(ignored_feature)

        # Find unique values for specified features
        for feature in self.features:
            self.features_unique[feature] = list(X[feature].unique())

        # Find quantiles for all dataset for each value of p
        for p in self.p:
            self.global_quantiles[p] = np.quantile(y, p)

        # Find quantiles for every feature and every value
        for feature in self.features:
            for value in list(X[feature].unique()):  # for every unique value
                # Find y values for specified feature and specified value
                idx = Xy[feature] == value
                y_group = y[idx]
                # counts for every feature and every value
                self.value_counts[feature, value] = len(y_group)
                # print(f'n={self.value_counts[feature, value]} for feature={feature}, value={value}')

                for p in self.p:
                    self.value_quantiles[feature, value, p] = np.quantile(y_group, p)
        return self

    def transform(self, X):
        X = X.copy()

        # Create new columns for quantile values
        for feature in self.features:
            X[feature] = X[feature].replace(np.nan, 'MISSING')
            X[feature] = X[feature].apply(lambda value: value if value in self.features_unique[feature] else 'UNKNOWN')
            for p in self.p:
                for m in self.m:
                    # Prepare new columns names
                    feature_name = feature + '_' + str(p) + '_' + str(m)

                    # return global quantile values if input value is nan or unknown
                    if self.handle_missing_or_unknown == 'value':
                        X[feature_name] = self.global_quantiles[p]
                        X[feature_name] = X[feature].apply(lambda value: self.global_quantiles[p]
                        if value == "MISSING" or value == 'UNKNOWN'
                        # Quantile Encoder: Tackling High Cardinality Categorical Features in Regression Problems, equation 2
                        else (self.value_counts[feature, value] * self.value_quantiles[feature, value, p] +
                              m * self.global_quantiles[p]) / (self.value_counts[feature, value] + m))

                    # return nan if input value is nan or unknown
                    if self.handle_missing_or_unknown == 'return_nan':
                        X[feature_name] = self.global_quantiles[p]
                        X[feature_name] = X[feature].apply(lambda value: np.nan
                        if value == "MISSING" or value == 'UNKNOWN'
                        # Quantile Encoder: Tackling High Cardinality Categorical Features in Regression Problems, equation 2
                        else (self.value_counts[feature, value] * self.value_quantiles[feature, value, p] +
                              m * self.global_quantiles[p]) / (self.value_counts[feature, value] + m))

        # Remove original features
        if self.remove_original:
            X = X.drop(self.features, axis=1)

        # Return dataframe or np array
        if self.return_df:
            return X
        else:
            return X.to_numpy()