import scrapy  # framework
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup  # Extract data from html files
import pandas as pd

pd.set_option('display.max_columns', None)

url_soup = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url_soup)

soup = BeautifulSoup(html, 'lxml')  # lxml API for parsing XML and HTML
title = soup.title
text = soup.get_text()
all_hyperlink = soup.find_all('a')

all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))

# convert website table to df
rows = soup.find_all('tr')
list_rows = []
for row in rows:
    row_td = row.find_all('td')
    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    list_rows.append(cleantext)
df = pd.DataFrame(list_rows)
df = df[0].str.split(',', expand=True)
df[0] = df[0].str.strip('[')

# To find table heading
col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
# convert the list of heading into dataframe
df_col = pd.DataFrame(all_header)
df_col_name = df_col[0].str.split(',', expand=True)

# concat the two df
frames = [df_col_name, df]
df_w_cols_name = pd.concat(frames)
df_w_dup_cols = df_w_cols_name.rename(columns=df_w_cols_name.iloc[0])
df_w_cols = df_w_dup_cols.drop(df_w_dup_cols.index[0])
df_w_cols_wo_na = df_w_cols.dropna(axis=0, how='any')
df_w_cols_wo_na.rename(columns={'[Place': 'Place'}, inplace=True)
df_w_cols_wo_na.rename(columns={' Team]': 'Team'}, inplace=True)
df_w_cols_wo_na['Team'] = df_w_cols_wo_na['Team'].str.strip(']')
print(df_w_cols_wo_na.head(1))

# response move between website when scraping
# response keep track of the URL within the response url variable
# lets us follow a new link with the follow() method


html = '''
<html>
    <body>
        <div class="hello data camp">
            <p>Hello World!</p>
        </div>
        <p>Enjoy DataCamp!</p>
    </body>
</html>
'''

# <xpath-to-element>/@attr-name
# ie. //div[@id="uid"]/a/@href
# Created a scrapy Selector object using a string with the html code
# The selector sel has selected the entire html document
sel = Selector(text=html)

selector_list = sel.xpath('//p').extract()

for selector in selector_list:
    print(selector)

url_wiki = 'https://en.wikipedia.org/wiki/Web_scraping'
html = requests.get(url_wiki).content
sel = Selector(text=html.decode("utf-8"))

# use text to extract the text without the tag
selector_list_xpath = sel.xpath('//p/text()').extract()

# for selector in selector_list_xpath:
#     print(selector)

# <css-to-element>::attr(attr-name)
# ie. div#uid > a::attr(href)
# <css-to-element>::attr(attr-name::text).extract to extract as text
# The CSS Wildcard You can use the wildcard * in CSS Locators too! In fact, we can use it in a similar way,
# when we want to ignore the tag type. For example:
# The CSS Locator string '*' selects all elements in the HTML document.
# The CSS Locator string '*.class-1' selects
# all elements which belong to class-1, but this is unnecessary since the string
# '.class-1' will also do the same
# job. The CSS Locator string '*#uid' selects the element with id attribute equal
# to uid, but this is unnecessary
# since the string '#uid' will also do the same job.
CSS_selector = sel.css('html > body > script:nth-of-type(1)')


def parse_pages(response):
    chapter_dict = {}
    crs_title = response.xpath('//h1[contains(@class, "title")/text()]')
    crs_title_ext = crs_title.extract_first().strip()
    ch_titles = response.css('h4.chapter__title::text')
    ch_titles_ext = [t.strip() for t in ch_titles.extract()]
    chapter_dict[crs_title_ext] = ch_titles_ext


def parse_front(response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
        yield response.follow(url=url,
                              callback=parse_pages)


def start_request(urls):
    """preload response variable from the specified url and send it to the method
    called parse"""
    for url in urls:
        yield scrapy.Request(url=url, callback=parse_front)
