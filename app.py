from flask import Flask
import os, socket

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Hello from EKS!",
        "version": os.environ.get("APP_VERSION", "1.0"),
        "pod": socket.gethostname(),
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
