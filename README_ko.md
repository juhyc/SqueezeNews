# SqueezeNews π

<p align="center"><a href="https://github.com/rmakerck37/SqueezeNews">πΊπΈ English</a> |    <b>π°π· νκ΅­μ΄</b><p>
μ€λλ μ νλ μ¬νμμλ μ μΉ, κ²½μ , κ·Έλ¦¬κ³  μ¬νμ κ°μ λ€μν λΆμΌμμ λ§μ μμ λ΄μ€κ° μμμ§λ€. μ¬λλ€μ λ§€μΌ μΆμ λλ λ°©λν μμ λ΄μ€λ₯Ό μ λΆ μ½μ μκ°μ΄ μλ€.
κΈ°μ¬μ ν΅μ¬λ§ μμ½ν΄ νλμ λ³΄μ¬μ£Όλ κΈ°λ₯μ λ°μ νλμΈλ€μκ² μκ°μ μ μ½ν  μ μκ³  νΈλ λλ₯Ό μ½κ² νμν  μ μλλ‘ λμμ€ κ²μ΄λ€.



# Dependencies π
- [Python 3.8.2](https://www.python.org/downloads/release/python-382/)
- [Newspaper3k 0.2.8](https://github.com/codelucas/newspaper)
- [nltk 3.6.5](https://www.nltk.org/)
- [beautifulsoup 4.8.1](https://beautiful-soup-4.readthedocs.io/en/latest/)

# Mission Statement π
'SqueezeNews' νλ‘μ νΈλ κΈ°μ¬λ₯Ό μΆμΆνκ³  νλ μ΄ννκΈ° μν μ€ν μμ€ μννΈμ¨μ΄λ₯Ό κ°λ°νλ€.
'SqueezeNews'λ νμ΄μ¬ μΉ ν¬λ‘€λ§μ μ¬μ©νμ¬ κΈ°μ¬λ₯Ό μΆμΆν  μ μλ€.
κ·Έκ²μ λ΄μ€ κΈ°μ¬μ μ λ¬Έκ³Ό ν€μλλ₯Ό μ½κ² λΆλ¬μ¬ μ μλλ‘ κ³ μλμλ€.
λν ν€μλ λΉλμ λ°λΌ λ€μν μκ° λ°μ΄ν°(μ: μλ ν΄λΌμ°λ, κ·Έλν)λ₯Ό μ κ³΅νλ€.

# Feature List π
Β· λ΄μ€ κΈ°μ¬ μ λ¬Έ μμ§

Β· κΈ°μ¬ μμ½ λ° ν€μλ μΆμΆ

Β· (μμ ) ν€μλμ λΉλμ λ°λ₯Έ μλ ν΄λΌμ°λ μμ±

Β· (μμ ) μ μ¬ν κΈ°μ¬ κ²μ

Β· (μμ ) κΈμ  λ° λΆμ  λ¨μ΄ λΉμ¨μ λ°λ₯Έ κΈ°μ¬ κ²½ν₯ λΆμ

# Target Development Language
Python .

# How to use βοΈ
### 1. GitHub repository λ³΅μ 
  ```
  https://github.com/rmakerck37/SqueezeNews.git
  ```
  
### 2. Dependencies μ€μΉ
  ```
  pip install -r requirements.txt
  ```
  
### 3. μ½λ μ€ν
  
  - ur κ°μ Έμ€κΈ°
  ```python
  import news_url_import
  
  keyword = 'κΈκ°'
  num = 10
  dictUrl = news_url_import.news_url_import(keyword, num)
 
  ```
  
  - κΈ°μ¬ μ λ¬Έ λΆλ¬μ€κΈ°
  ```python
  import news_text
  
  url = dictUrl[0]['url']
  myText = news_text.text_extraction(url)
  print(myText)
  ```
  - ν€μλ μΆμΆ
  ```python
  import news_keyword
  
  myKeyword = news_keyword.get_keyword(url,'ko')
  print(myKeyword)
  
  ```
  - κΈ°μ¬ μμ½
  ```python
  import news_summarization
  
  mySummary = news_summarization.summarize(text=myText, max_sents=5)
 
  ```
 
  # License π©
  Copyright Β© 2021 [rmakerck37](https://github.com/rmakerck37).
  
  μ΄ νλ‘μ νΈλ [Apache-2.0 License](https://github.com/rmakerck37/SqueezeNews/blob/main/LICENSE)μ ν¨κ»ν©λλ€.
