from crewai import Task

def create_loader_task(agent, pdf_text):
    return Task(
        description=f"""
        You are the Loader & Layout Extraction Agent.

        Extract ALL industrial information from the following PDF content:
        ---
        {pdf_text}
        ---

        Extract EXACT strings from the PDF.
        DO NOT hallucinate.
        Identify:
        - zones
        - machines
        - employees
        - coordinates (if visible)
        - equipment lists
        - tables
        - workflows
        - layout clues

        Return the extracted content as CLEAN TEXT ONLY.
        """,
        expected_output="Raw extracted structured text from PDF.",
        agent=agent
    )
