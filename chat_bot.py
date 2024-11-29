import streamlit as st
from google import generativeai as genai
# from google.generativeai import ChatSession
from langchain_google_genai import ChatGoogleGenerativeAI
import os


def get_docs(st_files, dir_path: str | None= r'./'):
    _docs = []
    for _file in st_files:
        f_path = fr'{dir_path}/{_file.name}'
        with open(f_path, 'wb')as f:
            f.write(_file.read())
            f.close()
        _docs.append(genai.upload_file(f_path))
        os.remove(f_path)
    return _docs


os.environ["GOOGLE_API_KEY"] = st.secrets.GOOGLE_API_KEY
genai.configure(api_key=st.secrets.GOOGLE_API_KEY)

st.title('💬 Chatbot')
if 'llm' not in st.session_state:
    # st.session_state['llm'] = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest')
    st.session_state['llm'] = ChatGoogleGenerativeAI(model='gemini-pro')

if 'chat' not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-flash')
    history = [{'role': 'model', 'parts': 'How can I help you?'}]
    st.session_state['chat'] = model.start_chat(history=history)

if 'messages' not in st.session_state:
    st.session_state['messages'] = st.session_state['chat'].history

if 'doc_names' not in st.session_state:
    st.session_state['doc_names'] = []

for msg in st.session_state['messages']:
    with st.chat_message(msg.role if msg.role =='user' else 'ai'):
        for part in msg.parts:
            st.write(part.text)
    # st.chat_message(msg.role if msg.role =='user' else 'ai').write(msg.parts)

llm = st.session_state['llm']
chat = st.session_state['chat']
_docs = st.session_state.get('_docs')
    
if prompt := st.chat_input():
    st.chat_message('user').write(prompt)
    if _docs:
        response = chat.send_message([prompt, *_docs], stream=True)
    else:
        response = chat.send_message(prompt, stream=True)
    # response = model.generate_content(prompt, stream=True)
    with st.chat_message('ai'):
        for chunk in response:
            msg = chunk.text
            st.write(msg)
    st.session_state['messages'] = chat.history

u_files = st.file_uploader('Upload a file', accept_multiple_files=True)
# {u_file.name: u_file.read() for u_file in u_files}
doc_names = [f.name for f in u_files]
if st.session_state['doc_names'] != doc_names:
    st.session_state['doc_names'] = doc_names
    st.session_state['_docs'] = get_docs(u_files)
