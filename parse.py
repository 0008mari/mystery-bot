# parsing

# input: dict obj
# output: 140자로 줄여진 책정보 (트윗에 업로드 할 것)
def parse(book):
    
    # 140자로 줄이기
    # 근데 링크가 23자로 축소됨? 그냥 안줄이고 가보자고 ㅋㅋ 
    
    result = book["title"] + "\n" + book["author"] + "\n" + book["publisher"] + "\n" + book["pubDate"] + "\n" + book["link"]
    print("파싱결과 @@@@ \n" + result + "\n@@@@결과끝")
    
    return result