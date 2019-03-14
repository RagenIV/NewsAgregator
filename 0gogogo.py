#!/usr/bin/env python3
#coding:utf8

import requests, re

kvo = 10 # Количество отслеживаемых слов
minlen = 5 # Минимальная длинка слов

al = ''
di = {}

clear_list = ['.',',',':','»','«']


def get_news(url, regexp):
    r = requests.get(url)
    s = 'FIASCO'
    if r.status_code == 200:
        a = (re.findall(regexp, r.text))
        s = ' '.join(a)
    return s

def clear_str(s1, li):
    s2 = s1
    for iii in li:
        s2 = s2.replace(iii,'')
    return s2

urlist = {'https://news.yandex.ru/':'data-counter=".*">(.*?)</a></h2>', 'https://news.mail.ru/?from=menu':'photo__title photo__title_new photo__title_new_hidden.*?">(.*?)</span>'}

for i in urlist.keys():
    s = get_news(i,urlist[i])
    if s == 'FIASCO':
        s = get_news(i,urlist[i])
    if s != 'FIASCO':
        al += s + ' '

al = clear_str(al, clear_list)

'''
r = requests.get('https://news.mail.ru/?from=menu ')
if r.status_code == 200:
    #print(r.text)

    al += (re.findall('photo__title photo__title_new photo__title_new_hidden.*?">(.*?)</span>', r.text))
    for i in " ".join(al).replace('.','').replace(',','').replace(':','').replace('»','').replace('«','').split():
        if len(i)>4:
            if di.get(i, -1)<0:
                di[i] = 1
            else:
                di[i] = di[i] + 1

'''

# <meta itemprop="name" content="(.*?)"><span
for i in al.split():
    if len(i)>=minlen:
        if di.get(i, -1)<0:
            di[i] = 1
        else:
            di[i] = di[i] + 1
        
di['0'] = 0
ans = ['0']*(kvo +1)
for i in di.keys():
    for j in range(kvo):
        ind = kvo-j-1
        if di[i] >= di[ans[ind]]:
            ans[ind+1] = ans[ind]
            ans[ind] = i
for i in range(kvo):
    print(ans[i], ' ', di[ans[i]])
