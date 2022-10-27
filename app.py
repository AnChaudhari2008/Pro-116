# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Siddharth" # write your name
    age = "Chaudhari" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage

(I did not learn how to do this and it was not in the class summary)

# define the route to mother webpage

(I did not learn how to do this and it was not in the class summary)

# define the route to friends webpage

(I did not learn how to do this and it was not in the class summary)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
