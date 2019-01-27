from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_python():
    control = 0
    for i in range(100):
        print_hello()
        control += i

    return control

def print_hello():
    print("Hello")
    return "Hello"

# @app.route('/')
# def source():
#     for i in range(100):
#         print(i)
#
#     html = 'Hello World!'
#     return html
