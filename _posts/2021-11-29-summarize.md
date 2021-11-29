---
title:  "Features: Summarize"
search: false
categories: 
  - Features
last_modified_at: 2021-11-29T08:05:34-05:00
---

**Summarize** is a function that summarizes the text of a news article. This function is a key function of **SqueezeNews**. You can simply summarize the news that is too long to read. `Text` can be extracted through the **text_extraction** function.

```yaml
news_summarization.summarize(text, max_sents)
```

Use the **summarize** method to summarize news text. Put the full text of the news article brought in **text_extraction** method into the **summarize** function. It is possible to select how many sentences to summarize through the parameter `max_sents`. (default = 5)
