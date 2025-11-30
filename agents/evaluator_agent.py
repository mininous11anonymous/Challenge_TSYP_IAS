from crewai import Agent

def create_evaluator_agent(llm):
    return Agent(
        role="Digital Twin Evaluator",
        goal="Evaluate the accuracy, completeness, and SimFlex readiness of the generated digital twin JSON.",
        backstory=(
            "Industrial engineering and simulation expert. "
            "Skilled in reviewing digital twin structures, "
            "checking coordinate consistency, machine placement logic, safety zones, and workflow accuracy."
        ),
        llm=llm,
        verbose=True
    )
