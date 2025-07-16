from model import Base
from sqlalchemy import create_engine,Integer,String,Column,Text,ForeignKey
from sqlalchemy.orm import relationship

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True,index = True)
    name = Column(String(50),unique = True)
    articles = relationship("Article", secondary="article_tag",back_populates="tag",lazy="dynamic")
    
class Airticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True,index = True)
    title=Column(String(50),nullable=False)
    content=Column(Text,nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship("User", backref="articles")
    tags=relationship("Tag", secondary="article_tag",back_populates="articles",lazy="dynamic")
    
class AriticleTag(Base):
    __tablename__ = 'article_tag'
    id = Column(Integer, primary_key=True,index = True)
    article_id = Column(Integer, ForeignKey('article.id'),primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'),primary_key=True)