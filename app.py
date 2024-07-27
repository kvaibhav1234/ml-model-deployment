
"""
Step 1: 
- Create a simple toy dataset for binary classification problem. 

- data: varibale that contains dataset -> list of lists 
    - inner list: datapoint with three values 
        - [1,1,1] -> feature1 = 1, feature2 = 1, label = 1
"""

data = [
    [1,1,1], 
    [2,1,1,],
    [3,2,0],
    [4,2,0],
    [5,3,1],
    [6,3,1]
]

import pandas as pd 

# Converts the list of lists into Pandas DataFrame with specificied column names. 
df = pd.DataFrame(data, columns=['feature1','feature2','label'])

# Selects feature columns (feature1 and feature2) from the DataFrame. 
x = df[['feature1', 'feature2']]

# Selects the label column (label) from the DataFrame. 
y = df['label']

"""
Step 2: Saving the Model 
- Run simple logistic regression model and save it.
"""

from sklearn.linear_model import LogisticRegression # Logistic Regression is a popular machine learning library. 
import joblib # Used to save and load Python objects

model = LogisticRegression() # Creates instance of Logisitic Regression model. 
model.fit(x,y) # Trains the Logisitic Regression model using feature data (x) and label data (y). 

joblib.dump(model, 'simple_model.pkl') # saves trained model to file 

import os 
print("Model saved:", os.path.exists('simple_mode.pkl'))

"""
Step 3: Deploy the Model on Flask 
"""

from flask import Flask, request, jsonify # Imports Flask, a lightweight frame web application framework. 
import joblib 
import numpy as np 

model = joblib.load('simple_model.pkl') # Load the pre-trained model using joblib 

app = Flask(__name__) # Initializes new Flask application instance. 

@app.route('/predict', methods=['POST']) # Defining a route '/predict' tha accepts POST requests. 
def predict(): 
    data = request.get_json(force=True) # Get the JSON data from the request 
    features = np.array(data['features']).reshape(1,-1) # Convert the 'features' from the JSON data into a NumPy array and reshape it to correct shape for model.  
    prediction = model.predict(features) # Use model to predict the label for the given features. 
    return jsonify({'prediction': int(prediction[0])}) # Return prediction as JSON response. 

if __name__ == '__main__': 
    app.run(debug=True) # Run the Flask app
