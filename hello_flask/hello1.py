from flask import Flask, render_template, redirect                        #added render_templates
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", multiplier=5)                        #instead of returning a string, w'll return the result of the render_template method, passing in the same name of our HTML file
    
@app.route("/<name>/<times>")
def hello_person(name, times):
    print("*"*80)
    print("in hello_person function")
    print(name)
    return render_template("name.html", some_name = name, num_times = int(times) )

@app.route("/users/<username>/<id>")
def show_user_profile(username, id):
    print("*"*80)
    print("in show user profile")
    print(f"username: {username}, id: {id}")
    return f"Hello {username}, {id}!"
                                            

if __name__=="__main__":
    app.run(debug=True)