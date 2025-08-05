import streamlit as st
from core.scenarios import SCENARIOS
from ai.analyzer import analyze_store_response
from ai.voice_utils import voice_input_widget

def main():
    st.set_page_config(page_title="AI Healthcare Assistant", layout="wide")
    
    st.sidebar.header("AI Healthcare Assistant")
    st.sidebar.write("Practice your healthcare communication skills with realistic scenarios.")
    
    selected_scenario_id = st.sidebar.selectbox(
        "Choose a scenario:",
        options=list(SCENARIOS.keys()),
        format_func=lambda x: f"{SCENARIOS[x]['name']}"
    )
    st.sidebar.markdown("---")
    
    # Author Section using Streamlit native components
    st.sidebar.markdown("### Author")
    st.sidebar.markdown("""
        <div class="author-header" style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: bold; color: white;">
                Y
            </div>
            <div class="author-info" style="display: flex; flex-direction: column; gap: 0px;">
                <p style="margin: 0; font-size: 16px; font-weight: bold;">ysskrishna</p>
                <p style="margin: 0; font-size: 15px; color: #666;">Full Stack Developer</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    


    if st.sidebar.button("🐙 GitHub: @ysskrishna", key="github_link"):
        st.markdown("[GitHub Profile](https://github.com/ysskrishna)")
    
    if st.sidebar.button("💼 LinkedIn: @ysskrishna", key="linkedin_link"):
        st.markdown("[LinkedIn Profile](https://linkedin.com/in/ysskrishna)")
    
    if st.sidebar.button("📁 View Source", type="primary", key="repo_link"):
        st.markdown("[Repository](https://github.com/ysskrishna/ai-healthcare-assisstant)")


    
    selected_scenario = SCENARIOS[selected_scenario_id]
    
    st.subheader(f"Scenario: {selected_scenario['name']}")
    st.write(selected_scenario['description'])
    
    st.markdown("---")
    
    # Input mode selection
    input_mode = st.radio(
        "Choose input method:",
        ["Text Input", "Voice Input"],
        horizontal=True
    )
    
    user_response = ""
    
    if input_mode == "Voice Input":
        voice_input_widget()
    else:
        user_response = st.text_area(
            "Enter your response to this scenario:",
            height=200,
            placeholder="Type your response here..."
        )
    
    if st.button("Analyze Response", type="primary"):
        if input_mode == "Text Input" and user_response.strip():
            analysis = analyze_store_response(selected_scenario_id, user_response)
        elif input_mode == "Voice Input" and st.session_state.transcribed_text:
            analysis = analyze_store_response(selected_scenario_id, st.session_state.transcribed_text)
        else:
            st.error("Please enter a response before analyzing.")
        
        with st.spinner("Analyzing your response..."):
            st.markdown("---")
            st.subheader("📊 Analysis Results")
            st.write(analysis)

if __name__ == "__main__":
    main()
