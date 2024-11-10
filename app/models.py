from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    department = Column(String)
    access_level = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String)
    resource = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String)

class DocumentMetadata(Base):
    __tablename__ = "document_metadata"
    id = Column(Integer, primary_key=True)
    source_system = Column(String)
    original_path = Column(String)
    last_updated = Column(DateTime)
    version = Column(String)
    department = Column(String)
    access_level = Column(Integer)