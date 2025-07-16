from model import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True,index = True,autoincrement=True)
    email = Column(String(50),unique = True,index = True)
    fullname = Column(String(50),unique  = True)
    password = Column(String(50),nullable = False)
    
class UserExtension(Base):
    __tablename__ = 'user_extension'
    id = Column(Integer, primary_key=True,index = True,autoincrement=True)
    university = Column(String(50))
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref="extension",uselist=False)