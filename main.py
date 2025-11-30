from dotenv import load_dotenv
from crewai import Crew, Process

# ---------------------------------------------------------
# Config
# ---------------------------------------------------------
from config.llm_config import initialize_llm
from config.chromadb_config import init_chroma

# ---------------------------------------------------------
# Utils
# ---------------------------------------------------------
from utils.pdf_reader import extract_text_from_pdf
from utils.pdf_cleaner import clean_pdf_text
from utils.vector_store import store_chunks
from utils.json_cleanup import safe_json
from utils.json_store import save_json
from utils.simflex_exporter import convert_to_simflex, save_simflex_scene

# ---------------------------------------------------------
# Agents
# ---------------------------------------------------------
from agents.loader_agent import create_loader_agent
from agents.json_extractor_agent import create_json_extractor_agent
from agents.reasoning_agent import create_reasoning_agent
from agents.simflex_generator_agent import create_simflex_agent
from agents.evaluator_agent import create_evaluator_agent

# ---------------------------------------------------------
# Tasks
# ---------------------------------------------------------
from tasks.loader_task import create_loader_task
from tasks.json_task import create_json_task
from tasks.reasoning_task import create_reasoning_task
from tasks.simflex_task import create_simflex_task
from tasks.evaluator_task import create_evaluator_task


# ============================================================
#             MAIN DIGITAL TWIN PIPELINE (PATCHED)
# ============================================================

def extract_output_text(output_obj):
    """Return plain text from CrewOutput."""
    if hasattr(output_obj, "output_text"):
        return output_obj.output_text
    if hasattr(output_obj, "raw"):
        return output_obj.raw
    return str(output_obj)


def main():
    load_dotenv()

    # ---------------------------------------------------------
    # Initialize LLM + ChromaDB
    # ---------------------------------------------------------
    llm = initialize_llm()
    chroma = init_chroma()

    # ---------------------------------------------------------
    # Load & Clean PDF
    # ---------------------------------------------------------
    print("📄 Loading PDF from ./data/input.pdf ...")
    raw_pdf = extract_text_from_pdf("./data/input.pdf")
    pdf_text = clean_pdf_text(raw_pdf)
    print("✔ PDF loaded and cleaned")

    # ---------------------------------------------------------
    # Store PDF chunks into ChromaDB
    # ---------------------------------------------------------
    print("📚 Storing PDF text chunks into ChromaDB...")
    pdf_chunks = pdf_text.split("\n\n")
    store_chunks(chroma, pdf_chunks)
    print("✔ PDF chunks stored")

    # =========================================================
    #                 1) LOADER AGENT
    # =========================================================
    loader_agent = create_loader_agent(llm)
    loader_task = create_loader_task(loader_agent, pdf_text)

    # Run LOADER alone first
    print("\n🔍 Running Loader Agent...")
    loader_crew = Crew(
        agents=[loader_agent],
        tasks=[loader_task],
        process=Process.sequential,
        verbose=True
    )
    loader_output = loader_crew.kickoff()

    loader_text = extract_output_text(loader_output)
    print("\n===== LOADER RESULT =====")
    print(loader_text[:800], "...\n")  # Preview

    # =========================================================
    #                 2) JSON EXTRACTOR AGENT
    # =========================================================
    json_agent = create_json_extractor_agent(llm)
    json_task = create_json_task(json_agent, loader_text)

    # =========================================================
    #                 3) REASONING AGENT
    # =========================================================
    reasoning_agent = create_reasoning_agent(llm)
    reasoning_task = create_reasoning_task(reasoning_agent)

    # =========================================================
    #                 4) SIMFLEX GENERATION AGENT
    # =========================================================
    simflex_agent = create_simflex_agent(llm)
    simflex_task = create_simflex_task(simflex_agent)

    # =========================================================
    #                 RUN FULL PIPELINE
    # =========================================================
    crew = Crew(
        agents=[
            json_agent,
            reasoning_agent,
            simflex_agent
        ],
        tasks=[
            json_task,
            reasoning_task,
            simflex_task
        ],
        process=Process.sequential,
        verbose=True
    )

    print("🚀 Running JSON → Reasoning → SimFlex pipeline...")
    pipeline_output = crew.kickoff()

    pipeline_text = extract_output_text(pipeline_output)

    # =========================================================
    #            SAVE DIGITAL TWIN JSON OUTPUT
    # =========================================================
    print("\n===== PARSING DIGITAL TWIN RESULT =====")
    digital_twin_json = safe_json(pipeline_text)

    twin_json_path = save_json(digital_twin_json, "digital_twin_output.json")
    print(f"💾 Digital Twin JSON saved at: {twin_json_path}")

    # ---------------------------------------------------------
    # Store Final JSON into ChromaDB
    # ---------------------------------------------------------
    print("📦 Storing final JSON into ChromaDB...")

    json_lines = pipeline_text.split("\n")
    chroma.add(ids=["json-full"], documents=[pipeline_text])

    for i, line in enumerate(json_lines):
        if len(line.strip()) > 0:
            chroma.add(
                ids=[f"json-line-{i}"],
                documents=[line]
            )

    print("✔ JSON inserted into ChromaDB")

    # =========================================================
    #                5) EVALUATION AGENT
    # =========================================================
    print("\n🔍 Running Evaluation Agent...")

    evaluator_agent = create_evaluator_agent(llm)
    evaluation_task = create_evaluator_task(
        evaluator_agent,
        digital_twin_json
    )

    crew_eval = Crew(
        agents=[evaluator_agent],
        tasks=[evaluation_task],
        process=Process.sequential,
        verbose=True
    )

    evaluation_output = crew_eval.kickoff()
    evaluation_text = extract_output_text(evaluation_output)

    print("\n===== EVALUATION REPORT =====")
    print(evaluation_text)

    evaluation_json = safe_json(evaluation_text)
    eval_path = save_json(evaluation_json, "evaluation_report.json")
    print(f"📊 Evaluation JSON saved at: {eval_path}")

    # =========================================================
    #                6) SIMFLEX SCENE EXPORT
    # =========================================================
    print("\n🎨 Generating SimFlex Scene JSON...")
    simflex_scene = convert_to_simflex(digital_twin_json)
    scene_path = save_simflex_scene(simflex_scene)

    print(f"🎉 SimFlex Scene file generated at: {scene_path}")

    print("\n🚀 Pipeline Completed Successfully — Digital Twin is Ready!")


# ---------------------------------------------------------
# MAIN ENTRY POINT
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
