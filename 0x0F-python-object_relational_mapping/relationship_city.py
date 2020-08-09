#!/usr/bin/python3
"""
defines City class that inherits from Base = declarative_base()
and links to MySQL table cities using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    defines City class that links to MySQL table 'cities'
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
