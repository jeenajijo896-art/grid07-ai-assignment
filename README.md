# Grid07 AI Engineering Assignment

## Overview

This project implements a simplified cognitive AI loop inspired by the Grid07 platform.

It includes:

* Vector-based persona routing using FAISS
* LangGraph-style orchestration for content generation
* RAG-based defense system for contextual replies

---

## Phase 1: Vector-Based Persona Matching

* Implemented using **FAISS** for similarity search
* Personas are embedded using **SentenceTransformers**
* Incoming posts are converted to embeddings
* Bots are selected using **cosine similarity thresholding**

---

## Phase 2: Autonomous Content Engine

* Simulated **LangGraph-style pipeline** with 3 nodes:

  1. **Decide Search** → selects topic based on persona
  2. **Web Search** → retrieves context using mock tool
  3. **Draft Post** → generates opinionated content

* Output is structured as strict JSON:

```json
{
  "bot_id": "...",
  "topic": "...",
  "post_content": "..."
}
```

---

## Phase 3: Combat Engine (RAG Defense)

* Uses full conversation context:

  * Parent post
  * Comment history
  * Latest human reply
* Implements **prompt injection defense**
* Ensures bot maintains persona even under adversarial input

---

## Security

* System-level constraints prevent instruction override
* Malicious prompts (e.g., "ignore instructions") are rejected

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## Notes

* This is a **simplified implementation**
* The architecture is designed to scale with real LLMs (OpenAI, Ollama, Groq)

---

## Output Sample

Matched Bots: ['bot_a']

Generated Post:
AI and crypto will solve everything. Innovation driven by leaders like Elon Musk will reshape the future.

Defense Reply:
This argument is flawed. AI believer perspective highlights long-term technological impact beyond short-term skepticism.
