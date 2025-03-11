import pandas as pd
import pytest

from src.data.preprocessor import preprocess_data


@pytest.fixture
def sample_data():
    data = {
        "UnderwrittenCoverID": [103],
        "NumberOfVehiclesInFleet": [2],
        "TransactionMonth": ["2023-03-01"],
        "TotalPremium": [12000],
        "CapitalOutstanding": [30000.0],
        "PostalCode": [9101],
        "Category": [None],
    }
    return pd.DataFrame(data)


def test_preprocess_data(sample_data):
    """Test preprocess_data() function for correct transformations."""
    processed_df = preprocess_data(sample_data)

    # Ensure redundant columns are removed
    assert "UnderwrittenCoverID" not in processed_df.columns
    assert "NumberOfVehiclesInFleet" not in processed_df.columns

    # Ensure missing numerical values are imputed
    assert processed_df["capitaloutstanding"].isna().sum() == 0

    # Ensure categorical columns are one hot encoded.
    assert "postalcode_9101" in processed_df.columns

    # Ensure column names are lower case with underscores.
    assert "totalpremium" in processed_df.columns
