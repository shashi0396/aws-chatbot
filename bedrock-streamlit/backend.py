import os
from config import APP_MODE

def get_response(prompt: str , history: list | None = None) -> str:
    """Return a response to the user's prompt."""

    if not prompt or not prompt.strip():
        return "Please enter a question."
    
    if history is None:
        history = []
    
    mode = os.getenv("APP_MODE", "mock")

    if APP_MODE == "mock":
        previous_messages = len(history)

        return (
            f"You asked: {prompt}\n\n"
            f"Previous messages available: {previous_messages}\n\n"
            "This is a local development response. "
            "Bedrock integration will come later."
        )
    
    raise RuntimeError(
        f"Unsupported application mode: {APP_MODE}."
    )