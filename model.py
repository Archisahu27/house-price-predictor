# model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# 1. Load dataset
data = pd.read_csv("housing.csv")

# 2. Select only required columns
data = data[["rm", "lstat", "ptratio", "medv"]]

# 3. Split into features and target
X = data[["rm", "lstat", "ptratio"]]
y = data["medv"]

# 4. Train model
model = LinearRegression()
model.fit(X, y)

# 5. Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")