import newspaper
from newspaper import Article
from newspaper.api import languages
import nltk
nltk.download('punkt')

# 단어의 빈도수를 기반으로 10개의 키워드를 반환.

def get_keyword(url, language):
    article = Article(url, language = language)
    article.download()
    article.parse()
    article.nlp()

    keywords = article.keywords
    return keywords[:10]

#test
# mykeyword = news_keyword('https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=417&aid=0000749254','ko')
# print(mykeyword)

