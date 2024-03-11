from flask import Flask,render_template

# Création de l'objet Flask (serveur web)
app = Flask(__name__)

# On définit une route qui renvoie la page index.html
@app.route("/")
def index():
    #return "C'est un serveur web !"
    return render_template("index.html")

# Lancement du serveur
if __name__ == '__main__':
    app.run(ssl_context=('cert.pem','key.pem'))