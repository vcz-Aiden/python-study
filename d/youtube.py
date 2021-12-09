import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

data_list = []
driver.get("https://www.youtube.com/watch?v=qZ2HqUuIjKc")

body = driver.find_element_by_tag_name('body')
last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(5)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")


    print('scrolling ', new_page_height, " / ", last_page_height)

    if (new_page_height == last_page_height):
        break

    last_page_height = new_page_height

print('end')
html0 = driver.page_source
html = BeautifulSoup(html0, 'html.parser')
comments_list = html.findAll('ytd-comment-thread-renderer', {'class': 'style-scope ytd-item-section-renderer'})

for j in range(len(comments_list)):
    comment = comments_list[j].find('yt-formatted-string', {'id': 'content-text'}).text
    comment = comment.replace('\n', '')
    comment = comment.replace('\t', '')

    youtube_id = comments_list[j].find('a', {'id': 'author-text'}).span.text
    youtube_id = youtube_id.replace('\n','')
    youtube_id = youtube_id.replace('\t', '')
    youtube_id = youtube_id.strip()

    raw_date = comments_list[j].find('yt-formatted-string', { 'class': 'published-time-text above-comment style-scope ytd-comment-renderer'})
    date = raw_date.a.text
    try:
        like_num = comments_list[j].find('span', {'id': 'vote-count-middle', 'class': 'style-scope ytd-comment-action-buttons-renderer', 'aria-label': re.compile('좋아요')}).text
        like_num = like_num.replace('\n', '')
        like_num = like_num.replace('\t', '')
        like_num = like_num.strip()
    except:
        like_num = 0

    data = {'comment': comment, 'youtube_id': youtube_id, 'date': date, 'like_num': like_num}
    data_list.append(data)

result_df = pd.DataFrame(data_list, columns=['comment','youtube_id','date','like_num'])
result_df.to_excel('comment_youtube3.xlsx', index=False)
driver.close()


