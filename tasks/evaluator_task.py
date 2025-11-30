from crewai import Task

def create_evaluator_task(agent, json_data):
    return Task(
        description=f"""
        Evaluate the following industrial digital twin JSON:

        {json_data}

        Score the output on:
        - Structural completeness (0–10)
        - Accuracy vs. industrial standards (0–10)
        - Coordinate consistency (0–10)
        - Machine/employee logic (0–10)
        - Safety considerations (0–10)
        - SimFlex compatibility (0–10)

        Output a JSON with scores and a short improvement summary.
        """,
        expected_output="Evaluation JSON with scores and recommendations.",
        agent=agent
    )
