# Heart Disease Data Explorer

A comprehensive web application for exploring and visualizing heart disease patient data and global cardiovascular disease statistics.

## Features

### 1. Patient Data Analysis
- View detailed patient records with clear, readable formatting
- Binary values converted to human-readable text (Yes/No)
- Numeric data properly rounded and formatted
- First 100 records displayed in an organized table

### 2. Health Information Integration
- Real-time health resources from Health.gov API
- Current CDC heart disease statistics and facts
- Interactive health information cards with detailed resources
- Links to authoritative health information sources

### 3. Data Descriptions
- Detailed explanations of all medical variables
- Comprehensive dataset column descriptions
- Medical terminology explained in plain language

## API Integration

### Health.gov API
- **Endpoint**: `https://health.gov/myhealthfinder/api/v3/topicsearch.json`
- **Features**:
  - Real-time heart disease information and resources
  - Latest health recommendations
  - Expert-reviewed content
  - Accessible health resources

### CDC Statistics
- Current heart disease mortality data
- Economic impact statistics
- Disease prevalence information
- Regular updates from CDC's official data

## Project Structure
```
Final Project/
│
├── database/
│   ├── create_db.py              # Database creation script
│   └── database/
│       ├── heart_failure.csv     # Heart disease dataset
│       └── Heart_failure_db.db   # SQLite database
│
├── website/
│   ├── app.py                    # Flask application with API integration
│   └── templates/
│       ├── base.html             # Base template
│       ├── index.html            # Home page
│       ├── about.html            # Variable descriptions
│       ├── data.html             # Patient data display
│       └── global_stats.html     # Health.gov and CDC data display
│
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Technology Stack
- **Backend**: Python 3.12, Flask 3.0.0
- **Database**: SQLite3
- **Data Processing**: Pandas 2.1.3, NumPy 1.26.2
- **Frontend**: HTML5, CSS3, Bootstrap-style components
- **HTTP Client**: Requests 2.31.0
- **APIs**: Health.gov API, CDC Data Integration

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Final\ Project
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
cd database
python create_db.py
cd ..
```

5. Run the application:
```bash
cd website
python app.py
```

6. Access the application at: http://localhost:5001

## Dataset Variables

### Patient Characteristics
- **Age**: Patient's age in years
- **Sex**: Gender (Male/Female)
- **Anaemia**: Decrease of red blood cells (Yes/No)
- **Diabetes**: If the patient has diabetes (Yes/No)
- **High Blood Pressure**: If the patient has hypertension (Yes/No)

### Medical Measurements
- **Ejection Fraction**: Percentage of blood leaving the heart
- **Platelets**: Platelets in blood (kiloplatelets/mL)
- **Serum Creatinine**: Level of serum creatinine in blood (mg/dL)
- **Serum Sodium**: Level of serum sodium in blood (mEq/L)
- **Creatinine Phosphokinase**: CPK enzyme level in blood (mcg/L)

### Follow-up Data
- **Time**: Follow-up period (days)
- **Smoking**: If the patient smokes (Yes/No)
- **Death Event**: If the patient died during follow-up (Yes/No)

## API Data Information
The application integrates two authoritative health data sources:

1. **Health.gov API**
   - Provides current heart disease information
   - Expert-reviewed health resources
   - Latest health recommendations
   - Accessible version links for detailed reading

2. **CDC Statistics**
   - Current mortality rates
   - Economic burden data
   - Prevalence statistics
   - Regular data updates

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Heart failure dataset from Kaggle ('https://raw.githubusercontent.com/akmand/datasets/887a65c5b48f3b259f39a7471e8da812c160470a/heart_failure.csv')
- Health.gov API for current health resources
- CDC for authoritative health statistics
- Built with Flask web framework
