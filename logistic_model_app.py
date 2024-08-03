
# Dataset Creation -> same one from week 4 

import pandas as pd

data = [
    [1,1,1],
    [2,1,1],
    [3,2,0],
    [4,2,0],
    [5,3,1],
    [6,3,1]
]

# Converts list of lists into  DataFrame where x contains features while y contains labels
df = pd.DataFrame(data, columns=['feature1', 'feature2', 'label'])
x = df[['feature1', 'feature2']]
y = df['label']


# Train and save model 

from sklearn.linear_model import LogisticRegression
import joblib
import os

# Trains logistic regression model using dataset 
model = LogisticRegression() # creates instance of logistic regression model 
model.fit(x, y) # trains model with features 'x' and labels 'y' 

# Save the trained model into file 
joblib.dump(model, 'simple_model.pkl') # saves trained model to file 

print("Model saved:", os.path.exists('simple_model.pkl')) # checks if file was saved correctly 

# Create and deploy flask app 

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__) # initializes flask application 
model = joblib.load('simple_model.pkl') # loads trained model from file 

@app.route('/predict', methods=['POST']) # defines endpoint that accepts POST requests
def predict():
    data = request.get_json(force=True) # retrieves JSON data sent to the '/predict' endpoint
    features = np.array(data['features']).reshape(1, -1) # converts the features from JSON into a NumPy array and reshapes to match model's input 
    prediction = model.predict(features) # makes prediction using trained model 
    return jsonify({'prediction': int(prediction[0])}) # returns prediction in JSON format 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Make sure the app is accessible externally

