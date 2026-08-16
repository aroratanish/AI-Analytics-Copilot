from flask import Flask, render_template, request
import pandas as pd
import os

from analysis.profile import profile_dataset
from analysis.cleaning import clean_dataset
from analysis.statistics import get_statistics
from analysis.eda import generate_eda


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    # Get uploaded file
    file = request.files["file"]

    # Create file path
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    # Save file
    file.save(file_path)

    # Read dataset
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file_path)

    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    else:
        return "Unsupported file type"

    # -----------------------------
    # DAY 3: DATASET PROFILING
    # -----------------------------

    profile = profile_dataset(df)

    # -----------------------------
    # DAY 4: DATA CLEANING
    # -----------------------------

    cleaned_df, cleaning_report = clean_dataset(df)

    # -----------------------------
    # DAY 5: STATISTICS
    # -----------------------------

    statistics = get_statistics(cleaned_df)

    # -----------------------------
    # DAY 5: EDA
    # -----------------------------

    eda = generate_eda(cleaned_df)

    # -----------------------------
    # SEND DATA TO DASHBOARD
    # -----------------------------

    return render_template(
        "dashboard.html",

        tables=[
            cleaned_df.head().to_html(
                classes="data"
            )
        ],

        filename=file.filename,

        profile=profile,

        cleaning_report=cleaning_report,

        statistics=statistics,

        eda=eda
    )


if __name__ == "__main__":
    app.run(debug=True)