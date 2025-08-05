
def analyze_response(scenario_id, user_response):
    """
    Dummy analysis function that provides feedback on the user's response
    """
    analysis = {
        "communication_skills": "Good",
        "empathy_level": "High",
        "medical_accuracy": "Accurate",
        "patient_comfort": "Excellent",
        "suggestions": [
            "Consider using more simple language for non-native speakers",
            "Remember to ask for consent before procedures",
            "Always verify understanding with elderly patients"
        ]
    }
    
    # Add some variation based on scenario
    if scenario_id == 1:
        analysis["communication_skills"] = "Excellent - Good use of calming language"
        analysis["suggestions"].append("Consider using visual aids for non-native speakers")
    elif scenario_id == 2:
        analysis["medical_accuracy"] = "Very Accurate - Good explanation of procedure"
        analysis["suggestions"].append("Consider offering distraction techniques for needle anxiety")
    elif scenario_id == 3:
        analysis["patient_comfort"] = "Good - Clear instructions provided"
        analysis["suggestions"].append("Consider providing written instructions for elderly patients")
    
    return analysis