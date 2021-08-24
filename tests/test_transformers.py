import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
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
    cqe = joblib.load('saved_cqe.joblib')
    out = cqe.transform(X=X_train)
    # print(out)
    assert cqe is not None


def test_is_pipeline_save_possible():
    cqe = joblib.load('saved_cqe.joblib')
    pipe = Pipeline([('categorical_quantile_encoder', cqe),
                     ('scaler', StandardScaler())])
    joblib.dump(cqe, 'pipeline.joblib')
    assert os.path.isfile('pipeline.joblib')


def test_is_pipeline_load_possible(X_train):
    pipeline = joblib.load('pipeline.joblib')
    out = pipeline.transform(X=X_train)
    # remove files after test
    os.remove('saved_cqe.joblib')
    os.remove('pipeline.joblib')
    assert out is not None


"""
import joblib
joblib.dump(vectorizer, 'custom_tfidf_vectorizer.joblib')

var='route_of_administration'
v = joblib.load('custom_tfidf_vectorizer.joblib')
v.fit(train[var])
X_df = v.transform(train[var])

"""
