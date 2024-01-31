from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('login.html')

@app.route('/data/<string:fact>', methods=['POST'])
def data(event):
    fact=json.loads(event)
    print()
    print(f'Name : {fact["Name"]}')
    print(f'PWS: {fact["PWS"]}')

    print()
    return('/')
if __name__ == '__main__':
   app.run()