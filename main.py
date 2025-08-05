import streamlit as st
from core.scenarios import SCENARIOS
from core.analyzer import analyze_response

def main():
    st.set_page_config(page_title="AI Healthcare Assistant", layout="wide")
    st.title("AI Healthcare Assistant")
    st.write("Practice your healthcare communication skills with realistic scenarios.")
    st.sidebar.header("Select a Scenario")
    
    selected_scenario_id = st.sidebar.selectbox(
        "Choose a scenario:",
        options=list(SCENARIOS.keys()),
        format_func=lambda x: f"{SCENARIOS[x]['name']}"
    )
    
    selected_scenario = SCENARIOS[selected_scenario_id]
    
    st.subheader(f"Scenario: {selected_scenario['name']}")
    st.write(selected_scenario['description'])
    
    st.markdown("---")
    user_response = st.text_area(
        "Enter your response to this scenario:",
        height=200,
        placeholder="Type your response here..."
    )
    
    if st.button("Analyze Response", type="primary"):
        if user_response.strip():
            with st.spinner("Analyzing your response..."):
                analysis = analyze_response(selected_scenario_id, user_response)
                
                st.markdown("---")
                st.subheader("📊 Analysis Results")
                st.write(analysis)
        else:
            st.error("Please enter a response before analyzing.")

if __name__ == "__main__":
    main()
