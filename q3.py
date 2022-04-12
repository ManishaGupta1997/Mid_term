from flask import Flask, request   #calling required libraries
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route("/my_name/<name>")   #after slash we have to write my_name followed by our name to get the output
def print_name(name):   #creating a function 
    return f"Welcome {name}"

if __name__=="__main__":   #done done name
    app.run(host='0.0.0.0', port=8080)  #changing port number 
