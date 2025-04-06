from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DECIMAL, Integer, String, DateTime

Base = declarative_base()

class Classes(Base):
    __tablename__ = 'Classes' 

    BasicClassId = Column(Integer, primary_key=True)
    TestField = Column(String)
    Refnr = Column(DECIMAL)  
    Oprettet = Column(DateTime)

    def __init__(self, BasicClassId, TestField, Refnr, Oprettet):
        self.BasicClassId = BasicClassId
        self.TestField = TestField
        self.Refr = Refnr
        self.Oprettet = Oprettet