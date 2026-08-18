from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier
)
from ml.preprocess import prepare_data

def detect_problem_type(y):
    """
    Detect whether the target is suitable
    for classification or regression.
    """

    if y.dtype == "object":
        return "classification"

    if y.nunique() <= 10:
        return "classification"

    return "regression"

def train_model(df, target_column):

    # Prepare data
    (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor
    ) = prepare_data(
        df,
        target_column
    )

    # Determine ML problem type
    problem_type = detect_problem_type(
        df[target_column]
    )

    # Select model
    if problem_type == "regression":

        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

    else:

        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
    # Train model
    model.fit(
        X_train,
        y_train
    )
    return {
        "model": model,
        "preprocessor": preprocessor,
        "X_test": X_test,
        "y_test": y_test,
        "problem_type": problem_type
    }

def predict_value(
    model,
    preprocessor,
    input_data
):

    # Convert input into DataFrame
    input_df = input_data.copy()

    # Transform input
    transformed_data = preprocessor.transform(
        input_df
    )

    # Predict
    prediction = model.predict(
        transformed_data
    )

    return prediction