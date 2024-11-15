import pickle

# Load the model from the pickle file
with open('model_pickle2', 'rb') as f:
    model = pickle.load(f)

def predict_house_price(area, bedrooms, age):
    # Input data as an array for model prediction
    input_data = [[area, bedrooms, age]]
    # Predict house price
    predicted_price = model.predict(input_data)
    return predicted_price[0]
