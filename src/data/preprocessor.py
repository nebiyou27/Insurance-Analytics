import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    # Convert TransactionMonth to datetime format if it's not already
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    
    # Handle categorical variables
    categorical_cols = ['Citizenship', 'LegalType', 'Title', 'Bank', 'AccountType', 'MaritalStatus', 'Gender', 
                        'Province', 'MainCrestaZone', 'SubCrestaZone', 'VehicleType', 'make', 'Model', 'bodytype', 
                        'AlarmImmobiliser', 'TrackingDevice', 'NewVehicle', 'WrittenOff', 'Rebuilt', 'Converted', 
                        'TermFrequency', 'CoverCategory', 'CoverType', 'CoverGroup', 'Section', 'Product']
    
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le
    
    # Handle missing values
    df.fillna(df.median(numeric_only=True), inplace=True)
    
    return df, label_encoders

def correlation_analysis(df):
    # Compute correlation matrix
    corr_matrix = df.corr()
    
    # Display the magnitude of correlation
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)
    plt.title('Feature Correlation Heatmap')
    plt.show()
    
    return corr_matrix

# Example usage (assuming df is your DataFrame)
# df, encoders = preprocess_data(df)
# corr_matrix = correlation_analysis(df)
