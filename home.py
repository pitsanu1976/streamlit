import streamlit as st 

st.set_page_config(
    page_title='Multipage App',
    page_icon="Hi"
)

st.title('Main Page')
st.header('this is the home page')
st.sidebar.success('select a page above')

if "my_input" not in st.session_state:
    st.session_state["my_input"]=""
    
my_input = st.text_input('input a text here',st.session_state["my_input"])
submit = st.button('submit')
if submit:
    st.session_state["my_input"]=my_input
    st.write('You have entered:',my_input)