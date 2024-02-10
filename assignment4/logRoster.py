import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


def visual_classifier(X, y, classifier):
    classifier.fit(X, y)
    X_set, y_set = X, y
    X1, X2 = np.meshgrid(
        np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
        np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
    )
    plt.contourf(
        X1,
        X2,
        classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
        alpha=0.75,
        cmap=plt.cm.Paired,
    )
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(
            X_set[y_set == j, 0],
            X_set[y_set == j, 1],
            c=plt.cm.Paired.colors[i],
            label=j,
        )
    plt.title("HS GPA and Math ACT")
    plt.xlabel("Math ACT")
    plt.ylabel("HS GPA")
    plt.legend()
    plt.show()


# Read CSV file
data = pd.read_csv("./classRoster-2.csv")

# Select columns
X = data.iloc[:, [3, 4]].values  # Independent variables
y = data.iloc[:, 5].values  # Dependent variable

# Encode grades using LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Logistic Regression
classifier = LogisticRegression(max_iter=100, random_state=0)

# Visualize classifier
visual_classifier(X, y, classifier)
