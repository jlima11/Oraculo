import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq


TIPOS_ARQUIVOS_VALIDOS = [
    'Site', 'Youtube', 'pdf', 'csv', 'txt'
]

CONFIG_MODELOS = {'Groq': {'modelos': ['llama-3.1-8b-instant', 'gemma2-9b-it', 'deepseek-r1-distill-qwen-32b'], 'chat': ChatGroq},
                  'OpenAI': {'modelos': ['gpt-4o-mini', 'gpt-4o', 'o1-mini'], 'chat': ChatOpenAI}}

MEMORIA = ConversationBufferMemory()
MEMORIA.chat_memory.add_user_message('Saudações Oráculo')
MEMORIA.chat_memory.add_ai_message('Saudações')

def carrega_modelo(provedor, modelo, api_key):
     chat = CONFIG_MODELOS[provedor]['chat'](model=modelo, api_key=api_key)
     st.session_state['chat'] = chat

def pagina_chat():
    st.header('🗣️Bem vindo ao Oráculo', divider=True)
   
    memoria = st.session_state.get('mensagens', MEMORIA)    
    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)
     
    input_usuario = st.chat_input('Fale com o Oráculo')
    if input_usuario:
        memoria.chat_memory.add_user_message(input_usuario)
        st.session_state['memoria'] = memoria
        st.rerun()

def sidebar():
    tabs = st.tabs(['Upload de arquivo', 'Selção de Modelo'])
    with tabs[0]:
            tipo_arquivo = st.selectbox('Selecione o tipo de arquivo',TIPOS_ARQUIVOS_VALIDOS)
            if tipo_arquivo == 'Site':
                 arquivo=st.text_input('Digite a URL do site')
            if tipo_arquivo == 'Youtube':
                 arquivo=st.text_input('Digite a URL do vídeo')
            if tipo_arquivo == 'pdf':
                 arquivo=st.file_uploader('Faça o upload do arquivo .pdf', type=['.pdf'])
            if tipo_arquivo == 'csv':
                 arquivo=st.file_uploader('Faça o upload do arquivo .csv', type=['.csv'])
            if tipo_arquivo == 'txt':
                 arquivo=st.file_uploader('Faça o upload do arquivo .txt', type=['.txt'])

    with tabs[1]:
         provedor = st.selectbox('Selecione provedor dos modelos', CONFIG_MODELOS.keys())
         modelo = st.selectbox('Selecione o modelo', CONFIG_MODELOS[provedor]['modelos'])
         api_key = st.text_input(
              f'Adicione uma api key para o provedor {provedor}', 
              value=st.session_state.get(f'api_key_{provedor}'))
         
         st.session_state[f'api_key_{provedor}'] = api_key

    if st.button('Inciar Oráculo', use_container_width=True):
          carrega_modelo(provedor, modelo, api_key)


def main():
     pagina_chat()
     with st.sidebar:
        sidebar()

if __name__ == '__main__':
    main()