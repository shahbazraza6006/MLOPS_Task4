from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

# Load the dataset
data = pd.read_csv("car_prices.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.json
    year = request_data['year']
    odometer = request_data['odometer']
    
    # Filter the data based on year and odometer
    filtered_data = data[(data['year'] == int(year)) & (data['odometer'] == int(odometer))]
    
    # Use the filtered data for prediction
    prediction = model.predict(filtered_data[['year', 'odometer']])
    
    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=False)
