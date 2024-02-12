import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from logistic_utils import visualize_classifier

data = pd.read_csv("./classRoster-2.csv")

X = data.iloc[:, [3, 4]].values
y = data.iloc[:, 5].values

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

classifier = LogisticRegression(max_iter=100, random_state=0)

classifier.fit(X, y)

visualize_classifier(classifier, X, y)
