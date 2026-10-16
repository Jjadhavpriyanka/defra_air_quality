# DEFRA Air Quality Prediction Using Machine Learning

## Project Overview
This project develops a machine learning pipeline to predict hourly PM10 (Particulate matter ≤10μm) concentrations using air quality data obtained from the UK's Department for Environment, Food & Rural Affairs (DEFRA). The study focuses on data collected from the London Bloomsbury monitoring station between 2019 and 2023.

The project combines data acquisition, preprocessing, exploratory data analysis, feature engineering, machine learning, and forecasting to provide accurate short-term PM10 predictions. Two regression models, Linear Regression and Random Forest Regressor, were evaluated and compared to identify the most effective forecasting approach.

## Business Problem
Air pollution poses significant risks to public health and environmental sustainability, PM10 particles can penetrate deep into the respiratory system and are associated with various health conditions.

Accurate forecasting of PM10 levels can support:
1. Environmental monitoring agencies
2. Public health authorities
3. Urban planning initiatives
4. Early warning systems for vulnerable populations
5. Data-driven environmental policy decisions

## Project Objectives
The main objectives of this project were to:
1. Collect air quality data from DEFRA monitoring stations.
2. Clean and preprocess pollutant measurements.
3. Engineer meaningful predictive features.
4. Explore pollutant behaviour over time.
5. Train and compare machine learning models.
6. Forecast future PM10 concentrations.
7. Evaluate predictions accuracy using standard regression metrics
8. Design a scalable architecture suitable for future database integration.

## Dataset
### Data Source
1. Department for Environment, Food & Rural Affairs (DEFRA)
2. Monitoring station: London Bloomsbury (CLL2)
3. Period: 2019-2023
4. Frequency: Hourly

### Target Variable
PM10 (μg/m³)

### Predictor Variables
1. PM2.5
2. NO₂ Nitrogen Dioxide)
3. Ozone (O₃)
4. SO₂ (Sulphur Dioxide)
5. Timestamp information

## Technology
### Programming Language
Python

### Libraries
1. Pandas
2. NumPy
3. Scikit-Learn
4. Matplotlib
5. Seaborn

### Development Tools
1. Jupyter Notebook
2. Visual Studio Code
3. GitHub

### Database Design
SQL schema designed for future implementation. Current project usees Pandas DataFrames for processing and analysis.

## Project Workflow
### Data Collection
Air quality measurements were downloaded from the DEFRA monitoring network and combined into a unifies dataset.

### Data Cleaning
Following preprocessing steps were applied:
1. Removed records lacking PM10 measurements
2. Standardised data and time formats
3. Converted pollutant readings into numerical values
4. Forward-filled short missing sequences
5. Applied interpolation where appropriate
6. Preserved genuine environmental outliers

### Feature Engineering
Several predictive features were generated.

#### Temporal Features
1. Year
2. Month
3. Day of week
4. Hour

#### Lag Features
Previous-hour values for PM2.5, NO₂, and O₃

#### Rolling Statistics
3-hour rolling averages

### EDA
Visual analysis was performed to identify:
1. Seasonal trends
2. Daily pollutant cycles
3. Correlation patterns
4. Missing data issues
5. Pollution peaks and anomalies

### Model Development
Two supervised machine learning algorithms were trained and evaluated. Linear Regression, used as a baseline interpretable forecasting model and Random Forest Regressor, to capture complex non-linear relationships between pollutants and PM10 concentrations.

### Model Evaluation
Models were evaluated using R² score and RMSE

## Future Enhancements
1. Incorporating meteorological variables (temperature, humidity, wind speed)
2. Multi-station forecasting across the UK
3. Real-time data integration pipelines
4. XGBoost implementation
5. Deep learning approaches such as LSTM networks
6. Automated dashboard development using Power BI
7. Full SQL database deployment
8. Cloud-based model serving and API development

## Skills Demonstrated
1. Python
2. Machine learning
3. Data cleaning
4. Data preprocessing
5. EDA
6. Feature Engineering
7. Regression modelling
8. Random Forest algorithms
9. Forecasting
10. Data visualisation
11. SQL database design
12. GitHub
