###########
How to use 
###########


Install Dependencies
**********************

   .. code-block::

      $ pip install -r requirements.txt


Choose news site
**********************
   If you want to bring 'Naver' news through the Naver portal site, use ``news_url_import`` method, 
   otherwise copy and bring the url of the news article you want.

Run code
**********

   * Get urls

   Use the **news_url_import** method to bring news article objects. 
   Set the keyword of the news ``keyword`` and the number of news ``num`` to the parameter value of the method.
   The method returns news articles objects in **dictionary form**.
   You can access the news url using the index and 'url' column name to the desired number of news url like ``news_url = news_dict[2]['url']``.

      .. code-block:: python

         import news_url_import
         keyword = 'gold price'
         num = 10
         dictUrl = news_url_import.news_url_import(keyword, num)

   * Get article texts

   Use the **text_extraction** method to bring news full text.
   The method accesses news articles through ``url`` and returns the full text of the news.
   The full text of the news will be returned in a single paragraph, a form in which the opening text has been removed.

      .. code-block:: python

         import news_text
         url = dictUrl[idx]['url']
         myText = news_text.text_extraction(url)
         print(myText)
  
   * Get keywords
    
   Use the **get_keyword** method to bring news keywords.
   Set the url of the news ``url`` and the language of the news ``ko,en`` to the parameter value of the method.
   Returns 10 keywords based on the frequency of words exposed to the news.

      .. csv-table:: available languages
         :header-rows: 1

         input code, full name
         ko, Korean
         en, English
         ja, Japanese
         zh, Chinese
         es, Spanish
       
      .. code-block:: python

         import news_keyword
            myKeyword = news_keyword.get_keyword(url,'ko')
            print(myKeyword)
       
   * Summarizing news 

   Use the **summarize** method to summarize news text.
   Put the full text of the news article brought in **news_text** method into the **summarize** function.
   It is possible to select how many sentences to summarize through the parameter ``max_sents``.
   (default = 5)

      .. code-block:: python

         import news_summarization
         mySummary = news_summarization.summarize(text=myText, max_sents=5)
     



     