from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bharat Citizen Assistant Backend Running 🚀"


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")

    # dummy response for now
    answer = f"You asked: {question}"

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    app.run(debug=True)
