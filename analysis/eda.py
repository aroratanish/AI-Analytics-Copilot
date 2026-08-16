def generate_eda(df):

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()

    categorical_analysis = {}

    for column in categorical_columns:

        value_counts = df[column].value_counts()

        categorical_analysis[column] = {
            "unique_values": int(df[column].nunique()),
            "most_common": (
                value_counts.index[0]
                if not value_counts.empty
                else None
            ),
            "most_common_count": (
                int(value_counts.iloc[0])
                if not value_counts.empty
                else 0
            )
        }

    return {
        "numerical_columns": numerical_columns,
        "categorical_columns": categorical_columns,
        "categorical_analysis": categorical_analysis
    }