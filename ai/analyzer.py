from ai.prompts import EVALUATION_PROMPT
from core.scenarios import SCENARIOS
from ai.client import get_ai_response
from ai.utils import extract_clean_json, save_result


def analyze_store_response(scenario_id, user_response):
    prompt = EVALUATION_PROMPT.format(
        scenario=SCENARIOS[scenario_id]["description"],
        response=user_response
    )

    print("Prompt: ", prompt)
    ai_response = get_ai_response(prompt)
    ai_response_json = extract_clean_json(ai_response)
    print("AI Response (JSON): ", ai_response_json)

    save_result(ai_response_json)
    
    return ai_response_json