

from flask import Flask, redirect, url_for, request, render_template
from zerotha_scanner import main
import time
import sys
import os, signal
app = Flask(__name__)

@app.route('/')
def open_tab():
   return render_template('flask.html')

@app.route('/',methods = ['POST', 'GET'])
def call_zerotha():
   if request.method == "POST":
      if request.form.get("start"):
         print('Started')
         main()
         return 'Execution Finished'
      elif request.form.get("stop"):
         pid = os.getpid()
         print('Stopped')
         os.kill(pid,signal.SIGTERM)
   # elif request.method == 'GET':
   #      return render_template('flask.html')
# @app.route('/<Stop>',methods = ['POST', 'GET'])
# def stop_zerotha(Stop):
#    print('Hello Pranav')
#    return sys.exit()
   # if request.method == 'POST':
   #    if 'Stop' in request.form:
   #       sys.exit()

if __name__ == '__main__':
    app.run()
