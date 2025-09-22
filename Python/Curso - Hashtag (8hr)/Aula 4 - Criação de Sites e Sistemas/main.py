import streamlit as st # importação de biblioteca para site [abreviação de streamlit = st]
from openai import OpenAI # importação da empresa OpenAI para o ChatGPT
modelo = OpenAI(api_key="https://api.openai.com/v1/organização/projetos/{id_do_projeto}/chaves_da_api") #import da chave da api

st.write("### Chatbot com IA") #título da página web
if not "lista_mensagens" in st.session_state: # se a lista de mensagens estiver na sessão do st
    st.session_state["lista_mensagens"] = [] # passa a coluna no parâmetro

for mensagem in st.session_state["lista_mensagem"]: # para a lista de mensagens na sessão do st
    role = mensagem["role"] # variável da mensagem do usuário
    content = mensagem["content"] # variável da mensagem do assistente
    st.chat_message(role).write(content) # mensagem de usuário no ChatBot

mensagem_usuario = st.chat_input("") # mensagem do usuário
if mensagem_usuario: # se existir mensagem do usuário, ele faz os passos
    st.chat_message("user").write(mensagem_usuario) # mensagem de usuário no ChatBot
    mensagem = {"role": "user", "content": mensagem_usuario} # dicionário com o tipo da mensagem do usuário
    st.session_state["lista_mensagens"].append(mensagem) # lista as mensagens e adiciona uma nova

    resposta_modelo = modelo.chat.completions.create( # craçao do modelo base do GPT
        messages=st.session_state["lista_mensagem"], # IA pega a lista de mensagens 
        model="gpt-4o" # modelo usado do GPT
    )
    resposta_ia = resposta_modelo.choices[0].message.content # IA responde baseado no primeiro item
    resposta_ia = "Você quis dizer: " + mensagem_usuario # resposta da IA com a mensagem do usuário
    st.chat_message("assistant").write(resposta_ia) # mensagem da IA no ChatBot

    mensagem_ia = {"role": "assistente", "content": resposta_ia} # dicionário de mensagens da IA
    st.session_state["lista_mensagens"].append(mensagem_ia) # lista as mensagens e adiciona uma nova da IA
    print(st.session_state["lista_mensagens"]) # exibe todas as mensagens na sessão do streamlit na web