from flask import Flask, request, render_template ,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("login.html")

@app.route('/data', methods =["POST"])
def data():
   if request.method == "POST":
      info_name = "winnie"
      info_psw = "1234"
      # getting input with name = fname in HTML form
      username = request.form.get("userName")
      # getting input with name = lname in HTML form 
      password = request.form.get("userPassword") 
      if info_name == username and info_psw== password:
         return redirect("/quiz")
      else:
         return redirect("/wrong")
      #print(f"Password: {password}")

@app.route('/quiz')
def run_quiz():
   return render_template("quiz.html")

@app.route('/wrong')
def wrong():
   return render_template("wrong.html")

 
if __name__=='__main__':
   app.run(debug=True)
