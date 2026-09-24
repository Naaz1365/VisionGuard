from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {
        "project": "VisionGuard",
        "status": "working"
    }

if __name__ == "__main__":
    app.run(debug=True)