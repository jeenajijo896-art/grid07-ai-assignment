# Grid07 AI Assignment

## Overview
This project implements:
- Vector-based persona routing
- LangGraph-style AI content generation
- RAG-based defense system

## Phase 1
Used FAISS for vector similarity matching.

## Phase 2
LLM decides topic → search → generate post.

## Phase 3
RAG ensures context awareness and prevents prompt injection.

## Security
Prompt injection is prevented using system-level constraints.

## Run
pip install -r requirements.txt  
python main.py