from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    image = request.files.get("image")

    if image is None or image.filename == "":
        return render_template(
            "index.html",
            result="Please select an image first."
        )

    filename = image.filename

    return render_template(
        "index.html",
        result=f"Image '{filename}' received successfully!"
    )


@app.route("/health")
def health():
    return {
        "project": "VisionGuard",
        "status": "working"
    }


if __name__ == "__main__":
    app.run(debug=True)