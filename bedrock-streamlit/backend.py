def get_response(prompt: str) -> str:
    """
    Process a user prompt and return a response.
    For now, this is a placeholder.
    Later, we will call Amazon Bedrock here.
    """

    if not prompt.strip():
        return "Please enter a question."
    
    return (
        f"You asked: {prompt}\n\n"
        "This response comes from our Python backend. "
        "Later, Amazon Bedrock will generate the answer."
    )