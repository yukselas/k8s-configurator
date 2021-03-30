from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base declarative_base()

class Pods(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True) # name bos birakilabilir
    version = Column(Integer)

engine = create_engine('sqlite:///ks8_configurator.db')

Base.metadata.create_all(engine)