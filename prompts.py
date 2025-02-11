V1_0_0 = """Prompt:

Analyze the sentiment of the given text and return confidence scores for the following emotions:

Joy
Sadness
Anger
Fear
Surprise
Disgust
Neutral
The response should be in JSON format with each emotion as a key and its confidence score as a decimal between 0 and 1 (inclusive), representing the likelihood that the text expresses that emotion. The sum of all confidence scores does not need to equal 1.

Example Input:
"I can't believe this happened! This is amazing!"

Example Output:

json
Copy
Edit
{
  "Joy": 0.85,
  "Sadness": 0.02,
  "Anger": 0.01,
  "Fear": 0.03,
  "Surprise": 0.75,
  "Disgust": 0.01,
  "Neutral": 0.05
}
Ensure consistency in formatting and avoid including explanations—only return the JSON object.

Text: "{PROMPT}"
"""
