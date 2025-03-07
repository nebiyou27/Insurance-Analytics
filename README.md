# Insurance Analytics & Risk Modeling Project

## Business Understanding

AlphaCare Insurance Solutions (ACIS) aims to optimize their car insurance marketing strategy and identify low-risk market segments in South Africa. As a marketing analytics engineer, my task is to analyze historical insurance claim data to discover patterns that can inform premium pricing and marketing decisions.

The project focuses on:
1. Finding demographic and geographic segments with lower risk profiles
2. Identifying statistically significant differences in risk across various customer segments
3. Building predictive models to optimize premium pricing based on risk factors
4. Providing actionable insights to help ACIS attract new customers through targeted marketing

## Project Tasks

### 1. Data Exploration & Preprocessing
- **Data Understanding**: Analyze the structure and content of insurance claims data from Feb 2014 to Aug 2015
- **Data Cleaning**: Handle missing values, outliers, and inconsistencies
- **Feature Engineering**: Create derived features relevant to risk assessment
- **Exploratory Data Analysis**: Visualize distributions, correlations, and patterns in the data

### 2. Data Version Control (DVC)
- **DVC Setup**: Initialize DVC for tracking datasets and model artifacts
- **Pipeline Creation**: Develop reproducible data processing pipelines
- **Version Management**: Implement proper versioning for datasets and models

### 3. A/B Hypothesis Testing
- **Test Design**: Formulate statistical tests for the following null hypotheses:
  - There are no risk differences across provinces
  - There are no risk differences between zipcodes
  - There are no significant margin (profit) differences between zip codes
  - There are no significant risk differences between women and men
- **Statistical Analysis**: Apply appropriate statistical tests (t-tests, chi-squared tests, ANOVA)
- **Multiple Testing Correction**: Account for multiple comparisons using methods like Bonferroni
- **Visualization**: Create clear visualizations of test results

### 4. Statistical Modeling
- **Linear Regression**: Build zipcode-specific models to predict total claims
- **Machine Learning Models**: Develop models to predict optimal premium values considering:
  - Vehicle features (make, model, year, etc.)
  - Owner demographics (gender, age, etc.)
  - Location data (province, zipcode)
  - Additional relevant features
- **Feature Importance**: Analyze and visualize the most influential features
- **Model Evaluation**: Assess models using appropriate metrics (RMSE, R², MAE)
- **Model Interpretability**: Implement SHAP analysis for transparent feature importance

### 5. Code Architecture & MLOps
- **Modular Design**: Refactor code into a well-structured Python package
- **Testing**: Implement comprehensive unit and integration tests
- **CI/CD**: Set up GitHub Actions for continuous integration
- **Documentation**: Create thorough documentation for all components
- **Model Tracking**: Use MLflow for experiment tracking and model versioning

### 6. Data Visualization & Reporting
- **Business Insights**: Extract actionable insights from analytical results
- **Interactive Dashboard**: Develop a Streamlit dashboard for exploring results
- **Final Report**: Compile a comprehensive report with findings and recommendations

## Data Description

The dataset contains insurance policy information from February 2014 to August 2015, including:

- **Policy Information**: CoverID, PolicyID, TransactionMonth
- **Client Demographics**: Gender, MaritalStatus, Citizenship, etc.
- **Location Data**: Province, PostalCode, CrestaZones
- **Vehicle Details**: Make, Model, RegistrationYear, VehicleType, etc.
- **Plan Information**: SumInsured, TermFrequency, CalculatedPremiumPerTerm, etc.
- **Financial Metrics**: TotalPremium, TotalClaims

## Extension Plan

The original project implementation was incomplete, with basic EDA and partial DVC implementation. I will extend it by:

1. **Properly Implementing All Required Components**:
   - Complete the DVC setup with full data pipeline
   - Implement all required hypothesis tests
   - Develop and evaluate multiple predictive models
   - Create comprehensive visualizations

2. **Adding Advanced Features**:
   - Implement ensemble modeling techniques
   - Add hyperparameter optimization
   - Create interactive dashboards for result exploration
   - Develop model interpretability visualizations

3. **Enhancing Code Quality**:
   - Refactor code into a proper Python package
   - Implement comprehensive testing
   - Add proper documentation
   - Set up CI/CD pipeline

4. **Improving Business Value**:
   - Connect statistical findings to actionable business recommendations
   - Develop ROI analysis for implementing recommendations
   - Create targeting strategies based on model insights

## Project Structure

```
insurance-analytics/
├── src/                # Source code package
│   ├── data/           # Data loading and preprocessing modules
│   ├── visualization/  # Data visualization utilities
│   ├── models/         # Statistical and ML models
│   └── utils/          # Helper functions and utilities
├── notebooks/          # Jupyter notebooks for analysis
├── tests/              # Unit and integration tests
├── data/               # Data directory (managed by DVC)
├── models/             # Saved model artifacts
├── reports/            # Generated reports and visualizations
└── docs/               # Documentation
```

## Libraries and Tools

- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Statistical Analysis**: scipy, statsmodels
- **Machine Learning**: scikit-learn, XGBoost
- **Model Interpretability**: SHAP
- **Data Version Control**: DVC
- **Model Tracking**: MLflow
- **Testing**: pytest
- **CI/CD**: GitHub Actions
- **Dashboard**: Streamlit
- **API**: FastAPI

## Expected Outcomes

- Statistically validated insights about risk differences across customer segments
- Predictive models for optimizing premium pricing
- Actionable recommendations for marketing strategy
- Interactive dashboard for exploring results
- Well-documented, maintainable, and reproducible codebase

This project will provide ACIS with data-driven insights to optimize their marketing strategy and premium pricing, ultimately helping them attract new customers in low-risk segments.
