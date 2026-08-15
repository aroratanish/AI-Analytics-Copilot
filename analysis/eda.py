import pandas as pd


def perform_eda(df):
    """
    Perform basic exploratory data analysis
    on the uploaded dataset.
    """

    # -----------------------------------------
    # 1. Select numerical columns
    # -----------------------------------------

    numerical_df = df.select_dtypes(include="number")


    # -----------------------------------------
    # 2. Select categorical columns
    # -----------------------------------------

    categorical_df = df.select_dtypes(
        include=["object", "category", "bool"]
    )


    # -----------------------------------------
    # 3. Descriptive statistics
    # -----------------------------------------

    numerical_summary = (
        numerical_df
        .describe()
        .round(2)
        .to_dict()
    )


    # -----------------------------------------
    # 4. Categorical summaries
    # -----------------------------------------

    categorical_summary = {}

    for column in categorical_df.columns:

        categorical_summary[column] = {
            "unique_values": int(
                categorical_df[column].nunique()
            ),
            "most_common": (
                categorical_df[column]
                .mode()
                .iloc[0]
                if not categorical_df[column].mode().empty
                else None
            )
        }


    # -----------------------------------------
    # 5. Correlation matrix
    # -----------------------------------------

    correlation_matrix = (
        numerical_df
        .corr()
        .round(2)
        .fillna(0)
        .to_dict()
    )


    # -----------------------------------------
    # Return all EDA results
    # -----------------------------------------

    return {
        "numerical_summary": numerical_summary,
        "categorical_summary": categorical_summary,
        "correlation_matrix": correlation_matrix
    }
