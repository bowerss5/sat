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
}
