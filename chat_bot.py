import streamlit as st
from google import generativeai as genai
from google.api_core.exceptions import InvalidArgument
from streamlit.runtime.uploaded_file_manager import UploadedFile
import os


def get_docs(st_files: list[UploadedFile], dir_path: str | None='temp_upload_files',
             clear_files: bool | None=True) -> list:
    _docs = []
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    for _file in st_files:
        f_path = fr'{dir_path}\{_file.name}'
        with open(f_path, 'wb')as f:
            f.write(_file.read())
            f.close()
        try:
            _docs.append(genai.upload_file(f_path))
        except ValueError as e:
            st.error(f'''Unsupported File Type Please Remove (`{_file.name}`)
                     \nError:
                     
                     {e}''', icon=':material/error:')
            print(type(e))
        finally:
            if clear_files:
                os.remove(f_path)
    return _docs


os.environ["GOOGLE_API_KEY"] = st.secrets.GOOGLE_API_KEY
genai.configure(api_key=st.secrets.GOOGLE_API_KEY)

st.title('💬 Chatbot')

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

chat = st.session_state['chat']
docs = st.session_state.get('docs')
    
if prompt := st.chat_input():
    st.chat_message('user').write(prompt)

    try:
        new_prompt = [prompt, *docs] if docs else prompt
        response = chat.send_message(new_prompt, stream=True)

        with st.chat_message('ai'):
            for chunk in response:
                msg = chunk.text
                st.write(msg)

    except InvalidArgument as e:
        reason = 'Invalid File Formats or Unsupported Documents causes this Error!' if e.code==400 else ''
        error = f'''Error Message:

        {e.__class__.__name__}: {e}
{reason}'''
        st.error(error, icon=':material/error:')

    st.session_state['messages'] = chat.history

u_files = st.file_uploader('Upload a file', accept_multiple_files=True)
doc_names = [f.name for f in u_files]

if st.session_state['doc_names'] != doc_names:
    st.session_state['doc_names'] = doc_names
    st.session_state['docs'] = get_docs(u_files)
