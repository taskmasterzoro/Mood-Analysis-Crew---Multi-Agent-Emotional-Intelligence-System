#🌟 Introduction

Mood Analysis Crew is an innovative AI-powered emotional intelligence system that combines three specialized agents working in sequence to provide comprehensive emotional support. This multi-agent system analyzes user input, provides empathetic responses, and delivers personalized self-care recommendations using advanced NLP techniques.

Core Concept: Three specialized AI agents collaborate to deliver layered emotional intelligence:

🕵️‍♂️ Mood Analysis Agent - Detects emotional states

💬 Companion Agent - Provides empathetic conversation

🌱 Self-Care Agent - Recommends wellness strategies


🚀 How It Works
System Architecture
Diagram
Code
graph LR
A[User Input] --> B(Mood Analysis Agent)
B --> C(Companion Agent)
C --> D(Self-Care Agent)
D --> E[Personalized Output]





Workflow Breakdown
User Input: User shares feelings through text

Mood Analysis Agent:

Performs sentiment analysis (-1 to +1 scale)

Detects dominant emotions (anger, joy, sadness, etc.)

Identifies sarcasm and psychological context

Companion Agent:

Generates empathetic 3-turn dialogue

Adapts tone based on emotional state

Provides validation and support

Self-Care Agent:

Creates tiered recommendations:

🚨 Immediate actions

📅 Short-term goals

🌱 Long-term habits

Output: Formatted emotional wellness package

🧩 Key Components
1. Specialized Agents
Agent	Role	Key Capabilities
Mood Analysis Agent	Emotional Intelligence Analyst	Sentiment scoring, Emotion classification, Sarcasm detection
Companion Agent	Empathetic Digital Confidant	Adaptive tone, Emotional validation, Context-aware dialogue
Self-Care Agent	Wellness Architect	Science-backed recommendations, Tiered action plans, Habit building
2. Technical Implementation
python
# crew.py - Crew Orchestration
crew = Crew(
  agents=[mood_agent, companion_agent, self_care_agent],
  tasks=[analysis_task, dialogue_task, recommendation_task],
  process=Process.sequential
)
3. User Interface
Therapeutic Gradio interface featuring:

Calming color palette (purples/blues)

Mobile-responsive design

Real-time processing indicators

Privacy-first approach (no data persistence)

https://via.placeholder.com/800x400?text=Gradio+Interface <!-- Replace with actual screenshot -->

⚙️ Tech Stack
Core Technologies
CrewAI: Multi-agent orchestration framework

OpenAI: Advanced language models for emotional NLP

Gradio: Web UI with custom therapeutic design

pysbd: Sentence boundary detection

Key Libraries
requirements.txt
crewai
openai
gradio
python-dotenv
pydantic
pysbd
🛠️ Installation & Setup
Prerequisites
Python 3.9+

OpenAI API key

Installation
bash
# Clone repository
git clone https://github.com/taskmasterzoro/mood-analysis-crew.git
cd mood-analysis-crew

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "OPENAI_API_KEY=your_api_key_here" > .env
🚦 Usage
Running the Crew
bash
# Run with default input
python main.py --run

# Run with custom input
python main.py --run "I'm feeling stressed about my exams"
Training Mode
bash
# Train with 50 iterations
python main.py --train 50 output.json
Replay Mode
bash
# Replay specific task
python main.py --replay task_id_23
Web UI
bash
# Launch Gradio interface
python ui.py
Access at: http://localhost:7860

📁 Project Structure
text
mood_analysis/
├── agents.yaml        # Agent configurations
├── tasks.yaml         # Task definitions
├── crew.py            # Crew orchestration
├── main.py            # CLI interface
├── ui.py              # Gradio web UI (2,100+ lines)
├── custom_tool.py     # Tool extension template
├── .env.example       # Environment template
└── tests/             # Validation suite
🌐 Live Demo
https://img.shields.io/badge/%F0%9F%A4%97-Open%2520in%2520Spaces-blue.svg

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a pull request

See our Contribution Guidelines for details.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
For inquiries or support:

Mohit Kainwal: mohitkainwal418@gmail.com

Project Repository: github.com/taskmasterzoro/mood-analysis-crew
