from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("register.html")
@app.route("/confirm", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        city = request.form.get("city")
        return  render_template("confirm.html",name=name, age=age, city=city)

if __name__ == "__main__":
    app.run(debug=True)