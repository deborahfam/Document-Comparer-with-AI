# Document Comparator Tool

An intelligent document comparison tool built with Streamlit and powered by Fireworks.ai for AI-driven analysis.

## Features

- **Multi-format Support**: Compare PDF, DOCX, and TXT documents
- **AI-Powered Analysis**: Uses Fireworks.ai for intelligent difference detection
- **Web Interface**: Clean and intuitive Streamlit-based UI
- **Structured Results**: Organized presentation of document differences
- **History Tracking**: Store and retrieve comparison history (optional)

## Project Structure

```
document-comparator/
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── comparator.py      # Core comparison logic
│   ├── database/
│   │   ├── __init__.py
│   │   └── models.py          # Database models
│   └── utils/
│       ├── __init__.py
│       └── file_processor.py  # File processing utilities
├── data/                      # Local storage directory
├── main.py                    # Streamlit application entry point
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

## Setup Instructions

1. **Clone and Navigate**:
   ```bash
   cd document-comparator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**:
   ```bash
   cp .env.example .env
   # Edit .env file with your Fireworks.ai API key
   ```

4. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

## Environment Variables

Copy `.env.example` to `.env` and configure:

- `FIREWORKS_API_KEY`: Your Fireworks.ai API key
- `FIREWORKS_BASE_URL`: API base URL (default provided)
- `APP_TITLE`: Application title
- `MAX_FILE_SIZE_MB`: Maximum file upload size
- `DEFAULT_MODEL`: LLM model to use

## Usage

1. **Upload Documents**: Use the sidebar to upload your original and updated documents
2. **Supported Formats**: PDF, DOCX, and TXT files are supported
3. **AI Analysis**: The tool will analyze differences using Fireworks.ai
4. **View Results**: Review structured comparison results with highlighted changes

## Development

The application is structured for easy extension:

- **Core Logic**: `app/core/comparator.py` - Main comparison algorithms
- **File Processing**: `app/utils/file_processor.py` - Text extraction utilities
- **Database**: `app/database/models.py` - Optional data persistence
- **UI**: `main.py` - Streamlit frontend

## Dependencies

- **Streamlit**: Web framework for the UI
- **Fireworks.ai**: LLM provider for AI analysis
- **Document Processing**: PyPDF2, python-docx for file handling
- **Database**: SQLAlchemy for optional persistence

## License

MIT License - see repository LICENSE file for details.