import streamlit as st
from modules.llm_handler import query_mistral

def run_chat_interface():
    st.subheader("💬 Ask Your Spatial Question")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Enter your spatial analysis question...")

    if user_input:
        # Append user input
        st.session_state.chat_history.append(("user", user_input))

        with st.spinner("Thinking..."):
            response = query_mistral(user_input)

        # Append response
        st.session_state.chat_history.append(("bot", response))

    # Display chat history
    for sender, msg in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f"🧍‍♀️ **You**: {msg}")
        else:
            st.markdown(f"🤖 **Assistant**: {msg}")
