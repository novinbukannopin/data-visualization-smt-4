import streamlit as st
import numpy as np
import pandas as pd
# input
st.text_input("Your name", key = "name")
st.write("Welcome to you,", st.session_state.name)

# btn submit
if st.button('Submit'):
    st.write('You have submitted!')
else:
    st.write('Please submit!')

# checkbox
agree = st.checkbox('I agree')
disagree = st.checkbox('I disagree')
if agree:
    st.write('Great!')

# selectbox -> option
skill_option = st.selectbox(
    'Which skill do you most want to learn?',
    ('Java', 'Python', 'C', 'PHP', 'C++', 'Javascript', 'HTML', 'Other'))
st.write('You selected:', skill_option)

# slider
score = st.slider('What is your score?', 0.0, 100.0, (80.0))
st.write('Score:', score)

# sidebar -> selectbox
add_selectbox = st.sidebar.selectbox("Which number do you like?", (10, 20, 30, 40))

df = pd.DataFrame(np.random.randn(10, 3),
                  columns = ('column %d' % col
                             for col in range(3)))
column_left, column_right = st.columns(2)
with column_left:
    st.line_chart(data = df)
with column_right:
    df
#%%
