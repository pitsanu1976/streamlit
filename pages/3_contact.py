import streamlit as st 
import openai
st.title('contact')
openai.api_key = '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'

def openai_chat(prompt):
    completions = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        temperature = 0.8
    )
    message = completions.choices[0].text 
    return message.strip()

prompt_text = st.input_text('enter prompt:')
st.write(openai_chat(prompt_text))