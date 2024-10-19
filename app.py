
import streamlit as st
from services.qdrant_service import QdrantService
from services.anthropic_service import AnthropicService

# Set up Streamlit app
st.title("Bank Statement Analyzer")

documents = """
Pinnacle
Date: 6/30/22
Balance Summary
...
"""

# Sidebar for data available
st.sidebar.header("Available Data")
st.sidebar.code(documents)

# User inputs
collection_name = st.text_input("Enter the Collection Name:")
query_text = st.text_area("Enter the stuff you're looking for:", height=100)
description = ""
user_query = st.text_area("Enter your Query from that stuff:", height=100)

# Process the bank statements and handle search
if st.button("Submit"):
    if collection_name and query_text:
        # Initialize Qdrant service
        qdrant_service = QdrantService(collection_name, documents)
        hits, extracted_content = qdrant_service.process_query(query_text, description)

        if extracted_content:
            st.subheader("Extracted Content:")
            st.code(extracted_content)

            # Initialize Anthropic service
            anthropic_service = AnthropicService()
            analysis_result = anthropic_service.extract_bank_statements(documents, extracted_content, user_query)

            st.subheader("Analysis Result:")
            st.write(analysis_result)
        else:
            st.warning("No relevant content found for the given query.")
    else:
        st.error("Please provide both the Collection Name and Query Text.")
