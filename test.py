from urllib import request
from bs4 import BeautifulSoup 
import numpy as np
import time

fs = open("data.txt","r")   #设置文件对象
urls = fs.readlines()  #直接将文件中按行读到list里
fs.close()

for url in urls:
    #url = "http://jwc.henu.edu.cn/jwzl/xszl.htm" 
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    page = request.Request(url,headers=headers) 
    page_info = request.urlopen(page).read().decode('utf-8')

    # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
    soup = BeautifulSoup(page_info, 'html.parser')

    titles = soup.find_all('td', 'tit1')# 查找所有td标签中class='tit1'的语句


    with open(r"test.txt","w") as file:
    
        for title in titles:
            print(title.text)
        
            file.write(title.text+'\n')
    time.sleep(2)
