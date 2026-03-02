from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome Shivaram 😎🔥</h1><p>This is my first Python web page!</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

