# SqueezeNews 📖

<p align="center"><a href="https://github.com/rmakerck37/SqueezeNews">🇺🇸 English</a> |    <b>🇰🇷 한국어</b><p>
오늘날의 현대 사회에서는 정치, 경제, 그리고 사회와 같은 다양한 분야에서 많은 양의 뉴스가 쏟아진다. 사람들은 매일 축적되는 방대한 양의 뉴스를 전부 읽을 시간이 없다.
기사의 핵심만 요약해 한눈에 보여주는 기능은 바쁜 현대인들에게 시간을 절약할 수 있고 트렌드를 쉽게 파악할 수 있도록 도와줄 것이다.



# Dependencies 🌏
- [Python 3.8.2](https://www.python.org/downloads/release/python-382/)
- [Newspaper3k 0.2.8](https://github.com/codelucas/newspaper)
- [nltk 3.6.5](https://www.nltk.org/)
- [beautifulsoup 4.8.1](https://beautiful-soup-4.readthedocs.io/en/latest/)

# Mission Statement 📝
'SqueezeNews' 프로젝트는 기사를 추출하고 큐레이팅하기 위한 오픈 소스 소프트웨어를 개발한다.
'SqueezeNews'는 파이썬 웹 크롤링을 사용하여 기사를 추출할 수 있다.
그것은 뉴스 기사의 전문과 키워드를 쉽게 불러올 수 있도록 고안되었다.
또한 키워드 빈도에 따라 다양한 시각 데이터(예: 워드 클라우드, 그래프)를 제공한다.

# Feature List 📋
· 뉴스 기사 전문 수집

· 기사 요약 및 키워드 추출

· (예정) 키워드의 빈도에 따른 워드 클라우드 생성

· (예정) 유사한 기사 검색

· (예정) 긍정 및 부정 단어 비율에 따른 기사 경향 분석

# Target Development Language
Python .

# How to use ✍️
### 1. GitHub repository 복제
  ```
  https://github.com/rmakerck37/SqueezeNews.git
  ```
  
### 2. Dependencies 설치
  ```
  pip install -r requirements.txt
  ```
  
### 3. 코드 실행
  
  - ur 가져오기
  ```python
  import news_url_import
  
  keyword = '금값'
  num = 10
  dictUrl = news_url_import.news_url_import(keyword, num)
 
  ```
  
  - 기사 전문 불러오기
  ```python
  import news_text
  
  url = dictUrl[0]['url']
  myText = news_text.text_extraction(url)
  print(myText)
  ```
  - 키워드 추출
  ```python
  import news_keyword
  
  myKeyword = news_keyword.get_keyword(url,'ko')
  print(myKeyword)
  
  ```
  - 기사 요약
  ```python
  import news_summarization
  
  mySummary = news_summarization.summarize(text=myText, max_sents=5)
 
  ```
 
  # License 🚩
  Copyright © 2021 [rmakerck37](https://github.com/rmakerck37).
  
  이 프로젝트는 [Apache-2.0 License](https://github.com/rmakerck37/SqueezeNews/blob/main/LICENSE)와 함께합니다.
