from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    print("in the hello function")
    return 'Hello World!!'

@app.route("/<name>")
def hello_person(name):
    print("*"*80)
    print("in hello_person function")
    print(name)
    return f"Hello {name}!"

@app.route("/users/<username>/<id>")
def show_user_profile(username, id):
    print("*"*80)
    print("in show user profile")
    print(f"username: {username}, id: {id}")
    return f"Hello {username}, {id}!"



if __name__ == '__main__':
    app.run(debug=True)