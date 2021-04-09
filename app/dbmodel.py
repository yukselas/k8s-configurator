
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy import create_engine


db = SQLAlchemy(app)

class isimModule(db.Model):
    id = Column(Integer, primary_key=True)
    name=  Column(String(250), nullable=True) # name bos birakilabilir
    val= Column(Text , nullable=True) # name bos birakilabilir
    defaultval = Column(String(250), nullable=True)
    def __repr__(self):
        return '<Name %r>' % self.name        




class k8sconfig(db.Model):
    name = Column(String(250), primary_key=True) # name bos birakilabilir
    config = Column(Text , nullable=True) # name bos birakilabilir
    version = Column(Integer)
    default = Column(Integer)
    def __repr__(self):
        return '<Name %r>' % self.name    


db.create_all()








