# SqueezeNews 📖

<p align="center"><b> 🇺🇸 English</b> |    <a href="https://github.com/rmakerck37/SqueezeNews/blob/main/README_ko.md"> 🇰🇷 한국어</a><p>
In today's modern society, a large amount of news is poured out in various fields such as politics, the economy, and society. There is no time to read all these vast amounts of news accumulated every day.
A function that summarizes only the core of the article and shows it at a glance can save time for busy modern people and it will help them easily identify trends.

# Dependencies 🌏
- [Python 3.8.2](https://www.python.org/downloads/release/python-382/)
- [Newspaper3k 0.2.8](https://github.com/codelucas/newspaper)
- [nltk 3.6.5](https://www.nltk.org/)
- [beautifulsoup 4.8.1](https://beautiful-soup-4.readthedocs.io/en/latest/)

# Mission Statement 📝
The ‘SqueezeNews’ project develops open-source software for extracting and curating articles.
The ‘SqueezeNews’  allows for extracting articles using python web-crawling.
It is designed to easily bring up the full text and keywords of news articles.
Also, it provides various visual data(e.g. word cloud, graphs) according to the frequency of keywords.

# Feature List 📋
  - Brings up the full text of news articles.
  
  - Summarizes articles and extracting keywords.
  
  - (planned) Creates a word cloud according to the frequency of keywords.
  
  - (planned) Search for similar articles.
  
  - (planned) Analysis of news article tendency according to positive or negative word ratio.

# Target Development Language
Python .

# How to use
### 1. Clone GitHub repository
  ```
  https://github.com/rmakerck37/SqueezeNews.git
  ```
  
### 2. Install Dependencies
  ```
  pip install -r requirements.txt
  ```

### 3. Run code
  
  - Get urls
  ```python
  import news_url_import
  
  keyword = '금값'
  num = 10
  dictUrl = news_url_import.news_url_import(keyword, num)
 
  ```
  
  - Get article texts
  ```python
  import news_text
  
  url = dictUrl[0]['url']
  myText = news_text.text_extraction(url)
  print(myText)
  ```
  
  - Get keywords
  ```python
  import news_keyword
  
  myKeyword = news_keyword.get_keyword(url,'ko')
  print(myKeyword)
  
  ```
  
  - Summarizing news
  ```python
  import news_summarization
  
  mySummary = news_summarization.summarize(text=myText, max_sents=5)
 
  ```
 
  # License
  Copyright © 2021 [rmakerck37](https://github.com/rmakerck37).
  
  This project is available under the [Apache-2.0 License](https://github.com/rmakerck37/SqueezeNews/blob/main/LICENSE).
