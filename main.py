#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Runs on port 5000 by default
if __name__ == "__main__":
    app.run()
