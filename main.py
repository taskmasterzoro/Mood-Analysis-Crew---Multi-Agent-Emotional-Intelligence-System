from dotenv import load_dotenv
import os
import sys

# This ensures the 'src' directory is on the Python path
# so that the 'iit_project' package can be found.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Important: Load environment variables before importing the UI
load_dotenv()

from iit_project.ui import chatbot_interface

def run():
    """
    Launches the Gradio web interface for the IIT Project Support Bot.
    """
    print("Starting the Gradio web interface...")
    # The launch logic is now handled in ui.py
    chatbot_interface.launch()

if __name__ == "__main__":
    run()
