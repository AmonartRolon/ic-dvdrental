from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>\n<h2>classic</h2>"

if __name__ == "__main__":
    app.run()
