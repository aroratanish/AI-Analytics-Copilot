import pandas as pd


def get_statistics(df):

    # Select numerical columns
    numerical_df = df.select_dtypes(include="number")

    # Statistical summary
    summary = numerical_df.describe().round(2).to_dict()

    # Correlation matrix
    correlation = numerical_df.corr().round(2).to_dict()

    return {
        "summary": summary,
        "correlation": correlation
    }