---
title:  "Features: News URL Import"
search: false
categories: 
  - Features
last_modified_at: 2021-11-29T08:05:34-05:00
---

**news_url_import** can extract the url address of the news article using keyword search. This function has the advantage of being very convenient to extract url without copying the address directly.


```yaml
news_url_import.news_url_import(keyword, num)
```

Use the **news_url_import** method to bring news article objects. Set the keyword of the news keyword and the number of news `num` to the parameter value of the method. The method returns news articles objects in dictionary form. You can access the news url using the index and 'url' column name to the desired number of news url like `news_url = news_dict[2]['url']`.