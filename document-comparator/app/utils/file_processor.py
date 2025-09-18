"""
Utility functions for file processing and text extraction
"""
import os
import io
from typing import Optional
import magic
import PyPDF2
from docx import Document

class FileProcessor:
    """Class for processing different file types"""
    
    @staticmethod
    def get_file_type(file_content: bytes) -> str:
        """Detect file type from content"""
        try:
            return magic.from_buffer(file_content, mime=True)
        except:
            return "application/octet-stream"
    
    @staticmethod
    def extract_text_from_pdf(file_content: bytes) -> str:
        """Extract text from PDF file"""
        try:
            pdf_file = io.BytesIO(file_content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise ValueError(f"Error extracting text from PDF: {str(e)}")
    
    @staticmethod
    def extract_text_from_docx(file_content: bytes) -> str:
        """Extract text from DOCX file"""
        try:
            docx_file = io.BytesIO(file_content)
            doc = Document(docx_file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text.strip()
        except Exception as e:
            raise ValueError(f"Error extracting text from DOCX: {str(e)}")
    
    @staticmethod
    def extract_text_from_txt(file_content: bytes) -> str:
        """Extract text from TXT file"""
        try:
            return file_content.decode('utf-8').strip()
        except UnicodeDecodeError:
            try:
                return file_content.decode('latin-1').strip()
            except Exception as e:
                raise ValueError(f"Error extracting text from TXT: {str(e)}")
    
    @staticmethod
    def extract_text(file_content: bytes, filename: str) -> str:
        """Extract text from file based on extension"""
        file_ext = os.path.splitext(filename.lower())[1]
        
        if file_ext == '.pdf':
            return FileProcessor.extract_text_from_pdf(file_content)
        elif file_ext == '.docx':
            return FileProcessor.extract_text_from_docx(file_content)
        elif file_ext == '.txt':
            return FileProcessor.extract_text_from_txt(file_content)
        else:
            raise ValueError(f"Unsupported file type: {file_ext}")

def validate_file_size(file_size: int, max_size_mb: int = 10) -> bool:
    """Validate file size"""
    max_size_bytes = max_size_mb * 1024 * 1024
    return file_size <= max_size_bytes