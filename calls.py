from prompts import V1_0_0 as PROMPT

import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv("API_KEY")


# Define the API key and endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

textExample = """In this assignment, you will prepare to conduct interviews to gather insights from
individuals who represent your target customers, including end users or anyone
interacting with your product or service. Empathy is essential in design, as it helps you
understand customer needs, frustrations, and aspirations from their perspective. By
actively listening and asking thoughtful, open-ended questions, you’ll uncover valuable
insights to guide your team in creating meaningful, customer-focused solutions that
address real problems and improve their experience.
To ensure a broad and diverse perspective, reach beyond your immediate circle of friends
and roommates when selecting individuals to interview. Engaging with a range of
customers from different backgrounds and experiences will help you uncover unique
insights and avoid biases. This will strengthen your understanding of the problem and
enhance the impact of your solution."""

def call(text):
    # Set up headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    formatted = PROMPT.replace("{PROMPT}", text)

    # Define the data for the request
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": formatted}
        ]
    }

    # Send the request
    response = requests.post(url, headers=headers, json=data)

    # Parse and print the response
    if response.status_code == 200:
        response_data = response.json()
        model_output = response_data['choices'][0]['message']['content']

        try:
            # Ensure model output is a valid JSON string
            parsed_json = json.loads(model_output)
            return parsed_json
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response from model", "raw_output": model_output}

    return {"error": f"API request failed with status {response.status_code}", "details": response.json()}

call(textExample)
