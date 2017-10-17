# import libraries
import re
import sys
import urllib2
from bs4 import BeautifulSoup

base_page   = 'https://forum.femina.mk/'
start_page   = 'https://forum.femina.mk/forums/%D0%A4%D0%B8%D0%BB%D0%BC%D0%BE%D0%B2%D0%B8.52'

threads = []
threads_with_comments = []

def getNumberOfPages(main_page_url):
    try:
        page = urllib2.urlopen(main_page_url)
        soup = BeautifulSoup(page, 'html.parser')
        PageNav = soup.find_all('div', attrs={'class': 'PageNav'})
        return int(PageNav[0]["data-last"])
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return 0

def parsePage(page_url):
    try:
        page = urllib2.urlopen(page_url)
        soup = BeautifulSoup(page, 'html.parser')
        discussionListItems =  soup.find_all('li', attrs={'class':'discussionListItem'})
        for discussionListItem in discussionListItems:
            discussionListItemTitle=discussionListItem.find('h3', attrs={'class':'title'}).text
            discussionListItemUrl = discussionListItem.find('h3', attrs={'class': 'title'}).find('a')
            discussionListItemHref = discussionListItemUrl['href']
            # print discussionListItemTitle
            threads.append([discussionListItemTitle,  discussionListItemHref])

        return threads
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return []

def getTotalThreadCommentsPages(thread_url):
    try:
        thread_page = urllib2.urlopen(thread_url)
        thread_page_soup = BeautifulSoup(thread_page, 'html.parser')
        PageNav = thread_page_soup.find_all('div', attrs={'class': 'PageNav'})
        if len(PageNav) > 0:
            return int(PageNav[0]["data-last"])
        else:
            return  0
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return 0

def parseThreadPage(thread_url):
    try:
        thread_page = urllib2.urlopen(thread_url)
        thread_page_soup = BeautifulSoup(thread_page, 'html.parser')\

        thread_messages = thread_page_soup.find_all('li', attrs={'class': 'message'})
        thread_messages_text = []
        for thread_message in thread_messages:
            messageContent = thread_message.find('div', attrs={'class': 'messageContent'})

            # remove bbCodeBlock blocks
            for bbCodeBlock in messageContent.findAll('div', attrs={'class': 'bbCodeBlock'}):
                bbCodeBlock.extract()
            # print messageContent.text
            thread_messages_text.append(['Comment', messageContent.text])
        return thread_messages_text
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return []

number_of_pages = getNumberOfPages(start_page)

for i in range(1, number_of_pages + 1):
    current_page_url = start_page +"/page-"+ str(i)
    print 'page_url=', current_page_url
    current_page_threads = parsePage(current_page_url)

    for thread in  current_page_threads:
        print 'thread_title=', thread[0]

        base_thread_url = base_page + thread[1]
        print 'base_thread_url=', base_thread_url
        base_thread_total_pages = getTotalThreadCommentsPages(base_thread_url)
        print 'total_thread_pages=', base_thread_total_pages

        # print 'total_thread_comments_pages', total_thread_pages
        thread_comments = []
        start_from = 0 if base_thread_total_pages == 0 else 1

        for j in range(start_from , base_thread_total_pages + 1):
          thread_url = base_thread_url;
          if(j > 1):
              thread_url =thread_url  +"page-"+ str(j)
          print 'thread_page_url=', thread_url
          thread_page_comments = parseThreadPage(thread_url)
          thread_comments.append(thread_page_comments)

        threads_with_comments.append([thread, thread_comments])

print '--------------------------------------------------------------------------'

for threads_with_comment in threads_with_comments:
    thread = threads_with_comment[0]
    comments= threads_with_comment[1]
    print thread[0]
    for comment in comments:
        print comment

# write to file
import io, json
with io.open('femina_mk.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(threads_with_comments, ensure_ascii=False))