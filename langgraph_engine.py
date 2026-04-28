import json

# Mock tool
def mock_searxng_search(query):
    if "crypto" in query.lower():
        return "Bitcoin hits new all-time high."
    if "ai" in query.lower():
        return "New AI model may replace developers."
    return "Tech industry continues rapid growth."


# Node 1: Decide Search
def decide_search(persona):
    if "AI" in persona or "crypto" in persona:
        return "latest AI crypto news"
    if "finance" in persona:
        return "market trends interest rates"
    return "tech society impact"


# Node 2: Web Search
def web_search(query):
    return mock_searxng_search(query)


# Node 3: Draft Post
def draft_post(bot_id, persona, context):
    post = f"{persona[:60]}... Based on news: {context}"
    
    return {
        "bot_id": bot_id,
        "topic": context,
        "post_content": post[:280]
    }


# Orchestrator (LangGraph style)
def generate_post(bot_id, persona):
    query = decide_search(persona)
    context = web_search(query)
    result = draft_post(bot_id, persona, context)

    return json.dumps(result, indent=2)