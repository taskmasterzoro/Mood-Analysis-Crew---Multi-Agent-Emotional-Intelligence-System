import gradio as gr
from dotenv import load_dotenv
import sys
import os

# --- Path Correction ---
# This ensures the parent 'src' directory is on the Python path
# so the 'iit_project' package can be found.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load environment variables BEFORE importing the crew
load_dotenv()

from iit_project.crew import IitProjectCrew

# --- Crew Execution Function with Memory ---
def run_support_crew(message: str, history: list) -> str:
    """
    This function is called by the Gradio ChatInterface for each new message.
    It runs the two-stage support crew and manages conversation history.

    Args:
        message: The user's input message.
        history: The conversation history (managed by Gradio).

    Returns:
        The final response from the AI companion.
    """
    if not message.strip():
        return "Please share how you are feeling. I'm here to listen."

    # Keep the last 5 interactions (user + bot) for context
    # Each interaction is a list of [user_message, bot_response]
    recent_history = history[-5:]

    inputs = {
        "user_input": message,
        "conversation_history": recent_history
    }
    crew_instance = IitProjectCrew()

    # --- Stage 1: Crisis Detection ---
    # We run this silently to check for safety first.
    crisis_result = crew_instance.crisis_crew().kickoff(inputs=inputs)

    # --- Stage 2: Determine Response Flow ---
    if "true" in str(crisis_result).lower():
        # If a crisis is detected, run the response crew
        return str(crew_instance.crisis_response_crew().kickoff(inputs=inputs))
    else:
        # If no crisis, run the standard support crew
        return str(crew_instance.support_crew().kickoff(inputs=inputs))

# --- Gradio Interface Definition (Corrected for Compatibility) ---
# Using gr.ChatInterface for a classic chatbot look and feel.
# Removed arguments that are not supported in older Gradio versions.
chatbot_interface = gr.ChatInterface(
    fn=run_support_crew,
    title="AI Support Companion 🤖",
    description="Share your thoughts or feelings, and our AI companion will listen and suggest a helpful activity. Your conversation is private and not stored.",
    theme="soft",
    examples=[
        "I'm feeling really stressed about my upcoming exams.",
        "I had a bad day at work and I'm feeling down.",
        "I'm just not feeling like myself today."
    ],
    textbox=gr.Textbox(placeholder="How are you feeling today?", container=False, scale=7),
)

if __name__ == "__main__":
    print("Launching AI Support Companion...")
    # The share=True argument generates a public link for easy access.
    chatbot_interface.launch(share=True)
