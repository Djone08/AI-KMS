import streamlit as st
from google import generativeai as genai


# with st.sidebar:
#     '[Get an Gemini API key](https://aistudio.google.com/apikey)'
#     '[View the source code](https://github.com/Djone08/AI-KMS)'

st.title('💬 Chatbot')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role': 'model', 'parts': 'How can I help you?'}]

for msg in st.session_state.messages:
    st.chat_message(msg['role'] if msg['role']=='user' else 'ai').write(msg['parts'])

if prompt := st.chat_input():

    genai.configure(api_key=st.secrets.GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=st.session_state['messages'])
    print(st.session_state.messages)
    

    st.session_state.messages.append({'role': 'user', 'parts': prompt})
    st.chat_message('user').write(prompt)
    response = chat.send_message(prompt, stream=True)
    # response = model.generate_content(prompt, stream=True)
    with st.chat_message('ai'):
        for chunk in response:
            msg = chunk.text
            st.write(msg)
        try:
            st.session_state.messages.append({'role': 'model', 'parts': response.text})
        except ValueError:
            print('='*100)
            print(response)
