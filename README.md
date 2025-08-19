https://github.com/Arundhas1212/ai-healthcare-assistant/releases

# AI Healthcare Assistant — Practice Clinical Communication

[![Release](https://img.shields.io/github/v/release/Arundhas1212/ai-healthcare-assistant?color=0ea5a4&label=Releases)](https://github.com/Arundhas1212/ai-healthcare-assistant/releases)

A Streamlit app that helps clinicians and trainees practice patient interviews. It uses Google Generative AI (Gemini) for scenario creation and evaluation. It also supports voice input and speech-to-text for realistic, spoken practice sessions.

Topics: ai, communication, gemini, google-gemini, healthcare, llm, python, speech-to-text, streamlit, stt, voice-assistant, voice-input, voice-transcription, ysskrishna

Badges
- Language: Python
- Framework: Streamlit
- Model: Google Gemini
- Voice: Speech-to-Text

Screenshot
![Doctor using computer and microphone](https://images.unsplash.com/photo-1582719478250-7fbf8b0af56c?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1200&fit=max)

Table of Contents
- About
- Key features
- Who this helps
- Quick start
- Release downloads
- Configuration
- How it works
- Scenario engine
- Evaluation rubric
- Voice and transcription
- Example sessions
- Deployment
- Docker
- Testing
- Development notes
- Contributing
- API and prompt patterns
- Security and secrets
- Performance and scaling
- Roadmap
- Credits
- License
- Troubleshooting and FAQ

About
This repo contains a learning tool. It helps learners practice patient interviews and get instant, structured feedback. The app creates case scenarios that mimic real encounters. It accepts typed or spoken input. It transcribes voice to text and scores communication across core clinical skills. The app uses Google Generative AI (Gemini) as the LLM and a speech-to-text service for voice input. It runs in Streamlit and supports local and cloud runs.

Key features
- Scenario generation: Create diverse patient cases on demand.
- Voice input: Record a patient interview and get a transcript.
- Live feedback: Receive immediate evaluations on empathy, questioning, and clarity.
- Scoring rubric: Quantitative and qualitative scores.
- Custom prompts: Configure scenario types and difficulty.
- Export: Save transcripts, recordings, and reports.
- Local and cloud-ready: Run locally or deploy to Streamlit Cloud or a container.
- Open design: Clear modules for LLM, STT, UI, and evaluation.

Who this helps
- Medical students practicing communication skills.
- Residents training for patient interviews.
- Nursing staff learning focused history taking.
- Educators who want a set of reproducible cases.
- Researchers studying clinical communication and AI feedback.

Quick start

Prerequisites
- Python 3.10 or later
- pip
- A Google Cloud project enabled for Generative AI (Gemini) and Speech-to-Text, or equivalent credentials
- Microphone for voice practice

Install
1. Clone the repo.
   git clone https://github.com/Arundhas1212/ai-healthcare-assistant.git
2. Change directory.
   cd ai-healthcare-assistant
3. Install packages.
   pip install -r requirements.txt

Run the app
- Start the Streamlit app.
  streamlit run app.py

The app opens in your browser. Use the GUI to create scenarios, record voice, and get feedback.

Release downloads
This project publishes release assets. Download the release file listed on the Releases page and run it as described. The file needs to be downloaded and executed. Visit the releases page here:
https://github.com/Arundhas1212/ai-healthcare-assistant/releases

To create a reproducible environment, we publish a packaged release. Download the asset that matches your platform. The release asset may include a packaged app, a Docker image reference, or a prebuilt wheel. After download, follow the run notes in the release description.

Configuration

Environment variables
Set these keys in your shell or environment manager. Commands assume a POSIX shell.

- GOOGLE_API_KEY — API key for Generative AI.
- GOOGLE_PROJECT_ID — Google Cloud project id.
- GOOGLE_APPLICATION_CREDENTIALS — Path to service account JSON, when required.
- STT_PROVIDER — "google" or "local" (controls speech-to-text selection).
- STREAMLIT_SERVER_PORT — Optional port number.

Example export statements:
export GOOGLE_API_KEY="your_api_key_here"
export GOOGLE_PROJECT_ID="my-project-id"
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/creds.json"
export STT_PROVIDER="google"

Requirements
The requirements.txt contains core packages:
- streamlit
- openai (used for auxiliary tools if present)
- google-cloud-speech (if using Google STT)
- google-generative-ai (or a wrapper)
- sounddevice
- python-dotenv
- pydub
- webrtc-streamlit or streamlit-webrtc
- pydantic
- requests

How it works

Core modules
- app.py — Streamlit entrypoint and UI.
- lib/llm.py — Wrapper for Gemini prompts and calls.
- lib/stt.py — Speech-to-text adapter.
- lib/scenario.py — Scenario generator and seed cases.
- lib/evaluate.py — Scoring and feedback engine.
- lib/audio.py — Recording and playback helpers.
- lib/export.py — Report generation and storage.

Flow
1. User chooses scenario type and difficulty.
2. The Scenario Engine creates a patient prompt.
3. The app presents the case as a brief patient statement.
4. The user types or records questions and responses.
5. Voice gets transcribed by STT.
6. The transcript and input go to the LLM for scoring.
7. The Evaluation module returns scores and suggested phrasing.
8. The UI shows scores, text feedback, and replay controls.

Scenario engine

Design goals
- Reproducible cases with random variation.
- Clinical realism and consistency.
- Adjustable complexity for learner level.

Types of scenarios
- Acute chest pain
- Shortness of breath
- Abdominal pain
- Medication counseling
- End-of-life discussion
- Chronic disease follow-up
- Pediatric well visit
- Mental health triage

Scenario fields
Each scenario includes:
- patient_profile: Age, sex, relevant history.
- chief_complaint: Key presenting problem.
- vitals: Optional vitals for context.
- red_flags: Critical items that should prompt escalation.
- distractors: Items that can mislead learner.
- educational_goals: Target skills for scoring.

Seeding
The repo ships with a seed set in lib/scenario.py. The app can expand the set with prompts to Gemini:
- Use base prompt templates.
- Apply controlled randomization to symptoms, duration, and comorbidities.

Scenario prompt example (to LLM)
Write a short patient persona for a 64-year-old male with chest discomfort. Include onset, location, risk factors, and one ambiguous symptom that could suggest a non-cardiac cause. Keep persona under 120 words.

Evaluation rubric

Core competencies
The app evaluates across clear competencies. Scores combine rubric checks, LLM analysis, and heuristics.

- Empathy and rapport (0-5)
  - Greets the patient.
  - Uses patient-centered language.
  - Validates concerns.

- History gathering precision (0-10)
  - Asks open and closed questions.
  - Covers onset, timing, severity, alleviating/aggravating factors.
  - Checks red flags.

- Clinical reasoning and prioritization (0-10)
  - Solicits relevant systems review.
  - Identifies likely differential diagnoses.
  - Recognizes urgent findings.

- Communication clarity (0-5)
  - Explains next steps in plain language.
  - Uses teach-back or checks for understanding.

- Time management and focus (0-5)
  - Keeps conversation efficient.
  - Avoids irrelevant tangents.

Score synthesis
- Each category returns a numeric score and a short rationale.
- The app synthesizes an overall score and a strengths/areas list.
- Feedback includes example phrases and alternatives.

Example scoring output
Empathy: 4/5
- Rationale: Open with "How are you feeling today?" but missed validating fear.

History: 8/10
- Rationale: Asked onset, quality, radiation. Missed asking about nausea.

Suggested phrasing:
- "I can see this is worrying. Tell me more about when the pain started."
- "Have you had any nausea, sweating, or lightheadedness?"

Voice and transcription

Supported flows
- Browser-based recording (webrtc-streamlit).
- Local recording and upload.
- External file import (mp3, wav).

Transcription options
- Google Cloud Speech-to-Text
- Whisper (local)
- A fallback local STT adapter

Audio capture
- The UI starts a record session.
- The client streams audio to a local buffer.
- The app saves a WAV file for processing.

Processing pipeline
1. Capture audio.
2. Normalize and resample to 16 kHz.
3. Send to STT provider.
4. Receive transcript and confidence scores.
5. Pass transcript to LLM with the scenario context.

Tips for high-quality audio
- Use a headset mic.
- Reduce background noise.
- Keep a short distance from the microphone.
- Speak at natural pace.

Example session transcripts
Below are anonymized transcripts that the app would analyze. They show sample interactions and the app's output.

Session A — Chest pain (voice input)
Patient: "I've had chest tightness for two hours. It started when I climbed stairs. I'm scared."
Learner: "When did the pain start? Can you point to where it hurts?"
Learner: "Have you had any nausea, sweating, or trouble breathing?"
Transcript delivered to the LLM for evaluation.

LLM feedback:
- Asked onset and location. Good.
- Included an open question. Good.
- Missed a direct question about syncope. Suggest adding: "Have you felt faint or lost consciousness?"

Session B — Medication counseling (typed input)
Patient: "I do not understand why I need this new blood pressure pill."
Learner: "This medicine lowers your blood pressure by relaxing vessels. It can help reduce stroke risk."
LLM feedback:
- Answer was brief and clinical. Suggest adding patient-centered phrasing: "Does that make sense? What concerns do you have?"

Deployment

Local
- Use the run steps above.
- For sound capture, run in a browser that supports getUserMedia.

Streamlit Cloud
- Connect the GitHub repo to your Streamlit account.
- Add environment variables in the app settings (GOOGLE_API_KEY, etc.).
- Deploy.

Heroku
- Use a Procfile:
  web: streamlit run app.py --server.port $PORT
- Add buildpack for Python.
- Add environment variables through the dashboard.

Docker

Dockerfile (summary)
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]

Build and run
docker build -t ai-healthcare-assistant .
docker run -p 8501:8501 -e GOOGLE_API_KEY=$GOOGLE_API_KEY ai-healthcare-assistant

Compose example
version: "3.8"
services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - STT_PROVIDER=${STT_PROVIDER}
    volumes:
      - ./data:/app/data

Testing

Unit tests
- Tests live under tests/.
- Run with pytest.
  pytest -q

Key test areas
- Scenario generation: checks for valid fields.
- LLM wrapper: mocks external calls and validates prompt format.
- STT adapter: validates expected outputs for mock audio.
- Evaluation engine: verifies score ranges and feedback labels.

End-to-end
- A simple end-to-end script records a short sample and checks the output JSON for required keys: transcript, scores, feedback.

Development notes

Code style
- Use black and isort.
- Keep functions small and testable.
- Document public functions with short docstrings.

Main design patterns
- Adapter for external services (LLM, STT).
- Pure functions for scoring logic.
- DTOs (pydantic) for scenario objects.

Contributing

How to contribute
- Fork the repository.
- Create a feature branch.
- Add tests.
- Open a PR with a clear description and tests.

Areas that need help
- Add more seed scenarios.
- Improve evaluation rubric for mental health encounters.
- Add multilingual support.
- Add user accounts and progress tracking.

PR checklist
- Code runs and tests pass locally.
- New code includes unit tests.
- Documentation updates included for any behavior changes.

API and prompt patterns

LLM wrapper
The wrapper centralizes prompt handling. It enforces a template and a system instruction.

System instruction (example)
You are a clinical educator AI. Evaluate the learner's communication skills. Provide a numeric score for each category and a short text rationale. Offer two sample phrases to improve empathy or clarity.

Prompt structure
- System message: instruct role and safety.
- User message: scenario context.
- Assistant input: learner transcript.

Example prompt to Gemini
System: [as above]
User: Patient profile: 72-year-old female with shortness of breath. Vitals: HR 105, RR 22.
Assistant: Learner transcript: "..."

Return format
- JSON with fields: empathy, history, reasoning, clarity, suggestions, overall_score.

Prompt engineering tips
- Keep prompts explicit about desired output format.
- Use short bullet lists to constrain output.
- Provide sample outputs in the prompt for consistent structure.

Sample LLM request (pseudo)
{
  "system": "You are a clinical educator.",
  "messages": [
    {"role": "user", "content": "Scenario..."},
    {"role": "assistant", "content": "Learner transcript..."}
  ],
  "max_tokens": 300
}

Security and secrets

Key management
- Use environment variables for keys.
- Use a secrets manager for production.
- Avoid committing credentials.

Local file handling
- Store recordings in a data folder with unique names.
- Rotate or delete old files based on retention policy.

Privacy
- The app records and stores audio and transcripts.
- Ensure you inform users before recording.
- For deployments used with real patients, follow institutional policy and data protection laws.

Performance and scaling

Profiling
- Profile LLM and STT calls as they drive most latency.
- Cache repeated LLM prompts when plausible.

Scaling
- Use async calls to LLM and STT.
- For many concurrent users, deploy the backend behind a load balancer and scale horizontally.
- Consider batching STT requests for recorded sessions.

Costs
- LLM calls and STT services incur cloud charges.
- Monitor usage and set quotas at the project level.

Roadmap

Short term
- Add multi-turn evaluation that tracks progress across a single session.
- Improve UI to show replay with timestamps and score overlays.
- Add role-play mode where the LLM acts as a patient voice.

Medium term
- User accounts and progress tracking.
- Curriculum builder for educators with case sets and quizzes.
- Offline STT option with lightweight models for low-latency environments.

Long term
- Integrate live feedback during the interview.
- Build multimodal feedback combining transcript, prosody, and facial cues.
- Support simulated family meetings and group scenarios.

Credits

Core contributors
- ysskrishna — primary developer and maintainer.

Libraries and services
- Streamlit — UI framework.
- Google Generative AI (Gemini) — LLM for scenario creation and evaluation.
- Google Speech-to-Text / Whisper — STT options.
- webrtc-streamlit / streamlit-webrtc — browser audio capture helpers.

Images
- Unsplash photos for README images.

License

This project uses the MIT License. See LICENSE file in the repository.

Releases and downloads

Primary release page:
https://github.com/Arundhas1212/ai-healthcare-assistant/releases

Download the release asset for your platform. The file needs to be downloaded and executed per the release notes. Each release includes a run guide and a checksum for verification.

Troubleshooting and FAQ

Why do I see low-quality transcriptions?
- Check microphone input level.
- Use a headset.
- Switch to a different STT provider in settings.

Why does the LLM give vague feedback?
- Verify your API key and project limits.
- Inspect the sent prompt for missing context.
- Increase max_tokens or provide a sample output to the prompt.

How can I add a custom scenario?
- Add a JSON file in data/scenarios/.
- Use the UI import tool to load the file.
- Follow the scenario schema in lib/scenario.py.

How do I change the scoring weights?
- Edit lib/evaluate.py.
- Update weight constants at the top and rerun tests.

Where are recordings stored?
- Local runs save to data/recordings/.
- Cloud runs may store to a configured bucket or the app's storage.

How to test without cloud keys?
- Use the provided mock adapters in tests/mocks/.
- Set STT_PROVIDER=mock and LLM_PROVIDER=mock in your environment.

Example advanced prompt templates

1) Focused history template
System: You are a clinical teacher. Evaluate how well the learner performs a focused history for chest pain.
User: Scenario: [patient text]
Assistant: Learner transcript: [text]
Return JSON with keys: history_score, missed_items, urgent_flags, sample_questions.

2) Empathy booster
System: You are a coach for communication skills.
User: Learner line: "The pain is probably nothing."
Assistant: Suggest three rewrites that show empathy and invite disclosures.

