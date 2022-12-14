# webscraper_pandas
This is a table that is automatically scraped using pandas.  After printing the "scraper" object it resulted in a URL error, related to SSL certificate. This error was fixed by importing SSL. For the next step, I was getting too much information with the code selecting almost all the tables appearing on the page. I decided to narrow down the list to clean it up a bit. Instead of printing "scraper", I simply typed

"for idx, table in enumerate(scraper):

Next, I printed the separator with a bunch of  "*******" using a very long line 
print(idx)
print(table)

After re-running the code again with shift+ENTER the table I was interested in was the "distribution table" under index 3.

To select it, I entered "scraper[3]" 

Ran the cell, with a beautiful, extra organize pandas data frame with all of the values I wanted to select.

Using pandas, not only did I discover saving a little time, it seemed to of made the code more reliable. Selecting the entire table, instead of individual items from the table of data. 
