from crewai import Task

def create_json_task(agent, raw_text):
    return Task(
        description=f"""
        Convert the following industrial PDF content into structured JSON:

        CONTENT:
        {raw_text}

        Extract:
        - factory zones
        - mapping structure
        - machines (model, type, location)
        - employees and positions
        - safety or workflow hints
        """,
        expected_output="JSON object with structured industrial layout data.",
        agent=agent
    )
