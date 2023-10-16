import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

'''Пока сломанно надо починить'''


def geekjob_jobs(text : str):
    # func_base = []
    url = "https://geekjob.ru/vacancies?qs=" + text
    browser = webdriver.Chrome()
    
    # with open('html_for_ geekjob.html', 'r+', encoding='utf-8') as r:
    browser.get("https://geekjob.ru/vacancies?qs=" + text)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
        # r.write(html)
  
    for vacaincie in soup.find_all('li', class_ = 'collection-item avatar'):
        name = vacaincie.find('p', class_ = 'truncate company-name').text.strip()
        title = vacaincie.find('p', class_ = 'truncate vacancy-name').text.strip()
        info = vacaincie.find('div', class_ = 'info').text
        if not info:
            info = 'Не указанно'
        for i in range(len(info)):
            if info[i].isdigit():
                info = info[:i-1] + '\n      ' + info[i:]
                break
        link = 'https://geekjob.ru/' + vacaincie.a['href']
        
    
        print(f'Title: {title}\nCompany: {name}\nURL: {link}\nInfo: {info}\nSalary: Не указанна')
    # return func_base



text = 'python'
print(geekjob_jobs(text), sep = '\n')


