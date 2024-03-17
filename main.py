import streamlit as st

def main():
    st.set_page_config(page_title="Ask your csv")
    st.header("Ask your csv")

    user_csv = st.file_uploader("upload your CSV file", type="csv")

