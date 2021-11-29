---
title:  "Features: Text Extraction"
search: false
categories: 
  - Features
last_modified_at: 2021-11-29T08:05:34-05:00
---

**Text_extraction** is a function of extracting text from news articles through url addresses. You can get the address yourself or extract `url` using the **news_url_import** function.

```yaml
news_text.text_extraction(url)
```

Use the **text_extraction** method to bring news full text. The method accesses news articles through `url` and returns the full text of the news. The full text of the news will be returned in a single paragraph, a form in which the opening text has been removed.