from langchain.chat_models import ChatOpenAI
from tools import mock_searxng_search

llm = ChatOpenAI()

def generate_post(bot_id, persona):

    # Step 1: Decide topic
    topic = llm.predict(f"{persona}\nChoose a trending topic.")

    # Step 2: Search
    context = mock_searxng_search(topic)

    # Step 3: Generate post
    prompt = f"""
    Persona: {persona}
    Context: {context}

    Generate a strong opinionated tweet under 280 characters.

    Return JSON:
    {{"bot_id": "{bot_id}", "topic": "...", "post_content": "..."}}
    """

    return llm.predict(prompt)