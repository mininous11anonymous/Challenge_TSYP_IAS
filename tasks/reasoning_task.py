from crewai import Task

def create_reasoning_task(agent):
    return Task(
        description=(
            "Using extracted JSON + vectorized context from ChromaDB, "
            "validate industrial constraints such as distances, safety margins, "
            "machine compatibility, workflow logic, and signal any inconsistencies."
        ),
        expected_output="Industrial reasoning report + validated layout suggestions.",
        agent=agent
    )
