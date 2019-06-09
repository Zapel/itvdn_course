from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello world!"

# app.run(host="0.0.0.0")
# app.run()
app.run(debug=True, port=5001)

