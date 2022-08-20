from flask import jsonify, Flask, render_template, flash, request, redirect, url_for
import json


app = Flask(__name__)
#app = Flask(__name__, template_folder='../../frontend/src')
app.secret_key = "askdlahdajkldhasjdlkhsadjkashd" #provide a secret key


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/contact')
def contact():
    
    return render_template("contact.html")


@app.route('/fullcalendar')
def fullcalendar():
    
    return render_template("fullcalendar.html")
    
@app.route('/log_in')
def log_in():

    return render_template("log-in.html")
    
@app.route('/sign_up')
def sign_up():

    return render_template("sign-up.html")
     
if __name__ == "__main__":
    app.run()