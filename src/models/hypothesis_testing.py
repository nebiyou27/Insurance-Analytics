import os

import pandas as pd
import scipy.stats as stats

# Define file path
data_path = (
    "C:\\Users\\neba\\Desktop\\Insurance-Analytics\\Data\\cleaned_insurance_data.csv"
)

# Load data
insurance_data = pd.read_csv(data_path)


# Hypothesis Testing Functions
def anova_test(group_column: str, target_column: str):
    """
    Perform an ANOVA test to check for differences in the target variable across groups.
    """
    groups = [
        group[target_column].dropna()
        for _, group in insurance_data.groupby(group_column)
    ]
    f_stat, p_value = stats.f_oneway(*groups)
    return f_stat, p_value


def t_test(group_column: str, target_column: str, group_a, group_b):
    """
    Perform a t-test for two groups within a categorical column.
    """
    group_a_values = insurance_data[insurance_data[group_column] == group_a][
        target_column
    ].dropna()
    group_b_values = insurance_data[insurance_data[group_column] == group_b][
        target_column
    ].dropna()
    t_stat, p_value = stats.ttest_ind(group_a_values, group_b_values, equal_var=False)
    return t_stat, p_value


# Run Hypothesis Tests
results = {}

# Risk Differences Across Provinces
results["Provinces"] = anova_test("Province", "TotalClaims")

# Risk Differences Across Postal Codes
results["Postal Codes"] = anova_test("PostalCode", "TotalClaims")

# Profit Margin Differences Across Postal Codes
results["Profit Margin - Postal Codes"] = anova_test("PostalCode", "ProfitMargin")

# Risk Differences Between Men and Women
results["Gender"] = t_test("Gender", "TotalClaims", "Male", "Female")

# Print Results
for test, (stat, p) in results.items():
    print(f"{test} Hypothesis Test")
    print(f"Statistic: {stat:.4f}, p-value: {p:.8f}")
    if p < 0.05:
        print(f"Reject Null Hypothesis: Significant difference detected in {test}.\n")
    else:
        print(
            f"Fail to Reject Null Hypothesis: No significant difference detected in {test}.\n"
        )

if __name__ == "__main__":
    print("Hypothesis testing complete.")
