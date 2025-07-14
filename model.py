import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
df = pd.read_csv(r'D:\original files for uplaoding\CONTROLLER PROJECTS\cash flow optiomization\Fortune 500 Companies.csv')

# Data preprocessing
df = df[['market_value_mil', 'revenue_mil', 'profit_mil', 'asset_mil', 'employees']].dropna()

# Features and target variable
X = df[['revenue_mil', 'profit_mil', 'asset_mil', 'employees']]
y = df['market_value_mil']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model with the name expected by app.py
with open('linear_model.pkl', 'wb') as f: # Changed 'model.pkl' to 'linear_model.pkl'
    pickle.dump(model, f)

print("Model trained and saved as linear_model.pkl") # Updated print message