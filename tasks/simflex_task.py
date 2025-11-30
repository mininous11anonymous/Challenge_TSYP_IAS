from crewai import Task

def create_simflex_task(agent):
    return Task(
        description=(
            "Generate a SimFlex-ready 3D scene blueprint with coordinates, machine placements, "
            "employee workstations, walking paths, safety zones, and structural boundaries. "
            "Output should be JSON ready for import into a digital twin engine."
        ),
        expected_output="SimFlex scene JSON describing the 3D layout.",
        agent=agent
    )
