# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return "Hello, world!"
#
# app.run()

import pandas as pd

data = {"a": [1, 2, 3, 4], "b": [1, 2, 3, 4]}

df = pd.DataFrame(data)

df.to_csv("data.csv")
