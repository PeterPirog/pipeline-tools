import pandas as pd
import joblib
from transformers import CategoriclalQuantileEncoder
import joblib
import os.path


def test_df_train_is_output(X_train, y_train):
    cqe = CategoriclalQuantileEncoder()
    out = cqe.fit_transform(X=X_train, y=y_train)
    print(out)
    assert out is not None


def test_is_transformer_save_possible(X_train, y_train):
    cqe = CategoriclalQuantileEncoder()
    out = cqe.fit_transform(X=X_train, y=y_train)
    joblib.dump(cqe, 'saved_cqe.joblib')
    assert os.path.isfile('saved_cqe.joblib')

def test_is_transformer_load_possible(X_train):
    cqe=joblib.load('saved_cqe.joblib')
    out = cqe.transform(X=X_train)
    print(out)
    assert cqe is not None


"""
import joblib
joblib.dump(vectorizer, 'custom_tfidf_vectorizer.joblib')

var='route_of_administration'
v = joblib.load('custom_tfidf_vectorizer.joblib')
v.fit(train[var])
X_df = v.transform(train[var])

"""
