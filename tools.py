def mock_searxng_search(query: str):
    if "crypto" in query:
        return "Bitcoin hits all-time high"
    elif "AI" in query:
        return "New AI model replaces developers"
    else:
        return "Global economy shows mixed signals"