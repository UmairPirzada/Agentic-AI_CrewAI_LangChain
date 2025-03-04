from crewai import Agent, Crew, Process, Task

from crewai.project import CrewBase, agent, crew, task
from crewai.tools import superDevTool, ScrapeWebsiteTools, FileWriterTool

from dotenv import load_dotenv

load_dotenv()
from crewai import tools
print(dir(tools))


@CrewBase
class AiNews:
    """AiNews crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def retrieve_news(self) -> Agent:
        return Agent(
            config=self.agents_config['retrieve_news'],
            tools=[superDevTool()],
            verbose=True
        )

    @agent
    def website_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['website_scraper'],
            tools=[ScrapeWebsiteTools()],
            verbose=True
        )

    @agent
    def ai_news_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_news_writer'],
            tools=[],
            verbose=True
        )

    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_writer'],
            tools=[FileWriterTool()],
            verbose=True
        )

    @task
    def retrieve_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_news_task']
        )

    @task
    def website_scraper_task(self) -> Task:
        return Task(
            config=self.tasks_config['website_scraper_task']
        )

    @task
    def ai_news_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_news_writer_task']
        )

    @task
    def file_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['file_writer_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiNews crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )
