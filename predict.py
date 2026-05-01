# predict.py

import pickle
import os

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct path to model
model_path = os.path.join(BASE_DIR, "model.pkl")

# Load model safely
model = pickle.load(open(model_path, "rb"))


def predict_price(rm, lstat, ptratio):
    features = [[rm, lstat, ptratio]]
    prediction = model.predict(features)[0]
    return round(prediction, 2)


# Test locally
if __name__ == "__main__":
    price = predict_price(6.5, 12.0, 15.0)
    print("Predicted Price:", price)