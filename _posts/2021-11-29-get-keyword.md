---
title:  "Features: Get Keyword"
search: false
categories: 
  - Features
last_modified_at: 2021-11-29T08:05:34-05:00
---

**Get_keyword** is a function of extracting keywords for news articles through url addresses. You can get the address yourself or extract `url` using the **news_url_import** function.

```yaml
news_keyword.get_keyword(url,'ko')
```

**Note:** There are a total of five languages available. `ko``en``ja``zh``es`
{: .notice--info}


Use the get_keyword method to bring news keywords. Set the url of the news `url` and the language of the news `ko`,`en` to the parameter value of the method. Returns 10 keywords based on the frequency of words exposed to the news.

