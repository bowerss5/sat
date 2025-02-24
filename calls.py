import json
import os

import requests
from dotenv import load_dotenv

from prompts import PROMPTS

load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("API_URL", "https://api.groq.com/openai/v1/chat/completions")
model = os.getenv("MODEL_NAME", "llama3-8b-8192")


def call(text, prompt="V1_0_0"):
    print("Running:", prompt)
    # Set up headers
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    formatted = PROMPTS[prompt].replace("{PROMPT}", text)

    # Define the data for the request
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": formatted},
            {"role": "assistant", "content":"```json"}
        ],
        "stop":"```"
    }

    # Send the request
    response = requests.post(url, headers=headers, json=data)

    # Parse and print the response
    if response.status_code == 200:
        response_data = response.json()
        model_output = response_data["choices"][0]["message"]["content"]

        try:
            # Ensure model output is a valid JSON string
            parsed_json = json.loads(model_output)
            return parsed_json
        except json.JSONDecodeError:
            if prompt == "fix_json":
                return {
                    "error": "Invalid JSON response from model",
                    "raw_output": model_output,
                }
            print("Attempting to fix json object")
            return call(model_output, "fix_json")

    return {
        "error": f"API request failed with status {response.status_code}",
        "details": response.json(),
    }
