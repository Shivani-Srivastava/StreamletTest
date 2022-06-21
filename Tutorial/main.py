'''

Streamlit Demo Application - Word Embeddings

Shivani Srivastava

'''

import streamlit as st

st.title('Welcome to Streamlit')

st.write('You can toggle which page to select using the column on the left side.')

st.write('The app has different pages, or tabs, with different uses and different inputs, but also persisting inputs.')



user = st.text_input('For instance, enter your name here:')

st.write('This will be stored to your local machine till you refresh this web-page.')

update = st.button('update user')

if 'user' not in st.session_state:
    st.session_state['user'] = user

if update:
    st.session_state['user'] = user

    
st.sidebar.write(f"hello {st.session_state['user']}")

st.write(st.session_state)



