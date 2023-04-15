import pandas as pd



from flask import Flask, render_template,request

# ...
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('mainpage.html')
@app.route('/reference.html')
def reference():
    return render_template('reference.html')