Appendix: sample scenario JSON

{
  "id": "cp-001",
  "title": "Chest tightness after exertion",
  "patient_profile": {
    "age": 64,
    "sex": "male",
    "history": ["hypertension", "smoker"]
  },
  "chief_complaint": "Chest tightness for 2 hours",
  "vitals": {
    "bp": "150/90",
    "hr": 98,
    "rr": 18,
    "temp": 36.8,
    "spo2": "96%"
  },
  "red_flags": ["sweating", "nausea", "syncope"],
  "educational_goals": ["ask about onset", "assess risk", "explain next steps"]
}

Frequently used CLI helpers

- Export a sample report
  python tools/export_report.py --session-id SESSION123 --out report.json

- Run tests
  pytest -q

- Lint
  black .
  isort .

Extending STT support
- Add a new adapter implementing transcribe(audio_path) that returns {"text": "...", "confidence": 0.95}.
- Register the adapter in lib/stt.py and the settings.

Extending LLM support
- The LLM wrapper expects a send(prompt, options) and returns structured JSON.
- Add a new provider in lib/llm_providers/ and update config.

User experience tips for educators
- Create a set of 8 cases for a single session.
- Set clear goals for each learner before the run.
- Use the export feature to track progress over time.
- Combine app reports with human debriefs.

