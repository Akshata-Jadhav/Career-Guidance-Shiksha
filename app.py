
from flask import Flask,render_template,request,jsonify

from chat import get_response

import json



app= Flask(__name__)

@app.route("/", methods=["GET"])
def index_get():
    return  render_template("base.html")

@app.route("/about")
def about():
    return (render_template("about.html"))

@app.route("/students")
def students():
    return (render_template("students.html"))

@app.route("/info")
def info():
    return (render_template("info.html"))

@app.route("/services")
def services():
    return (render_template("services.html"))

@app.route("/Scholarship")
def scholarship():
    return (render_template("Scholarship.html"))


@app.route("/contact")
def contact():
    return (render_template("contact.html"))

@app.route("/team")
def team():
    return (render_template("team.html"))

@app.route("/base")
def home():
    return (render_template("base.html"))
    
#@app.post("/predict")
@app.route("/predict", methods=["POST"])
def predict():
    text=request.get_json().get("message")
    #check if text is valid
    
    response=get_response(text)
    
    message={"answer":response}
    return jsonify(message)


if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0")