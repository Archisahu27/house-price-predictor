# predict.py

import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

def predict_price(rm, lstat, ptratio):
    # Input must be 2D list
    features = [[rm, lstat, ptratio]]
    
    prediction = model.predict(features)[0]
    
    return round(prediction, 2)


# Test (temporary)
if __name__ == "__main__":
    price = predict_price(6.5, 12.0, 15.0)
    print("Predicted Price:", price)