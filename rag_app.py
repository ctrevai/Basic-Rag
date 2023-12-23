import streamlit as st
import rag_lib as glib

st.set_page_config(page_title="RAG", page_icon="📚")
st.title("Retrieval-Augmented-Generation")

uploaded_file = st.file_uploader("Upload a pdf file", type=["pdf"])

if uploaded_file:
    if 'has_document' not in st.session_state:
        upload_button = st.button("Upload")

        if upload_button:
            with st.spinner("Uploading..."):
                upload_reponse = glib.save_file(
                    file_bytes=uploaded_file.getvalue())
                st.success(upload_reponse)
                st.session_state.has_document = True
            with st.spinner("Indexing..."):
                st.session_state.vector_index = glib.get_index()
            glib.last_uploaded_file = uploaded_file.name
    else:
        if uploaded_file.name != glib.last_uploaded_file:
            upload_button = st.button("Upload")

            if upload_button:
                with st.spinner("Uploading..."):
                    upload_reponse = glib.save_file(
                        file_bytes=uploaded_file.getvalue())
                    st.success(upload_reponse)
                    st.session_state.has_document = True

                with st.spinner("Indexing..."):
                    st.session_state.vector_index = glib.get_index()
                glib.last_uploaded_file = uploaded_file.name

    if 'vector_index' in st.session_state:
        if uploaded_file.name != glib.last_uploaded_file:
            st.write("please click upload to upload the new pdf.")
        else:
            input_text = st.text_input("Enter a query about " +
                                       uploaded_file.name)
            go_button = st.button("Generate")

            if go_button:
                with st.spinner("Generating..."):
                    response_content = glib.get_rag_response(
                        index=st.session_state.vector_index, question=input_text)
                    st.write(response_content)
else:
    st.write("No file uploaded yet.")
