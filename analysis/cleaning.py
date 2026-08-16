import pandas as pd


def clean_dataset(df):

    df = df.copy()

    cleaning_report = {
        "duplicates_removed": 0,
        "missing_values_before": int(df.isnull().sum().sum()),
        "missing_values_after": 0
    }

    
    duplicates = int(df.duplicated().sum())

    if duplicates > 0:
        df = df.drop_duplicates()

    cleaning_report["duplicates_removed"] = duplicates

    for column in df.columns:

        if df[column].isnull().sum() > 0:

            if pd.api.types.is_numeric_dtype(df[column]):
                df[column] = df[column].fillna(df[column].median())

            else:
                mode = df[column].mode()

                if not mode.empty:
                    df[column] = df[column].fillna(mode[0])

    cleaning_report["missing_values_after"] = int(
        df.isnull().sum().sum()
    )

    return df, cleaning_report