from flask import Flask, jsonify, request
import subprocess

from calls import call

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_sentiment():
    return jsonify(call("Example text"))

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    input_text = data.get("text", "")

    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    response_json = call(input_text)
    return jsonify(response_json)


if __name__ == '__main__':
    app.run(debug=True)
