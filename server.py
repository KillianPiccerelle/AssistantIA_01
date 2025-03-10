from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Bienvenue sur AssistantIA hébergé sur Vercel!"})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json  # Récupérer la requête JSON
    question = data.get("question", "")
    
    # Logique de réponse de l'assistant (remplace avec ta logique réelle)
    response = f"Je ne sais pas encore répondre à '{question}', mais je m'améliore !"
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
