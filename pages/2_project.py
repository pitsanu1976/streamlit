import streamlit as st 

import pandas as pd

a = [[1,2,3],[4,5,6],[7,8,9]]
data = pd.DataFrame(a,columns=['a','b','c'])

st.title('Project')

st.header('header for project')

st.write('you enter',st.session_state['my_input'])

st.write(data)