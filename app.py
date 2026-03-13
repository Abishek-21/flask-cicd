from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/status")
def status():
    return jsonify({
        "app": "Flask CI/CD Demo",
        "version": "1.0.0",
        "status": "running",
        "author": "Abishek Budhiraja"
    })

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/api/info")
def info():
    return jsonify({
        "project": "CI/CD Pipeline Demo",
        "tech": ["Python", "Flask", "Docker", "GitHub Actions"],
        "cloud": "AWS EC2"
    })

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
