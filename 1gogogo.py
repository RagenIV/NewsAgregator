#!/usr/bin/env python3
#coding:utf8

import requests, re

kvo = 10 # Количество отслеживаемых слов
minlen = 5 # Минимальная длинка слов
lookat = 50

al = ''
di = {}

clear_list = ['.',',',':','»','«', '"', 'из-за', 'после']


def get_news(url, regexp):
    s = 'FIASCO'
    try:
        r = requests.get(url)
        if r.status_code == 200:
            a = (re.findall(regexp, r.text))
            s = ' '.join(a)
    except:
        pass
    return s

def clear_str(s1, li):
    s2 = s1
    for iii in li:
        s2 = s2.replace(iii,'')
    return s2.upper()

urlist = {'https://news.yandex.ru/':'data-counter=".*">(.*?)</a></h2>',
'https://news.mail.ru/?from=menu':'photo__title photo__title_new photo__title_new_hidden.*?">(.*?)</span>',
'https://ria.ru/':'<meta itemprop="name" content="(.*?)"><span',
'https://www.rbc.ru/':'<span class="news-feed__item__title">\n\ *(.*?)\n',
'http://www.vesti.ru/':'<h3 class="b-item__title"><a href=".*?">(.*?)</a> </h3>',
'https://news.rambler.ru/?utm_source=head&utm_campaign=self_promo&utm_medium=nav&utm_content=main':'data-blocks="teaser::[0987654321]+::content">\n([^><"/]*?)\n',
'https://rg.ru/':'<span class="b-link__inner-text">(.*?)</span>',
'http://www.interfax.ru':'<a href=".*?" data-vr-headline>(.*?)</a></H3></div>'}


# urlist = {


for i in urlist.keys():
    s = get_news(i,urlist[i])
    if s == 'FIASCO':
        s = get_news(i,urlist[i])
    if s != 'FIASCO':
        al += s + ' '

al = clear_str(al, clear_list)



for i in al.split():
    if len(i)>=minlen:
        if di.get(i, -1)<0:
            di[i] = 1
        else:
            di[i] = di[i] + 1
        
di['0'] = 0
ans = ['0']*(lookat +1)
for i in di.keys():
    for j in range(lookat):
        ind = lookat-j-1
        if di[i] >= di[ans[ind]]:
            ans[ind+1] = ans[ind]
            ans[ind] = i
for i in range(kvo):
    print(ans[i], ' ', di[ans[i]])
