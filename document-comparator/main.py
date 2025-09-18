"""
Main entry point for the Document Comparator Streamlit application
"""
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Main application function"""
    st.set_page_config(
        page_title=os.getenv("APP_TITLE", "Document Comparator Tool"),
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("🔍 Document Comparison Tool")
    st.markdown("Compare two versions of a document and analyze key differences using AI")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("Configuration")
        st.info("Upload your documents to get started")
        
        # File upload sections
        st.subheader("📁 Upload Documents")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Original Document**")
            original_file = st.file_uploader(
                "Choose original file",
                type=['pdf', 'docx', 'txt'],
                key="original"
            )
            
        with col2:
            st.write("**Updated Document**")
            updated_file = st.file_uploader(
                "Choose updated file", 
                type=['pdf', 'docx', 'txt'],
                key="updated"
            )
    
    # Main content area
    if original_file and updated_file:
        st.success("✅ Both documents uploaded successfully!")
        
        # Placeholder for comparison logic
        st.subheader("📊 Document Comparison Results")
        st.info("🚧 Comparison functionality will be implemented here")
        
        # Display file information
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Original Document Info:**")
            st.write(f"- Name: {original_file.name}")
            st.write(f"- Size: {original_file.size} bytes")
            st.write(f"- Type: {original_file.type}")
            
        with col2:
            st.write("**Updated Document Info:**")
            st.write(f"- Name: {updated_file.name}")
            st.write(f"- Size: {updated_file.size} bytes")
            st.write(f"- Type: {updated_file.type}")
            
    else:
        st.info("👆 Please upload both documents to start comparison")
        
        # Instructions
        st.subheader("📋 How to use:")
        st.markdown("""
        1. **Upload Documents**: Use the sidebar to upload your original and updated documents
        2. **Supported Formats**: PDF, DOCX, and TXT files
        3. **AI Analysis**: The tool will use Fireworks.ai to analyze differences
        4. **Results**: View structured comparison results with key changes highlighted
        """)

if __name__ == "__main__":
    main()