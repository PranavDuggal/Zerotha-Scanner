# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, url_for, request
from zerotha_scanner import main

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/',methods = ['POST', 'GET'])
def call_zerotha():
   if request.method == 'POST':
    #   user = request.form['nm']
      return main()
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


if __name__ == '__main__':
    app.run()
    