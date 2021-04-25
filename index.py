from flask import Flask, render_template, request, jsonify, url_for
import requests


app = Flask(__name__)


def busca(cep):
	url = f"https://viacep.com.br/ws/{cep}/json"
	req = requests.get(url).json()
	return req


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/search", methods=['POST'])
def search():
    cep = request.form['cep']
    print(len(cep))
    busca_result = busca(cep)
    return render_template("index.html", busca=busca_result)


if __name__ == '__main__':
	app.run(debug=True)
