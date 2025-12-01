import streamlit as st
import ollama

st.title("ZNET 🤖 ")
models = ["qwen2.5:0.5b", "qwen2.5-coder:1.5b"]
if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = models[0]
with st.expander("Model", expanded=False):
    selected = st.selectbox("Choose model", models, index=models.index(st.session_state["ollama_model"]))
    st.session_state["ollama_model"] = selected
    st.success(f"Selected model: {selected}")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_text = ""
        placeholder = st.empty()
        buffer = ""

        stream = ollama.chat(
            model=st.session_state["ollama_model"],
            messages=st.session_state.messages,
            stream=True
        )

        for chunk in stream:
            token = chunk["message"]["content"]
            buffer += token

            if len(buffer) > 10:
                response_text += buffer
                placeholder.write(response_text)
                buffer = ""

        if buffer:
            response_text += buffer
            placeholder.write(response_text)

    st.session_state.messages.append(
        {"role": "assistant", "content": response_text}
    )