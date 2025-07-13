from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pocetna():
    return render_template("index.html")

@app.route("/usluge")
def usluge():
    return render_template("usluge.html")

@app.route("/cenovnik")
def cenovnik():
    return render_template("cenovnik.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/galerija")
def galerija():
    return render_template("galerija.html")


if __name__ == "__main__":
    app.run(debug=True)
