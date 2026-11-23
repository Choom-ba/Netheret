from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form.get("email","").strip()
        password = request.form.get("password","").strip()

        if not email or not password:
            error = ("Please enter your email and password")

    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)

