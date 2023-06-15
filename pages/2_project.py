import streamlit as st 

import pandas as pd

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[10,11,12]]
data1 = pd.DataFrame(a,columns=['a','b','c'])
data2 = pd.DataFrame(b,columns=['a','b','c'])
st.title('Project')

st.header('header for project')


c,d = st.columns(2)
with c:
    st.header('data1')
    st.write(data1)
with d:
    st.header('data2')
    st.write(data2)
