import streamlit as st
import rag_lib as glib

st.set_page_config(page_title="RAG", page_icon="📚")
st.title("Retrieval-Augmented-Generation")

if 'vector_index' not in st.session_state:
    st.session_state.vector_index = glib.get_index()

input_text = st.text_input("Enter a query")
go_button = st.button("Generate")

if go_button:
    with st.spinner("Generating..."):
        response_content = glib.get_rag_response(
            index=st.session_state.vector_index, question=input_text)
        st.write(response_content)
