🌐 Digital Twin Generator – Agentic AI + SimFlex Pipeline

🚀 An automated multi-agent system that converts industrial PDF reports into full 3D-ready Digital Twin JSON models
using CrewAI, LLMs, ChromaDB, and SimFlex-compatible exporters.

📌 Overview

This project implements a fully automated PDF → Digital Twin → 3D Scene pipeline.
It uses a sequence of specialized AI agents (CrewAI) to extract industrial information, generate structured JSON, validate constraints, evaluate quality, and output a SimFlex-ready 3D scene file.

✔ Key Capabilities

📄 Extract industrial data from PDF

🧠 Agentic reasoning with multiple specialized AI agents

📚 ChromaDB vector memory for industrial knowledge

🏭 Digital Twin JSON generation

🎨 SimFlex / FlexSim 3D scene export

🔍 Evaluation & scoring agent for quality assurance

🔄 Fully modular, extensible architecture

🧠 System Architecture
PDF Report
    ↓
Loader Agent (A1)
    ↓
Structured Text Extraction
    ↓
JSON Extractor Agent (A2)
    ↓
Industrial JSON Model
    ↓               ↘
ChromaDB Vector Memory  Reasoning Agent (A3)
    ↓                       ↓
Knowledge Retrieval    Layout Consistency Validation
    ↓                       ↓
SimFlex Generator Agent (A4)
    ↓
3D-Ready Scene JSON
    ↓
Evaluator Agent (A5)

🧩 Agents Overview
Agent	Purpose
A1 – Loader Agent	Extracts text, tables, layout, zones, machines, workers
A2 – JSON Extractor Agent	Produces structured industrial digital-twin JSON
A3 – Reasoning Agent	Validates constraints, safety, distances, flow logic
A4 – SimFlex Generator Agent	Converts JSON → 3D scene format
A5 – Evaluation Agent	Scores completeness, accuracy, safety, quality
📦 Technology Stack
Component	Technology
Agentic Framework	CrewAI
Language Models	OpenRouter (Gemma/Llama)
Memory	ChromaDB
PDF Extraction	PyPDF
JSON Export	Python (custom)
3D Scene Format	SimFlex / FlexSim compatible JSON
Environment	Python 3.12
Packaging	pip / virtualenv
📁 Project Structure
digital_twin_agentic/
│
├── main.py
├── .env
│
├── config/
│   ├── llm_config.py
│   ├── chromadb_config.py
│
├── agents/
│   ├── loader_agent.py
│   ├── json_extractor_agent.py
│   ├── reasoning_agent.py
│   ├── simflex_generator_agent.py
│   ├── evaluator_agent.py
│
├── tasks/
│   ├── loader_task.py
│   ├── json_task.py
│   ├── reasoning_task.py
│   ├── simflex_task.py
│   ├── evaluator_task.py
│
├── utils/
│   ├── pdf_reader.py
│   ├── pdf_cleaner.py
│   ├── vector_store.py
│   ├── json_cleanup.py
│   ├── json_store.py
│   ├── simflex_exporter.py
│
└── data/
    ├── input.pdf
    ├── digital_twin_output.json
    ├── simflex_scene.json
    ├── evaluation_report.json
