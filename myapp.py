from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def greet():
    return render_template("original.html")

@app.route("/")
def result(mark):
    if 101> mark >=80:
        if mark==100:
            return f"You got grade (A) with full mark!!. Great job."
        else:
            return f"You got grade (A) with the mark of {mark}"
    elif 80 > mark >=60:
        return f"You got grade (B) with the mark of {mark}"
    elif 60> mark  >=40:
        return f"You got grade (C) with the mark of {mark}"
    elif 40> mark >=0:
        if mark ==0:
            return f"ZERO!! Really? Try much harder next time. You got D"
        elif mark == 39:
            return f"Failed with just one mark. Gook luck next time. You got D"
        else:
            return f"You got grade (D) with the mark of {mark}"
    else:
        return f"This isn't funny"

if __name__=="__main__":
    app.run()