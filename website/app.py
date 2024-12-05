from flask import Flask, render_template
import sqlite3
import pandas as pd
import os
import requests
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    db_path = os.path.join(project_dir, 'database', 'database', 'Heart_failure_db.db')
    
    # Print the path for debugging
    print("Attempting to connect to database at:", db_path)
    
    # Verify if the database file exists
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file not found at: {db_path}")
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    variable_descriptions = {
        'age': 'Age of the patient (years)',
        'anaemia': 'Decrease of red blood cells or hemoglobin',
        'creatinine_phosphokinase': 'Level of CPK enzyme in the blood (mcg/L)',
        'diabetes': 'If the patient has diabetes',
        'ejection_fraction': 'Percentage of blood leaving the heart at each contraction',
        'high_blood_pressure': 'If the patient has hypertension',
        'platelets': 'Platelets in the blood (kiloplatelets/mL)',
        'serum_creatinine': 'Level of serum creatinine in the blood (mg/dL)',
        'serum_sodium': 'Level of serum sodium in the blood (mEq/L)',
        'sex': 'Gender of the patient',
        'smoking': 'If the patient smokes',
        'time': 'Follow-up period (days)',
        'DEATH_EVENT': 'If the patient died during the follow-up period'
    }
    return render_template('about.html', variables=variable_descriptions)

@app.route('/data')
def data():
    try:
        conn = get_db_connection()
        df = pd.read_sql_query('SELECT * FROM heart_data LIMIT 100', conn)
        conn.close()
        
        # Rename columns to be more readable
        column_descriptions = {
            'age': 'Age',
            'anaemia': 'Anaemia',
            'creatinine_phosphokinase': 'CPK Level',
            'diabetes': 'Diabetes',
            'ejection_fraction': 'Ejection Fraction (%)',
            'high_blood_pressure': 'High Blood Pressure',
            'platelets': 'Platelets',
            'serum_creatinine': 'Serum Creatinine',
            'serum_sodium': 'Serum Sodium',
            'sex': 'Gender',
            'smoking': 'Smoking',
            'time': 'Follow-up Period (days)',
            'DEATH_EVENT': 'Death Event'
        }
        
        df = df.rename(columns=column_descriptions)
        
        # Format binary columns
        df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})
        df['Anaemia'] = df['Anaemia'].map({1: 'Yes', 0: 'No'})
        df['Diabetes'] = df['Diabetes'].map({1: 'Yes', 0: 'No'})
        df['High Blood Pressure'] = df['High Blood Pressure'].map({1: 'Yes', 0: 'No'})
        df['Smoking'] = df['Smoking'].map({1: 'Yes', 0: 'No'})
        df['Death Event'] = df['Death Event'].map({1: 'Yes', 0: 'No'})
        
        # Format numeric columns
        df['Platelets'] = df['Platelets'].round(0).astype(int)
        df['Serum Creatinine'] = df['Serum Creatinine'].round(2)
        
        return render_template('data.html', tables=[df.to_html(classes='data', header="true", index=False)])
    except Exception as e:
        import traceback
        error_msg = f"An error occurred: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)  # Print to console for debugging
        return error_msg, 500

@app.route('/global-stats')
def global_stats():
    try:
        # Health.gov API endpoint for health indicators
        api_url = "https://health.gov/myhealthfinder/api/v3/topicsearch.json"
        params = {
            'lang': 'en',
            'keyword': 'heart disease'
        }
        
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            resources = data.get('Result', {}).get('Resources', {}).get('Resource', [])
            
            # Process and organize the health information
            health_info = []
            for resource in resources:
                info = {
                    'title': resource.get('Title', ''),
                    'category': resource.get('Categories', ''),
                    'last_update': resource.get('LastUpdate', ''),
                    'url': resource.get('AccessibleVersion', ''),
                    'description': resource.get('Categories', '')
                }
                health_info.append(info)
            
            # Add CDC statistics (as a reliable source)
            cdc_stats = [
                {
                    'country': 'United States',
                    'fact': 'Heart Disease Deaths',
                    'value': '659,041 annually',
                    'source': 'CDC',
                    'year': '2023'
                },
                {
                    'country': 'United States',
                    'fact': 'Cost Burden',
                    'value': '$363 billion annually',
                    'source': 'CDC',
                    'year': '2023'
                },
                {
                    'country': 'United States',
                    'fact': 'Prevalence',
                    'value': '1 in 4 deaths',
                    'source': 'CDC',
                    'year': '2023'
                }
            ]
            
            return render_template('global_stats.html', 
                                 health_info=health_info,
                                 cdc_stats=cdc_stats)
            
        else:
            error_message = f"Error accessing Health.gov API: {response.status_code}"
            return render_template('global_stats.html', 
                                 health_info=None,
                                 message=error_message)
            
    except Exception as e:
        print(f"Exception details: {str(e)}")
        return render_template('global_stats.html', 
                             health_info=None,
                             message=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
