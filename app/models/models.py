from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), default="user")
    
    # relationship
    blogs = relationship("Blog", back_populates="creator", cascade="all, delete-orphan", lazy="selectin")
    
    
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    
    # relationship
    creator = relationship("User", back_populates="blogs", lazy="selectin")