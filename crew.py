from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
import os

# Updated import to include the new localized tool
from iit_project.tools.custom_tool import (
    mood_analysis_tool,
    self_care_recommendation_tool,
    crisis_detection_tool,
    localized_emergency_resource_tool
)

@CrewBase
class IitProjectCrew:
    """IitProjectCrew to support users based on their mood."""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:
        # --- Model Updated to gpt-4o-mini ---
        self.openai_llm = ChatOpenAI(
            # Switched to gpt-4o-mini for faster, high-quality responses.
            model_name=os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"), 
            temperature=0.7 
        )

    # --- Agent Definitions ---
    @agent
    def crisis_detector_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['crisis_detector_agent'],
            tools=[crisis_detection_tool, localized_emergency_resource_tool],
            llm=self.openai_llm,
            allow_delegation=False,
            verbose=True
        )

    @agent
    def mood_analyzer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['mood_analyzer_agent'],
            tools=[mood_analysis_tool],
            llm=self.openai_llm,
            allow_delegation=False,
            verbose=True
        )

    @agent
    def self_care_recommender_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['self_care_recommender_agent'],
            tools=[self_care_recommendation_tool],
            llm=self.openai_llm,
            allow_delegation=False,
            verbose=True
        )

    @agent
    def companion_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['companion_agent'],
            llm=self.openai_llm,
            allow_delegation=False,
            verbose=True
        )

    # --- Task Definitions ---
    @task
    def crisis_detection_task(self) -> Task:
        return Task(
            config=self.tasks_config['crisis_detection_task'],
            agent=self.crisis_detector_agent()
        )

    @task
    def crisis_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['crisis_response_task'],
            agent=self.crisis_detector_agent()
        )
        
    @task
    def mood_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['mood_analysis_task'],
            agent=self.mood_analyzer_agent()
        )

    @task
    def recommend_activity_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommend_activity_task'],
            agent=self.self_care_recommender_agent(),
            context=[self.mood_analysis_task()]
        )

    @task
    def compose_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['compose_response_task'],
            agent=self.companion_agent(),
            context=[self.mood_analysis_task(), self.recommend_activity_task()]
        )

    # --- Crew Definitions ---
    @crew
    def crisis_crew(self) -> Crew:
        """Crew for detecting a crisis."""
        return Crew(
            agents=[self.crisis_detector_agent()],
            tasks=[self.crisis_detection_task()],
            process=Process.sequential,
            verbose=False
        )

    @crew
    def crisis_response_crew(self) -> Crew:
        """Crew for responding to a crisis with localized resources."""
        return Crew(
            agents=[self.crisis_detector_agent()],
            tasks=[self.crisis_response_task()],
            verbose=True
        )

    @crew
    def support_crew(self) -> Crew:
        """Crew for standard mood analysis and support."""
        return Crew(
            agents=[
                self.mood_analyzer_agent(),
                self.self_care_recommender_agent(),
                self.companion_agent()
            ],
            tasks=[
                self.mood_analysis_task(),
                self.recommend_activity_task(),
                self.compose_response_task()
            ],
            process=Process.sequential,
            verbose=True
        )
