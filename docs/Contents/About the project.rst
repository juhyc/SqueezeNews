####################
About the project
####################

Introduction
================

How much news do we read a day?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In today's modern society, a large amount of news is pouring out in various fields such as politics, economy, and society due to the rapidly developing Internet.
Among them, it is not easy to notice what today's core news is, what the overall social situation is, and what the trend was this week.
It also takes quite a long time to re-read the news article that I missed that day.

Therefore, not only is it difficult to understand the vast amount of news accumulated every day, but it also lacks time to read the news.
Then, how can we efficiently manage vast amounts of news in a complex modern society?

* If there was a function that summarized only the core of the article and showed it at a glance, it would help busy modern people save time.
* It also would help me easily grasp the news trend of the day.



How can it be useful?
==========================
`SqueezeNews` uses the Python web crawling function, which brings in the full text of news articles through links to news that want a quick core summary to help summarize articles and extract key keywords.

Through this, you will be able to easily find out the core of the article anytime, anywhere by collecting only links to news articles you are interested in.

In addition, we will add several more features for an efficient summary of news articles.

1. Provide **wordcloud** [#f1]_ function that visually stands out key words so that you can intuitively grasp keywords and concepts of documents.
2. Search articles **similar** to news articles you're interested in.
3. Provide analysis of news article **tendency** according to positive/negative word ratio.

.. rubric:: Footnotes

.. [#f1] Depending on the frequency of keywords, the more frequently mentioned words are expressed in a larger size so that they can be seen at a glance.
