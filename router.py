from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Bot personas
personas = {
    "bot_a": "AI and crypto will solve all human problems. Optimistic about Elon Musk and tech.",
    "bot_b": "Tech monopolies are destroying society. Critical of AI and billionaires.",
    "bot_c": "Focus on markets, trading, ROI, finance."
}

# Create embeddings
texts = list(personas.values())
embeddings = model.encode(texts)

# FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def route_post_to_bots(post_content, threshold=0.7):
    post_embedding = model.encode([post_content])
    D, I = index.search(np.array(post_embedding), k=3)

    matched = []
    for dist, idx in zip(D[0], I[0]):
        similarity = 1 / (1 + dist)  # convert distance → similarity
        if similarity > threshold:
            bot_id = list(personas.keys())[idx]
            matched.append(bot_id)

    return matched