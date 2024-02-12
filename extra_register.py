from flask import Flask, request, render_template ,redirect,url_for
import re
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("login.html")

infos = [{"name": "winnie","pws":"1234","email":"wut@gmail.com"},{"name": "logan","pws":"1111","email":"logan5@gmail.com"}]
@app.route('/data', methods =["POST"])
def data():
   if request.method == "POST":
      username = request.form.get("userName")
      password = request.form.get("userPassword") 
      for info in infos:
         if (username in info["name"]) and password==info["pws"]:
            return redirect("/quiz")
         else:
            return redirect("/wrong")
      
@app.route('/quizdata', methods =["POST"])
def quiz():
   score = 0
   if request.method == "POST":
      list1 = ["oldest","member","youngest","year","debut"]
      for i in list1:
         num= request.form.get(i)
         if num =="1":
            score+=1
      if 3 <= score <= len(list1):
         return render_template("score.html",txt = f" Your score is {score}🤩✨")
      if  score < 3:
         return render_template("score.html",txt = f" Your score is {score}😢🎈")


@app.route('/signup-data',methods=["POST"])
def sdata():
   if request.method =="POST":
      email = request.form.get("email")
      password = request.form.get("userPassword")
      cpassword = request.form.get("cPassword")
      if re.match(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$ ",email):
         if password == cpassword:
            return redirect('/quiz')
         else:
            return render_template("wrong.html",error="Password don't match")
      else:
            return render_template("wrong.html",error="Invalid email")


@app.route('/quiz')
def run_quiz():
   return render_template("quiz.html")

@app.route('/register')
def register():
   return render_template("signup.html")


 
if __name__=='__main__':
   app.run(debug=True)
