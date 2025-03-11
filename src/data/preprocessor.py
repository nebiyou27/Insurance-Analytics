import pandas as pd


def preprocess_data(df):
    """
    Preprocesses the insurance data.
    """
    # Drop unnecessary columns
    df = df.drop(["UnderwrittenCoverID", "NumberOfVehiclesInFleet"], axis=1)

    # Fill missing numerical values with median
    for col in df.select_dtypes(include=["number"]).columns:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing categorical values with mode (most frequent value)
    for col in df.select_dtypes(include=["object"]).columns:
        mode_result = df[col].mode()
        if not mode_result.empty:
            df[col] = df[col].fillna(mode_result.iloc[0])

    # Convert 'TransactionMonth' to datetime
    df["TransactionMonth"] = pd.to_datetime(df["TransactionMonth"])

    # Explicitly convert PostalCode to string and check
    df["PostalCode"] = df["PostalCode"].astype(str)
    print(f"PostalCode dtype after conversion: {df['PostalCode'].dtype}")
    print(
        f"PostalCode values: {df['PostalCode'].unique()}"
    )  # Print unique PostalCode values

    # Handle outliers in 'TotalPremium' using IQR
    Q1 = df["TotalPremium"].quantile(0.25)
    Q3 = df["TotalPremium"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df["TotalPremium"] >= lower_bound) & (df["TotalPremium"] <= upper_bound)]

    # Get categorical columns for encoding
    categorical_cols = df.select_dtypes(include=["object"]).columns
    print(f"Categorical cols: {categorical_cols}")

    # Handle the 'PostalCode' and 'Category' columns using one-hot encoding
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=False)

    # Ensure column names are lower case with underscores
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    return df
