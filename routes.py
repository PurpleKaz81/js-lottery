from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/numbers")
def numbers():
    url = "https://apiloterias.com.br/app/resultado?loteria=megasena&token=Cz7y6RJtOJxS3uk"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify(error="Unable to fetch numbers."), 500
    data = response.json()

    if "erro" in data:
        return jsonify(error=data["erro"]), 401

    numbers = data["dezenas"]
    return jsonify(numbers)


if __name__ == "__main__":
    app.run(debug=True)
