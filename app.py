from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)


#
# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['name']
#       return redirect(url_for('dashboard',name = user))
#    else:
#       user = request.args.get('name')
#       return render_template('login.html')

@app.route('/user')
def login():
    user = request.args.get('amma')
    if user == "amma":
        return "Amma"
    elif user=="nanna":
        return "nanna"
    else:
        return "dada reddy"
if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')