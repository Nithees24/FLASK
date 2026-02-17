from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about.html",methods=["GET","POST"])
def about():
    return render_template("about.html")


@app.route("/contacts.html",methods=["GET","POST"])
def contacts():
    return render_template("contacts.html")


@app.route("/<name>")
def name(name):
    return 'Hi you landed in %s page!' % name

if __name__=="__main__":
    app.run(debug=True)