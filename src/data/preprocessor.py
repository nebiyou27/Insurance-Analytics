import pandas as pd

def preprocess_data(df):
    """
    Preprocesses the insurance data.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pandas.DataFrame: The preprocessed DataFrame.
    """

    # 1. Drop Redundant Columns
    df = df.drop(['UnderwrittenCoverID', 'NumberOfVehiclesInFleet'], axis=1)

    # 2. Handle Missing Values (customize based on your strategy)
    # Example: Fill numerical missing values with median, categorical with mode
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    # 3. Convert Data Types
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    df['PostalCode'] = df['PostalCode'].astype(str)

    # 4. Handle Outliers (example: using IQR method for 'TotalPremium')
    Q1 = df['TotalPremium'].quantile(0.25)
    Q3 = df['TotalPremium'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df['TotalPremium'] >= lower_bound) & (df['TotalPremium'] <= upper_bound)]

    # 5. Handle Categorical Variables (example: one-hot encoding)
    df = pd.get_dummies(df, columns=df.select_dtypes(include=['object']).columns, drop_first=True)

    # 6. Clean column names.
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    return df