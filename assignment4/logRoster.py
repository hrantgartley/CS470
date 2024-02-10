import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from logistic_utils import visualize_classifier

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

# Train the classifier
classifier.fit(X, y)

# Visualize classifier using the existing function
visualize_classifier(classifier, X, y)
