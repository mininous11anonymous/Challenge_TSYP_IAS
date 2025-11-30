from crewai import Agent

def create_json_extractor_agent(llm):
    return Agent(
        role="Industrial Data Structuring Agent",
        goal="Convert raw PDF text into clean structured JSON with mapping, machines, and employees.",
        backstory="Specialist in converting semi-structured industrial documentation into JSON schemas.",
        llm=llm,
        verbose=True
    )
