from flask import Flask
app = Flask(__name__)

@app.route('/')
def fa():
    return "ASDASDASD\nfffffffffffffffffffff"

if __name__ == '__main__':
    app.run()