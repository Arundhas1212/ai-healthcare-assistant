import re
import json
import os
from core.config import Config
from datetime import datetime

def extract_clean_json(text):
    try:
        # Match the first complete {...} block
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            json_text = match.group(0)
            return json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
    return None

def save_result(result):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
    file_path = f"{Config.OUTPUT_DIR}/{timestamp}_result.json"
    with open(file_path, "w") as f:
        json.dump(result, f, indent=2)