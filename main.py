from flask import Flask, render_template, request, jsonify
from chatbot import responder

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/responder", methods=["POST"])
def chat_response():
    user_input = request.json["mensagem"]
    resposta = responder(user_input)
    return jsonify({"resposta": resposta})

print(__name__)

if __name__ == "__main__":
    app.run(debug=True)