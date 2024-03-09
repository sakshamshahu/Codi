import ollama
import streamlit as st

st.title('Codi: Unminify on command')
st.write('Codi is a simple AI tool to unminify your code. Just paste your minified code and click on the button to unminify it  💻 ⛏️ ')

# if prompt := st.text_area('Paste your minified code here'):
#     with st.spinner('Unminifying your code...'):
#         unminified = ollama.unminify(prompt)
#         st.write(unminified)

if "messages" not in st.session_state: # Initialize state history
    st.session_state["messages"] = []

#model selection
if "model" not in st.session_state:
    st.session_state['model'] = ''

models = [model['name'] for model in ollama.list()['models']]
st.session_state['model'] = st.selectbox('Select model', models)

def model_res_generator():
    stream = ollama.chat(
        model=st.session_state["model"],
        messages=st.session_state["messages"],stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]
        
# Display chat message in history on rerrunning app
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

if prompt := st.chat_input('Whats Up ?'):
    
    st.session_state['messages'].append({'role': 'user', 'content': prompt})
    
    with st.chat_message('user'):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message = st.write_stream(model_res_generator())
        st.session_state["messages"].append({"role": "assistant", "content": message})
        