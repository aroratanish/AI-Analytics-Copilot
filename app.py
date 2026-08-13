from flask import Flask, render_template, request
import pandas as pd
import os

from analysis.profile import profile_dataset

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(file_path)
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(file_path)
    else:
        return "Unsupported file type"

    profile = profile_dataset(df)

    return render_template(
        "dashboard.html",
        tables=[df.head().to_html(classes="data")],
        filename=file.filename,
        profile=profile
    )


if __name__ == "__main__":
    app.run(debug=True)