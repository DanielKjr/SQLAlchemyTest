from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DECIMAL, Integer, String, DateTime

Base = declarative_base()

class Classes(Base):
    __tablename__ = 'Classes' 
    # __table_args__ = {'schema': 'dbo'}
    BasicClassId = Column(Integer, primary_key=True)
    TestField = Column(String)
    Refnr = Column(DECIMAL)  
    Oprettet = Column(DateTime)

