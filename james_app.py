from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to james_app.py! Flask is running smoothly, James."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
