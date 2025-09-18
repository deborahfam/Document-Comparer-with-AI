# Quick Start Guide

## 🚀 Getting Started with Document Comparator

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd document-comparator
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and add your Fireworks.ai API key:
   ```
   FIREWORKS_API_KEY=your_actual_api_key_here
   ```

5. **Run the application**:
   ```bash
   streamlit run main.py
   ```

6. **Open your browser** to `http://localhost:8501`

### First Use

1. Upload two documents (original and updated versions)
2. Supported formats: PDF, DOCX, TXT
3. Click compare to see AI-powered analysis
4. Review the structured differences and summary

### Troubleshooting

- **Import errors**: Make sure all dependencies are installed (`pip install -r requirements.txt`)
- **API errors**: Verify your Fireworks.ai API key in the `.env` file
- **File upload issues**: Check file size limits in your `.env` configuration

### Next Steps

- Customize the UI in `main.py`
- Extend comparison logic in `app/core/comparator.py`
- Add new file types in `app/utils/file_processor.py`
- Set up database persistence using `app/database/models.py`