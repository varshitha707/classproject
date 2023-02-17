# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "VARSHITHA.G.P" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "GOPINATHAN.P"
    age = "34"

    return render_template('index.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "PREETHEE.K"
    age = "33"

    return render_template('index.html' , name = name , age = age)


# define the route to sibling webpage
@app.route("/brother")
def brother():

    name = "TAMAN KRISH.G.P"
    age = "9"

    return render_template('index.html' , name = name , age = age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
