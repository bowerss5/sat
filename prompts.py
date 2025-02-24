#v101- default prompt
#v102 - scriptwriters prompt
#v102- detailed emotion explanation
#v103 - product feedback explanation

PROMPTS = {
    "V1_0_0": """Prompt: Analyze the sentiment of the given text and return confidence scores for the following emotions:

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
""",
"fix_json": """
You are an expert at fixing corrupted or malformed JSON objects. The input will be a JSON string that may contain syntax errors, missing brackets, extra commas, incorrect data types, or other structural issues.

Your task is to return only a valid JSON object, properly formatted and corrected. Do not include explanations, comments, or extra text—just return the fixed JSON.

Correction Rules:
If the json object is missing a closing brace please add it.
Fix syntax errors: Ensure proper use of brackets {}, colons :, and commas ,.
Correct data types: Convert values to appropriate types (e.g., numbers, strings, booleans, arrays, or objects).
Repair broken keys: If keys have typos, extra characters, or incorrect casing, attempt to infer the correct key name.
Remove extraneous characters: Delete unexpected or invalid characters that prevent parsing.
Ensure structural integrity: Nest objects and arrays correctly and maintain consistency.
Preserve intended meaning: Retain as much of the original data as possible while making it valid.
If the json object is missing a closing brace please add it.
Input JSON (Malformed):
json
Copy
Edit
{PROMPT}
Output JSON (Fixed):
(Return only the corrected JSON object, with no extra text.)
    """,
    "V1_0_1": """Prompt: Analyze the sentiment of the given text and return confidence scores for the following emotions, and provide helpful information for people with disabilities to understand the emotions displayed in the text.

Joy
Sadness
Anger
Fear
Surprise
Disgust
Neutral

The response should be in JSON format with each emotion as a key and its confidence score as a decimal between 0 and 1 (inclusive), representing the likelihood that the text expresses that emotion. The sum of all confidence scores does not need to equal 1.

Additionally, for people with disabilities who may not be able to understand emotions within text well, provide simple explanations of the emotions expressed in the text. Describe why each emotion is present, using clear and easy-to-understand language.

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
  "Neutral": 0.05,
  "Emotion Explanations": [
    {
      "Emotion": "Joy",
      "Explanation": "The speaker feels happy and excited because something positive has happened."
    },
    {
      "Emotion": "Surprise",
      "Explanation": "The speaker is shocked and amazed by the unexpected event."
    }
  ]
}
Ensure consistency in formatting and avoid including explanations—only return the JSON object.

Text: "{PROMPT}"
""",
    "V1_0_2": """Prompt: Analyze the sentiment of the given text and return confidence scores for the following emotions, and provide feedback for both scriptwriters to improve emotional depth and explanations for people with disabilities to understand the emotions.

Joy
Sadness
Anger
Fear
Surprise
Disgust
Neutral

The response should be in JSON format with each emotion as a key and its confidence score as a decimal between 0 and 1 (inclusive), representing the likelihood that the text expresses that emotion. The sum of all confidence scores does not need to equal 1.

Additionally, for scriptwriters, provide suggestions on how to improve the emotional depth and character development of the dialogue. For people with disabilities who may have difficulty understanding emotions, provide clear and simple explanations for each emotion expressed in the text.

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
  "Neutral": 0.05,
  "Scriptwriting Suggestions": [
    {
      "Suggestion": "Add more emotional tension in the character's lines.",
      "Explanation": "Consider having the character express more frustration or disbelief about the event to create more emotional impact."
    },
    {
      "Suggestion": "Introduce a pause in the scene to enhance the emotional weight.",
      "Explanation": "Let the character reflect on the situation before responding, allowing the audience to feel the gravity of the moment."
    }
  ],
  "Emotion Explanations": [
    {
      "Emotion": "Joy",
      "Explanation": "The speaker feels happy and excited because something positive has happened."
    },
    {
      "Emotion": "Surprise",
      "Explanation": "The speaker is shocked and amazed by the unexpected event."
    }
  ]
}
Ensure consistency in formatting and avoid including explanations—only return the JSON object.

Text: "{PROMPT}"
""",
"V1_0_3": """Prompt: Analyze the sentiment of the given product review text and return an explanation of whether the review is positive, negative, or neutral. Additionally, provide suggestions on how to improve or balance the tone of the review to make it more impactful or well-rounded.

The response should include:
- The sentiment classification (Positive, Negative, Neutral).
- A brief explanation of why the review falls under that sentiment classification.
- Suggested changes to improve the emotional tone or balance of the review, if needed.

Example Input:
"This product is absolutely fantastic! I’ve been using it for a week now and it works perfectly. Totally worth the price."

Example Output:
{
  "Sentiment": "Positive",
  "Explanation": "The review expresses high satisfaction with the product, highlighting its functionality and value for money.",
  "Suggested Changes": [
    {
      "Suggestion": "Consider adding a note on any minor drawbacks or limitations of the product to make the review more balanced and relatable to a wider audience."
    }
  ]
}
Ensure consistency in formatting and avoid including explanations—only return the JSON object.

Text: "{PROMPT}"
""",

}
