import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_cubiccapacity_vs_kilowatts(df):
    """
    Scatter plot of cubiccapacity vs. kilowatts with marginal distributions.
    """
    sns.jointplot(
        x="cubiccapacity",
        y="kilowatts",
        data=df,
        kind="scatter",
        marginal_kws=dict(bins=50, fill=True),
    )
    plt.suptitle("Relationship between Cubic Capacity and Kilowatts", y=1.02)
    plt.show()


def plot_total_premium_distribution(df):
    """
    Violin plot of TotalPremium with overlaid box plot.
    """
    plt.figure(figsize=(10, 6))
    sns.violinplot(y="TotalPremium", data=df, inner=None, color="skyblue")
    sns.boxplot(y="TotalPremium", data=df, width=0.1, color="gray")
    plt.title("Distribution of Total Premium with Outliers")
    plt.show()


def plot_total_claims_monthly_trends(df):
    """
    Line plot of monthly trends in TotalClaims.
    """
    monthly_claims = df.groupby(df["TransactionMonth"].dt.to_period("M"))[
        "TotalClaims"
    ].mean()
    plt.figure(figsize=(12, 6))
    monthly_claims.plot(marker="o", linestyle="-")
    plt.title("Monthly Trends in Total Claims")
    plt.xlabel("Month")
    plt.ylabel("Average Total Claims")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Replace with your actual file path
    file_path = r"C:\Users\neba\Documents\week-3\MachineLearningRating_v3.csv"

    # Load the data
    df = pd.read_csv(file_path, low_memory=False)

    # Convert CapitalOutstanding to numeric
    df["CapitalOutstanding"] = pd.to_numeric(df.iloc[:, 32], errors="coerce")

    # Convert CrossBorder to boolean
    df["CrossBorder"] = df.iloc[:, 37].fillna("No") == "No"

    # Remove CrossBorder
    df = df.drop("CrossBorder", axis=1)

    # Impute NaN values with the median (corrected)
    median_capital = df["CapitalOutstanding"].median()
    df["CapitalOutstanding"] = df["CapitalOutstanding"].fillna(median_capital)

    # Convert TransactionMonth to datetime
    df["TransactionMonth"] = pd.to_datetime(df["TransactionMonth"])

    # Plot the graphs.
    plot_cubiccapacity_vs_kilowatts(df)
    plot_total_premium_distribution(df)
    plot_total_claims_monthly_trends(df)
