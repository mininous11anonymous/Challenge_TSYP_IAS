from crewai import Agent

def create_reasoning_agent(llm):
    return Agent(
        role="Industrial Reasoning & Validation Agent",
        goal="Check constraints, validate layout logic, and detect inconsistencies in the factory structure.",
        backstory="Expert in industrial engineering, safety constraints, process flows, and ergonomics.",
        llm=llm,
        verbose=True
    )
