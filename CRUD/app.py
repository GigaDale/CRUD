from flask import Flask, render_template, request, redirect, url_for
import middlewares.db_middleware as db

app = Flask(__name__)

@app.route("/")
def home():
    lista_tuplas = list(db.get_item())

    lista_dicionarios = []

    for tupla in lista_tuplas:
        dicionario = {"id": tupla[0], "nome": tupla[1], "quantidade": tupla[2]}
        lista_dicionarios.append(dicionario)
    return render_template("html/home.html", lista=lista_dicionarios)

@app.route("/add_item", methods=['POST'])
def add_item():
    name = request.form['new_item']
    quantity = request.form['new_item_quantidade']
    db.insert_item(name.title(), quantity)
    return redirect(url_for('home'))

@app.route("/remove_item", methods=['POST'])
def remove_item():
    name = request.form['remove_item']
    db.delete_item(name.title())
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True) # Tirar debug antes de dar deploy