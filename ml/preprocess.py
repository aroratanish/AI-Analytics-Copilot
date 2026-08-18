import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
def prepare_data(df, target_column):
    data = df.copy()

    if target_column not in data.columns:
        raise ValueError(
            f"Target column '{target_column}' not found."
        )

    X = data.drop(columns=[target_column])
    y = data[target_column]

    numerical_columns = X.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = X.select_dtypes(
        include="object"
    ).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                "passthrough",
                numerical_columns
            ),
            (
                "categorical",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
                categorical_columns
            )
        ]
    )

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Transform features
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor
    )