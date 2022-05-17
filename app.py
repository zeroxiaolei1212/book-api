from flask import Flask

app = Flask(__name__)
# 默认的url
# @app.route("/")
# 有接内容的url
@app.route("/hello")
def hello_world():
    # return "<p>Hello, Word!</p>"
    return "<p>Hello, xiaolei!</p>"