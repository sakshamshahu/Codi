import ollama
import streamlit as st

st.title('Codi: Unminify on command')
st.write('Codi is a simple AI tool to unminify your code. Just paste your minified code and click on the button to unminify it  💻 ⛏️ ')

if prompt := st.text_area('Paste your minified code here'):
    with st.spinner('Unminifying your code...'):
        unminified = ollama.unminify(prompt)
        st.write(unminified)