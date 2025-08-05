import speech_recognition as sr
import streamlit as st
from typing import Optional

def setup_recognizer():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 4000
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 2.0
    return recognizer

def record_audio_continuous(recognizer: sr.Recognizer) -> Optional[sr.AudioData]:
    """
    Record audio from microphone continuously until stopped.
    
    Args:
        recognizer: Speech recognizer instance
    
    Returns:
        AudioData object if successful, None otherwise
    """
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
            return audio
    except sr.WaitTimeoutError:
        st.error("No speech detected. Please try again.")
        return None
    except Exception as e:
        st.error(f"Error recording audio: {str(e)}")
        return None

def speech_to_text(audio: sr.AudioData, recognizer: sr.Recognizer) -> Optional[str]:
    """
    Convert speech audio to text using Google's speech recognition.
    
    Args:
        audio: AudioData object from microphone
        recognizer: Speech recognizer instance
    
    Returns:
        Transcribed text if successful, None otherwise
    """
    try:
        with st.spinner("Converting speech to text..."):
            text = recognizer.recognize_google(audio)
            return text
    except sr.UnknownValueError:
        st.error("Could not understand the audio. Please try again.")
        return None
    except sr.RequestError as e:
        st.error(f"Could not request results from speech recognition service; {e}")
        return None
    except Exception as e:
        st.error(f"Error converting speech to text: {str(e)}")
        return None

def voice_input_widget() -> Optional[str]:
    """
    Streamlit widget for voice input functionality with start/stop controls.
    
    Returns:
        Transcribed text if successful, None otherwise
    """
    
    # Initialize session state for recording status
    if 'recording' not in st.session_state:
        st.session_state.recording = False
    if 'audio_data' not in st.session_state:
        st.session_state.audio_data = None
    if 'transcribed_text' not in st.session_state:
        st.session_state.transcribed_text = ""
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if not st.session_state.recording:
            if st.button("🎤 Start Recording", type="primary"):
                st.session_state.recording = True
                st.session_state.audio_data = None
                st.session_state.transcribed_text = ""
                st.rerun()
        else:
            if st.button("⏹️ Stop Recording", type="secondary"):
                st.session_state.recording = False
                st.rerun()
    
    with col2:
        if st.session_state.recording:
            st.info("🎤 Recording in progress... Click 'Stop Recording' when done.")
        else:
            st.markdown("""
            **Instructions:**
            - Click "Start Recording" to begin
            - Speak clearly into your microphone
            - Click "Stop Recording" when finished
            - Wait for text conversion to complete
            """)
    
    # Handle recording process
    if st.session_state.recording and st.session_state.audio_data is None:
        recognizer = setup_recognizer()
        audio = record_audio_continuous(recognizer)
        if audio:
            st.session_state.audio_data = audio
            st.session_state.recording = False
            st.rerun()
    
    # Handle transcription after recording stops
    if st.session_state.audio_data is not None and not st.session_state.transcribed_text:
        recognizer = setup_recognizer()
        text = speech_to_text(st.session_state.audio_data, recognizer)
        if text:
            st.session_state.transcribed_text = text
            st.session_state.audio_data = None
            st.success("✅ Speech converted successfully!")
            st.rerun()
        else:
            st.session_state.audio_data = None
            st.rerun()
    
    # Display transcribed text if available
    if st.session_state.transcribed_text:
        st.markdown("**Transcribed Text:**")
        st.text_area(
            "Your transcribed response:",
            value=st.session_state.transcribed_text,
            height=200,
            key="voice_transcription_display"
        )
        return st.session_state.transcribed_text
    
    return None 