import streamlit as st
from backend import get_response
from config import APP_TITLE, APP_ICON , APP_MODE

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="centered",
)

st.title("Cloud Assistant")
st.caption("Your personal cloud and DevOps assistant")

# name = st.text_input("What is your name?")

# if st.button("Submit"):
#     if name:
#         st.success(f"Welcome, {name}!")
#     else:
#         st.warning("Please enter your name.")

# Initilaize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# sidebar controls
with st.sidebar:
    st.header("Settings")
    st.info(f"Application Mode: {APP_MODE}")
    st.write("Mode: Local Development")

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption("Built with Python and Streamlit")
    st.caption("Powered by Amazon Bedrock")

# Render conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# accept user prompt
prompt = st.chat_input("Ask me anything ...")

if prompt:
    # Display and store user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Process response with a loading indicator
    with st.chat_message("assistant"):
        with st.spinner("Thinking ..."):
            try:
                response = get_response(
                    prompt,
                    history=st.session_state.messages[:-1],
                )
            except Exception:
                st.error(
                    "Unable to process your request. "
                    "Please try again."
                )
                st.stop()
        st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant","content": response}
    )
