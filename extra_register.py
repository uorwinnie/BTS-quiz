from flask import Flask, request, render_template ,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("login.html")

@app.route('/data', methods =["POST"])
def data():
   if request.method == "POST":
      info = {"winnie":"1234","logan":"0000","dardar":"1111","tina":"9999","ollie":"1919"}
      username = request.form.get("userName")
      password = request.form.get("userPassword") 
      if (username in info.keys()) and password==info[username]:
         return redirect("/quiz")
      else:
         return redirect("/wrong")

@app.route('/quiz')
def run_quiz():
   return render_template("quiz.html")

@app.route('/wrong')
def wrong():
   return render_template("wrong.html")

@app.route('/<string:signup>/')
def signup():
   return render_template("signup.html")
 
if __name__=='__main__':
   app.run(debug=True)
