import streamlit as st
from backend import get_response

st.set_page_config(
    page_title="Cloud Assistant",
    page_icon=":guardsman:",
)

st.title("Cloud Assistant")

# st.write("Our first step toward an Amazon Bedrock application")
st.caption("Learning to build an AI application step by step")

# Initilaize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
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
    
    # temporary reponse - no AI model yet
    response = (
        f"You asked: {prompt}\n\n"
        "this is a placeholder response from the Cloud Assistant."
        " we will connect to Amazon Bedrock later!"
    )

    response = get_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant",
        "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)



# name = st.text_input("What is your name?")

# if st.button("Submit"):
#     if name:
#         st.success(f"Welcome, {name}!")
#     else:
#         st.warning("Please enter your name.")
