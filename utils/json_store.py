import json
import os

def save_json(data, filename="digital_twin_output.json", folder="./data"):
    """Save the digital twin JSON result locally."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"💾 JSON saved at: {path}")
    return path
