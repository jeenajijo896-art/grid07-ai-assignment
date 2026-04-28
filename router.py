from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Initialize embeddings
embedding = HuggingFaceEmbeddings()

# Bot personas
personas = {
    "bot_a": "AI and crypto will solve everything. Love Elon Musk, space.",
    "bot_b": "Tech is destroying society. Hate AI, love privacy.",
    "bot_c": "Markets, trading, ROI, finance mindset."
}

# Create vector DB
texts = list(personas.values())
metadatas = [{"id": k} for k in personas.keys()]

db = FAISS.from_texts(texts, embedding, metadatas=metadatas)

def route_post_to_bots(post_content, threshold=0.5):
    results = db.similarity_search_with_score(post_content, k=3)

    matched = []
    for doc, score in results:
        similarity = 1 - score
        if similarity > threshold:
            matched.append(doc.metadata["id"])

    return matched