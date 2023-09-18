from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my youtube channel"

@app.route('/family')
def family():
    return "Welcome to my youtube family!"

if __name__ == '__main__':
    app.run(debug=True)
