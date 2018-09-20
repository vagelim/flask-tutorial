#!/usr/bin/env python

from flask import Flask
import requests


app = Flask(__name__)

@app.route("/")
def hello():
    # Read from database:
    r = requests.get('user:super_secret_pass@remote-resource.com/response.html')
    return r.text

# Runs on port 5000 by default
if __name__ == "__main__":
    app.run()
