from flask import Flask

app = Flask(__name__)

def main_python():
    return "Hello 2!"

# @app.route('/')
# def source():
#     for i in range(100):
#         print(i)
#
#     html = 'Hello World!'
#     return html
