import streamlit as st 

import pandas as pd

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[7,8,9]]
data1 = pd.DataFrame(a,columns=['a','b','c'])
data2 = pd.DataFrame(b,columns=['a','b','c'])
st.title('Project')

st.header('header for project')

st.write('you enter',st.session_state['my_input'])
c,d = st.columns(2)
with c:
    st.write(data1)
with d:
    st.write(data2)
