from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class CareerCoach:
    """Personalized Career Coach Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # --- Agents ---
    @agent
    def resume_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_analyzer'],  # references agents.yaml
            verbose=True
        )

    @agent
    def skill_matcher(self) -> Agent:
        return Agent(
            config=self.agents_config['skill_matcher'],
            verbose=True
        )

    @agent
    def job_market_scanner(self) -> Agent:
        return Agent(
            config=self.agents_config['job_market_scanner'],
            verbose=True
        )

    @agent
    def career_recommendation(self) -> Agent:
        return Agent(
            config=self.agents_config['career_recommendation'],
            verbose=True
        )

    # --- Tasks ---
    @task
    def analyze_resume(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_resume']  # references tasks.yaml
        )

    @task
    def match_skills(self) -> Task:
        return Task(
            config=self.tasks_config['match_skills']
        )

    @task
    def scan_job_market(self) -> Task:
        return Task(
            config=self.tasks_config['scan_job_market']
        )

    @task
    def recommend_career_path(self) -> Task:
        return Task(
            config=self.tasks_config['recommend_career_path']
        )

    # --- Crew ---
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,   # from decorators
            tasks=self.tasks,     # from decorators
            process=Process.sequential,
            verbose=True
        )
