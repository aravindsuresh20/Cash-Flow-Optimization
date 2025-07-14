import pandas as pd
from flask import Flask, request, render_template
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import random
import os

# Load and preprocess data

df = pd.read_csv(r'D:\original files for uplaoding\CONTROLLER PROJECTS\cash flow optiomization\Fortune 500 Companies.csv')

df = df[['name', 'market_value_mil', 'revenue_mil', 'profit_mil', 'asset_mil', 'employees']].dropna()

# Train or load model
model_path = 'linear_model.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    X = df[['revenue_mil', 'profit_mil', 'asset_mil', 'employees']]
    y = df['market_value_mil']
    model = LinearRegression()
    model.fit(X, y)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

# Generate EDA results and save to Notepad file
eda_results = []
eda_results.append("Summary Statistics:\n")
eda_results.append(str(df.describe(include='all')))
eda_results.append("\n\nMissing Values:\n")
eda_results.append(str(df.isnull().sum()))
eda_results.append("\n\nBasic Insights:\n")
eda_results.append(f"Total number of rows (companies): {df.shape[0]}")
eda_results.append(f"\nTotal number of columns: {df.shape[1]}")
eda_results.append(f"\nColumn names: {', '.join(df.columns)}\n")

with open('eda_results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(eda_results))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        revenue = float(request.form['revenue_mil'])
        profit = float(request.form['profit_mil'])
        assets = float(request.form['asset_mil'])
        employees = int(request.form['employees'])

        input_df = pd.DataFrame([[revenue, profit, assets, employees]],
                                columns=['revenue_mil', 'profit_mil', 'asset_mil', 'employees'])
        prediction = model.predict(input_df)[0]

        company_names = df['name'].sample(2).tolist()
        company1_data = df[df['name'] == company_names[0]].iloc[0]
        company2_data = df[df['name'] == company_names[1]].iloc[0]

        company1_input = pd.DataFrame([[company1_data['revenue_mil'], company1_data['profit_mil'],
                                        company1_data['asset_mil'], company1_data['employees']]],
                                      columns=['revenue_mil', 'profit_mil', 'asset_mil', 'employees'])
        company2_input = pd.DataFrame([[company2_data['revenue_mil'], company2_data['profit_mil'],
                                        company2_data['asset_mil'], company2_data['employees']]],
                                      columns=['revenue_mil', 'profit_mil', 'asset_mil', 'employees'])

        company1_prediction = model.predict(company1_input)[0]
        company2_prediction = model.predict(company2_input)[0]

        return render_template('result.html',
                               prediction=prediction,
                               company1_name=company_names[0],
                               company2_name=company_names[1],
                               company1_prediction=company1_prediction,
                               company2_prediction=company2_prediction)
    except Exception as e:
        return f"Error during prediction: {e}"

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/compare', methods=['POST'])
def compare():
    company1 = request.form['company1']
    company2 = request.form['company2']

    data1 = df[df['name'].str.contains(company1, case=False)]
    data2 = df[df['name'].str.contains(company2, case=False)]

    if data1.empty or data2.empty:
        return "One or both companies not found."

    combined = pd.concat([data1, data2])
    plt.figure(figsize=(10, 6))
    sns.barplot(data=combined, x='name', y='market_value_mil')
    plt.title(f'{company1} vs {company2} Market Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/company_comparison.png')
    plt.close()

    return render_template('compare.html', company1=company1, company2=company2)

if __name__ == '__main__':
    app.run(debug=True)
