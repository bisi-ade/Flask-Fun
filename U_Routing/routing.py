from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    print("*"*80)
    print("in index")
    return "Hello World!"

@app.route('/dojo')
def dojo():
    print("*"*80)
    print("in dojo")
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print("*"*80)
    print("in say")
    print(name)
    return f"Hi {name}"

@app.route('/repeat/<multiply>/<text>')
def repeat(multiply, text):
    print("*"*80)
    print("in repeat")
    return (text + "") * int(multiply)

if __name__ == '__main__':
    app.run(debug=True)