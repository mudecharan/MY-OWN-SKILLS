"""model-selection-advisor · baseline ladder with fair, repeated comparison.
Usage: python baseline_ladder.py --data data.csv --target y --task classification
"""
import argparse
import time

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_pipelines(X, task):
    num = X.select_dtypes(include=np.number).columns
    cat = [c for c in X.columns if c not in num]
    pre = ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler())]), num),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat),
    ])
    if task == "classification":
        from sklearn.dummy import DummyClassifier
        return {
            "0-rules(majority)": Pipeline([("pre", pre), ("m", DummyClassifier(strategy="most_frequent"))]),
            "1-logistic": Pipeline([("pre", pre), ("m", LogisticRegression(max_iter=2000))]),
            "2-gbt": Pipeline([("pre", pre), ("m", GradientBoostingClassifier(random_state=0))]),
        }
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.linear_model import Ridge
    return {"1-ridge": Pipeline([("pre", pre), ("m", Ridge())]),
            "2-gbt": Pipeline([("pre", pre), ("m", GradientBoostingRegressor(random_state=0))])}


class MajorityBaseline:
    """Rung 0: always predict majority class / mean — the model must beat this.
    Wrapped in cross_val_score via a lambda-free callable; sklearn-tag compatible
    by delegating to DummyClassifier under the hood."""
    def __init__(self):
        from sklearn.dummy import DummyClassifier
        self._m = DummyClassifier(strategy="most_frequent")

    def get_params(self, deep=True):
        return self._m.get_params(deep)

    def set_params(self, **kw):
        self._m.set_params(**kw)
        return self

    def fit(self, X, y):
        self._m.fit(X, y)
        return self

    def predict(self, X):
        return self._m.predict(X)

    def __sklearn_is_fitted__(self):
        try:
            return hasattr(self._m, "classes_")
        except Exception:
            return False

    def __getattr__(self, name):
        # expose fitted attributes (classes_, etc.) from the inner estimator
        if name.startswith("__") or name == "_m":
            raise AttributeError(name)
        return getattr(self.__dict__["_m"], name)

    @property
    def __sklearn_tags__(self):
        from sklearn.dummy import DummyClassifier
        return DummyClassifier().__sklearn_tags__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--task", choices=["classification", "regression"], default="classification")
    a = ap.parse_args()

    df = pd.read_csv(a.data)
    y = df[a.target]
    X = df.drop(columns=[a.target])

    results = []
    for name, pipe in build_pipelines(X, a.task).items():
        t0 = time.time()
        try:
            scores = cross_val_score(pipe, X, y, cv=5,
                                     scoring="roc_auc" if a.task == "classification" else "r2")
            fit_s = time.time() - t0
            ci = 1.96 * scores.std(ddof=1) / np.sqrt(len(scores))
            results.append((name, scores.mean(), ci, fit_s))
            print(f"{name:<22} score={scores.mean():.3f} ±{ci:.3f}   fit={fit_s:.1f}s")
        except Exception as e:
            print(f"{name:<22} FAILED: {e}")

    # winner check: does rung N+1 beat rung N beyond CI overlap?
    ok = all(results[i + 1][1] - results[i][1] > (results[i][2] + results[i + 1][2]) * 0.5
             for i in range(len(results) - 1))
    print("\nEscalation justified at every rung:", "yes" if ok else "NO — prefer the simpler model")


if __name__ == "__main__":
    main()