Data model

Primary objects
- Session — Contains scenario id, timestamp, user id, transcript, audio file, scores.
- Scenario — Template for patient persona.
- Feedback — Structured output from LLM with suggestions.

Storage
- Local mode: data/sessions.json and data/recordings/.
- Cloud mode: optional connector to S3 or GCS.

Analytics
- Store anonymized metrics: average scores per scenario, common missed items.
- Use these metrics to adapt scenario difficulty.

Examples of suggested feedback phrases

Empathy prompts
- "I can see this worries you. Tell me more about what feels most concerning."
- "That sounds hard. What effect has this had on your daily life?"

Closing the visit
- "Here's the plan: I will order tests, start medication X, and follow up in 48 hours."
- "Do you have any questions about this plan?"

Sample educational case flow

1. Launch app.
2. Select "Chest pain — Intermediate".
3. App shows scenario summary and two objectives.
4. Start audio recording and conduct a 5-minute interview.
5. Stop recording.
6. App transcribes and sends to Gemini.
7. Receive scores and suggested scripts.
8. Replay audio with highlighted timestamps for missed questions.
9. Export a report.

Integration ideas
- Link progress to an LMS via LTI.
- Use Webhooks to send session data to a debriefing tool.
- Connect to standard EHR test instances for scenario realism.

Community and support
- Use the repository Issues to report bugs or request features.
- Open PRs for scenario additions or fixes.

Further reading and references
- Clinical communication textbooks for rubric design.
- Google Generative AI docs for API usage and quotas.
- Streamlit docs for deployment and UI patterns.
- Research on conversational agents in clinical education.

Contact
Open an issue or a pull request on the GitHub repo for feature requests or bug reports.

License
MIT

Acknowledgments
This project builds on open-source tools and the Streamlit community. The design reflects input from clinicians and learners who tested early prototypes.