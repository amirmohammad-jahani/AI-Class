from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

data = {
    "income": [
        25, 45, 18, 60, 35, 12, 80, 50, 22, 70,
        40, 15, 90, 30, 55, 20, 65, 10, 75, 48,
        28, 85, 33, 58, 14, 95, 42, 24, 68, 38,
        52, 16, 78, 32, 62, 19, 88, 44, 27, 72,
        36, 100, 21, 57, 13, 82, 46, 29, 63, 39
    ],

    "credit_score": [
        3, 2, 1, 3, 2, 1, 3, 2, 1, 3,
        2, 1, 3, 1, 3, 1, 3, 1, 3, 2,
        1, 3, 1, 3, 1, 3, 2, 1, 3, 2,
        3, 1, 3, 1, 3, 1, 3, 2, 1, 3,
        2, 3, 1, 3, 1, 3, 2, 1, 3, 2
    ],

    "age": [
        25, 35, 22, 45, 31, 19, 50, 38, 27, 42,
        33, 21, 55, 29, 40, 24, 47, 18, 52, 36,
        26, 58, 30, 43, 20, 60, 34, 23, 49, 32,
        39, 22, 54, 28, 46, 25, 57, 37, 24, 51,
        31, 62, 27, 41, 19, 56, 35, 26, 48, 33
    ],

    "history": [
        85, 72, 25, 95, 68, 15, 90, 78, 30, 88,
        75, 20, 98, 35, 82, 28, 91, 10, 96, 70,
        22, 93, 40, 87, 18, 99, 76, 32, 92, 65,
        84, 12, 94, 38, 89, 24, 97, 73, 29, 90,
        67, 100, 21, 86, 16, 95, 79, 34, 88, 71
    ],

    "approve": [
        1, 1, 0, 1, 1, 0, 1, 1, 0, 1,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 1,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 1,
        1, 0, 1, 0, 1, 0, 1, 1, 0, 1,
        1, 1, 0, 1, 0, 1, 1, 0, 1, 1
    ]
}
df = pd.DataFrame(data)
X = df.drop("approve", axis=1)
y = df["approve"]  

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = tree.DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Actual:", y_test.values)



