# parsing

# input: dict obj
# output: 140자로 줄여진 책정보 (트윗에 업로드 할 것)
def parse(book):
    
    # 140자로 줄이기
    # 트위터 spec 상 링크가 23자로 줄여지기 때문에 일단은 초과하지 않는다고 판단함
    
    result = book["title"] + "\n" + book["author"] + "\n" + book["publisher"] + "\n" + book["pubDate"] + "\n" + book["link"]
    print("파싱결과 @@@@ \n" + result + "\n@@@@결과끝")
    
    return result
