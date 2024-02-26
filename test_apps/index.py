from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/info/<string:fact>', methods=['POST'])
def info(fact):
    fact=json.loads(fact)
    print()
    print(f'Name : {fact["Name"]}')
    print(f'Email : {fact["Email"]}')
    print(f'Amount : {fact["Amount"]}')
    print()
    return('/')

if __name__ == '__main__':
   app.run()