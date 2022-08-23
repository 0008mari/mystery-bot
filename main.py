# main

from request import *
from parse import *
from upload import *

from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    uid = Column(Integer, primary_key = True)
    title = Column(String(50))
    author = Column(String(20))
    pubDate = Column(String(11))
    publisher = Column(String(10))
    link = Column(String(100))

def main():

    print("---봇 기동---")
    
    raw = request()
    
    # raw 가공
    books = []
    for book in raw['item']:
        print(book)
        tmp = json.dumps(book)
        books.append(book)
    
    #### 여기서부터 db 연결 코드
    engine = create_engine('sqlite:///books.db', echo=True)
    Book.__table__.create(bind=engine, checkfirst=True)
    
    # Session 생성
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for book in books:
        # 중복 체크
        stmt = select(Book).where(Book.uid == book["itemId"])
        result = session.execute(stmt)
        
        # 중복 아니면
        if result.first() == None:
            # 객체 생성
            book_obj = Book(uid=book["itemId"], title=book["title"], author=book["author"], pubDate=book["pubDate"], publisher=book["publisher"], link=book["link"])
            # db에 삽입
            session.add(book_obj)
            
            # 정보를 140자에 꾸겨넣기
            text_140 = parse(book)
            # 책 하나 트윗하기
            upload(text_140)
        else: 
            print("중복임 ㅅㄱ")
            
        # db 연결 끝
        session.commit()
    # 끝
        
    print("---봇 작업 성공적으로 마침---")
    return 0

main()
    