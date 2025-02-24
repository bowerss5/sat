from flask import Flask, jsonify, request
from flask_cors import CORS

from calls import call
from prompts import PROMPTS

app = Flask(__name__)
CORS(app)


# @app.route("/api", methods=["GET"])
# def get_sentiment():
#     return jsonify(call("Example text"))


@app.route("/prompts", methods=["GET"])
def get_prompts():
    return jsonify([key for key in PROMPTS.keys() if key != "fix_json"])


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    input_text = data.get("text", "")
    version = data.get("version", "V1_0_0")
    if not input_text:
        return jsonify({"error": "No text provided"}), 400
    if version not in PROMPTS:
        return jsonify({"error": "Prompt not found"})

    response_json = call(input_text, version)
    return jsonify(response_json)


if __name__ == "__main__":
    app.run(debug=True)
