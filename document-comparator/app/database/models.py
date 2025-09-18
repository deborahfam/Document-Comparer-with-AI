"""
Database models and operations
"""
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class ComparisonHistory(Base):
    """Model for storing comparison history"""
    __tablename__ = 'comparison_history'
    
    id = Column(Integer, primary_key=True)
    original_filename = Column(String(255), nullable=False)
    updated_filename = Column(String(255), nullable=False)
    comparison_result = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class DatabaseManager:
    """Database manager for the application"""
    
    def __init__(self):
        database_url = os.getenv("DATABASE_URL", "sqlite:///./data/comparator.db")
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
    def create_tables(self):
        """Create all database tables"""
        Base.metadata.create_all(bind=self.engine)
    
    def get_session(self):
        """Get a database session"""
        return self.SessionLocal()
    
    def save_comparison(self, original_filename: str, updated_filename: str, result: str):
        """Save a comparison result to the database"""
        session = self.get_session()
        try:
            comparison = ComparisonHistory(
                original_filename=original_filename,
                updated_filename=updated_filename,
                comparison_result=result
            )
            session.add(comparison)
            session.commit()
        finally:
            session.close()