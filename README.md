# Cash-Flow-Optimization

# Fortune 500 Company Market Value Prediction and Analysis Application

This project provides a web-based application to predict the market value of Fortune 500 companies based on their revenue, profit, assets, and number of employees. It uses a Linear Regression model for predictions and offers functionalities for data exploration (EDA) and company comparisons through an interactive web interface.

## Features

* **Market Value Prediction**: Predicts a company's market value in millions based on user-provided financial metrics and employee count.
* **Linear Regression Model**: Utilizes a Linear Regression model for robust and interpretable predictions.
* **Model Persistence**: The application automatically trains and saves the prediction model (`linear_model.pkl`) if it doesn't already exist, ensuring quick startup on subsequent runs.
* **Exploratory Data Analysis (EDA)**: Generates a comprehensive EDA summary, including descriptive statistics, missing values, and basic insights about the dataset, saved to `eda_results.txt`.
* **Web Interface (Flask)**:
    * Provides a simple homepage for inputting prediction parameters.
    * Displays prediction results along with comparative predictions for randomly selected companies.
    * Includes a separate section for viewing charts and comparing specific companies.
* **Company Comparison Visualizations**: Allows users to compare the market values of two chosen companies through an auto-generated bar plot.
* **Modular Design**: Separates the core model training logic (in `model.py`) from the web application logic (in `app.py`).

## Requirements

Ensure you have the following Python libraries installed:

* Python 3.x
* Flask
* pandas
* scikit-learn (for `LinearRegression`)
* matplotlib
* seaborn
* joblib (for saving/loading models, although `pickle` is used in the provided code)
* pickle (for saving/loading models)
* `os` (standard library, for path operations)
* `random` (standard library, for random company selection)

## Installation

1.  **Set up Project Directory:**
    Organize your project files with the following structure:
    ```
    /fortune500-predictor
    ├── app.py
    ├── model.py                # Script for standalone model training (optional to run separately)
    ├── requirements.txt        # You will create this file
    ├── data/
    │   └── Fortune 500 Companies.csv # Your input dataset
    ├── static/                 # Directory for static files like generated charts
    │   └── company_comparison.png
    └── templates/
        ├── index.html          # Homepage/prediction input form
        ├── result.html         # Displays prediction results
        ├── charts.html         # Page to initiate company comparison
        └── compare.html        # Displays company comparison chart
    ```
    *Ensure `app.py` and `model.py` are in the project root. Create the `data`, `static`, and `templates` folders as shown.*

2.  **Update Data Paths in `app.py`:**
    **Crucially, you need to update the hardcoded file path in `app.py`** to point to the correct location of your data file within the `data/` directory.

    * In `app.py`, change the line:
        ```python
        df = pd.read_csv('C:/Users/AS5560/Downloads/Controller Projects/cash flow optiomization/Fortune 500 Companies.csv')
        ```
        to:
        ```python
        df = pd.read_csv('data/Fortune 500 Companies.csv')
        ```

3.  **Set up a Virtual Environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```

4.  **Create `requirements.txt`:**
    In your project root, create a file named `requirements.txt` and add the following content:
    ```
    Flask
    pandas
    scikit-learn
    matplotlib
    seaborn
    ```
    *Note: `pickle` and standard libraries like `os`, `random` are built-in and don't need to be listed.*

5.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Run the Flask App:**
    * The `app.py` script will automatically train and save the `linear_model.pkl` in your project's root directory if it doesn't find an existing model. It will also generate `eda_results.txt` and save comparison charts to the `static/` folder.
    * To run the application:
        ```bash
        python app.py
        ```
    * *(Optional - Using `model.py` for standalone training):* If you prefer to train the model separately before running `app.py`, you can run `model.py`. Ensure `model.py` is modified to output `linear_model.pkl` instead of `model.pkl` to be compatible with `app.py`, and place `Fortune 500 Companies 1.csv` in the same directory as `model.py` or adjust its path.
        ```python
        # In model.py, change 'model.pkl' to 'linear_model.pkl'
        with open('linear_model.pkl', 'wb') as f:
            pickle.dump(model, f)
        ```
        Then run:
        ```bash
        python model.py
        ```

## Project Structure

/fortune500-predictor
│── app.py                # Main Flask web application for prediction, EDA, and comparisons
│── model.py              # Standalone script for training and saving the Linear Regression model
│── requirements.txt      # Lists all project dependencies
│── linear_model.pkl      # Saved trained Linear Regression model (generated by app.py or model.py)
│── eda_results.txt       # Generated text file with EDA summary (generated by app.py)
│
├── data/                 # Directory for input data
│   └── Fortune 500 Companies.csv # The raw Fortune 500 companies dataset
│
├── static/               # Directory for static web assets like generated charts
│   └── company_comparison.png # Generated bar chart for company comparison
│
└── templates/            # HTML templates for the Flask web interface
├── index.html        # Homepage and form for market value prediction input
├── result.html       # Displays prediction results
├── charts.html       # Page to access company comparison functionality
└── compare.html      # Displays the company comparison chart


## Usage

1.  **Access the Application:**
    Open your web browser and navigate to `http://127.0.0.1:5000` (or the address displayed in your console after running `app.py`).

2.  **Predict Market Value:**
    * On the homepage, you will find a form to input:
        * `revenue_mil` (Revenue in millions)
        * `profit_mil` (Profit in millions)
        * `asset_mil` (Assets in millions)
        * `employees` (Number of employees)
    * Enter the values and submit the form.
    * The application will display the predicted market value for your input, along with predictions for two randomly selected companies from the dataset for comparison.

3.  **View Charts and Compare Companies:**
    * Navigate to `http://127.0.0.1:5000/charts`.
    * On this page, you can enter the names of two Fortune 500 companies you wish to compare.
    * Submit the form to generate a bar chart comparing their market values, which will be displayed on the `compare.html` page.
