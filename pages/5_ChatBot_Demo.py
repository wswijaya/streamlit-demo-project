import streamlit as st
from openai import AzureOpenAI

st.title("ChatGPT-like clone")

client = AzureOpenAI(
    azure_endpoint=st.secrets["AzureOpenAI"]["AZ_OPENAI_API_ENDPOINT"],
    api_version=st.secrets["AzureOpenAI"]["AZ_OPENAI_API_VERSION"],
    api_key=st.secrets["AzureOpenAI"]["AZ_OPENAI_API_KEY"],
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = st.secrets["AzureOpenAI"]["AZ_MODEL_DEPLOYMENT_NAME"]

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

