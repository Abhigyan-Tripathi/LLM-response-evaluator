from flask import Flask, request, jsonify
from inference import judge
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits= ["10 per minute"],
)
CORS(app)

@app.route("/judge", methods=["POST"])
def judge_responses():
    data = request.json

    prompt = data["prompt"]
    respA = data["response_a"]
    respB = data["response_b"]

    result = judge.score(prompt, respA, respB)
    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return {"message": "LLM Judge API running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
