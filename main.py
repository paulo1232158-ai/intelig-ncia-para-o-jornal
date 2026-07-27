import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key = "AQ.Ab8RN6KriuDXKUaeNqDtPq9ftZgr4o17cFx2bvdwTEc2KL6xLg",
                   base_url= "https://generativelanguage.googleapis.com/v1beta/openai")


st.write("# Assistente  Alfa IA") # markdown



if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")


for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    # Nome
    # user
    # assistant

    # ia respondeu
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-3.5-flash"
    )
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)