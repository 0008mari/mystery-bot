# dao - db접근 

import sqlite3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key = True)
    title = Column(String(50))
    author = Column(String(20))
    pubDate = Column(String(11))
    publisher = Column(String(10))
    link = Column(String(100))
    
def dao():
    engine = create_engine('sqlite:///books.db', echo=True)

    Book.__table__.create(bind=engine, checkfirst=True)
    
    # Session 생성
    Session = sessionmaker(bind=engine)
    session = Session()
    
    book_list=Book(id=296918869, title='5인의 목격자', author='ddd', pubDate='2310', publisher='하빌리스', link='http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=296918869&amp;partner=openAPI&amp;start=api')

    session.add(book_list)
    session.commit()
    
    

# dao()