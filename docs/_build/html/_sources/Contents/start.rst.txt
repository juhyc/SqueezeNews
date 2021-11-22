##########################################
Getting start - Installation
##########################################

SqueezeNews📰 is tested on Python 3.7+. Follow the installation process.


Installation with pip
******************************

SqueezeNews can be installed using pip as follows:

.. code-block:: winbatch

    $pip install SqueezeNews

- testing example

.. code-block:: python

    from SqueezeNews.function import news_text

-----------------------------------------------------------------    

Installation with Jupyter Notebook
*************************************

Please download the .py file from the github website. 

   https://github.com/rmakerck37/SqueezeNews


1. Please click the .py file button.

.. image:: images/first.JPG

2. Please click the Raw button.

.. image:: images/second.JPG

3. Please download the file through 'ctrl + s'.

.. image:: images/third.JPG

4. Please download all files through the following process.

This method requires Jupyter Notebook and Anaconda environment.

.. image:: images/fourth.JPG
.. image:: images/fifth.JPG

Put all .py files in a sub-folder of the currently running code.

------------------------------------------------------------------    

Testing your installation
********************************

That’s all! You can check that SqueezeNews is correctly installed by starting up python.
Enter the news url link in :class:`url` variable.

- testing example

.. code-block:: python

    from function.news_text import text_extraction
    from function.news_summarization import summarize
    from function.news_keyword import get_keyword
    from function.news_url_import import news_url_import

.. warning :: 
  If you have a **lookup error**, run the following process.

.. code-block:: python

    import nltk
    nltk.download('punkt')

.. code-block:: python

    url = ''
    text = text_extraction(url)
    summarize(text)
    get_keyword(url, 'en')