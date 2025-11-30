from crewai import Agent

def create_loader_agent(llm):
    return Agent(
        role="PDF Loader & Layout Extractor",
        goal="Extract raw text, structure, and layout hints from industrial PDFs.",
        backstory="Expert in document ingestion and layout analysis.",
        llm=llm,
        verbose=True
    )
