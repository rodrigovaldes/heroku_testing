from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_python():
    control = 0
    for i in range(100):
        control += i

    return control


# @app.route('/')
# def source():
#     for i in range(100):
#         print(i)
#
#     html = 'Hello World!'
#     return html
