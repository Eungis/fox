from fox.tasks.base.mecab import KoMecabTokenizer

tokenizer = KoMecabTokenizer()
print(tokenizer.pos("안녕하세요. 저는 한국인입니다."))