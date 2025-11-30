from crewai import Agent

def create_simflex_agent(llm):
    return Agent(
        role="SimFlex Digital Twin Generator",
        goal="Generate 3D-ready scene descriptions compatible with SimFlex or similar tools.",
        backstory="Transforms validated industrial data into precise 3D layout instructions.",
        llm=llm,
        verbose=True
    )
