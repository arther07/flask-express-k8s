from flask import Flask
import os
import requests

app = Flask(__name__)
backend_url = os.environ.get("BACKEND_URL", "http://localhost:3000")

@app.route("/")
def index():
    try:
        response = requests.get(f"{backend_url}/api")
        backend_message = response.text
    except Exception as e:
        backend_message = f"Error contacting backend: {e}"

    return f"""
        <h1>Flask Frontend</h1>
        <p>Message from Express Backend: {backend_message}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
