from ai.prompts import EVALUATION_PROMPT
from core.scenarios import SCENARIOS
from ai.client import get_ai_response
from ai.utils import extract_clean_json, save_result

def calculate_overall_score(ai_response_json):
    scores = ai_response_json.get("scores", {})
    VALID_SCORE_KEYS = ["medical_accuracy", "clarity", "empathy", "completeness"]
    filtered_scores = {k: scores.get(k) for k in VALID_SCORE_KEYS if isinstance(scores.get(k), (int, float))}
    if filtered_scores:
        overall_score = sum(filtered_scores.values()) / len(filtered_scores)
    else:
        overall_score = 0.0
    return overall_score


def analyze_store_response(scenario_id, user_response):
    prompt = EVALUATION_PROMPT.format(
        scenario=SCENARIOS[scenario_id]["description"],
        response=user_response
    )
    try:
        ai_response = get_ai_response(prompt)
        ai_response_json = extract_clean_json(ai_response)
        if ai_response_json is None:
            raise Exception("AI response is not a valid JSON object")
        
        overall_score = calculate_overall_score(ai_response_json)
        ai_response_json["overall_score"] = overall_score

        result = {
            "scenario_id": scenario_id,
            "user_response": user_response,
            "ai_response_json": ai_response_json
        }
        save_result(result)
        
        return ai_response_json
    except Exception as e:
        return {"error": str(e)}