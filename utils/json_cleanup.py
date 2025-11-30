import json

def safe_json(text):
    """
    Convert messy LLM output into valid JSON whenever possible.
    """
    try:
        return json.loads(text)
    except:
        cleaned = text.replace("'", '"').replace("\n", "")
        try:
            return json.loads(cleaned)
        except:
            return {"error": "invalid_json", "raw": text}
