from selenium import webdriver
from bs4 import BeautifulSoup
from load_cookie import get_page_with_cookies


def data_song_lv(session):
    allscore_url='https://bemaniwiki.com/?DanceDanceRevolution+WORLD/%C1%B4%B6%CA%C1%ED%A5%CE%A1%BC%A5%C4%BF%F4%A5%EA%A5%B9%A5%C8#ACSN'
    csvfilename='songnotes.csv'
    with open(csvfilename,'w',encoding="utf-8") as fname:
        offsetindex=0
        fname.write("曲名;bSP;BSP;DSP;ESP;CSP;BDP;DDP;EDP;CDP\n")
        #ページ全体のtd一覧にwhileの外で実行
        index_url=allscore_url
        print('='*50)
        response = session.get(index_url)
        print("取得したデータ一覧:")
        print(index_url)
        print(response.url)
        soup=BeautifulSoup(response.content,'lxml')
        alltr=soup.find_all("tr")
            
        for trlist in alltr:
            print(str(len(trlist))+"\n")
            if len(trlist)>=10:
                    
                alltd=trlist.find_all("td")
                #print(alltd)
                Songname=alltd[0].text
                print("曲名:",Songname)
                bSP=alltd[1].text
                BSP=alltd[2].text
                DSP=alltd[3].text
                ESP=alltd[4].text
                CSP=alltd[5].text
                BDP=alltd[6].text
                DDP=alltd[7].text
                EDP=alltd[8].text
                CDP=alltd[9].text
                fname.write(f"{Songname};{bSP};{BSP};{DSP};{ESP};{CSP};{BDP};{DDP};{EDP};{CDP}\n")
                       
            



options = webdriver.ChromeOptions()


# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')

# Requestsのセッションを作成
#session = requests.Session()

# Seleniumから取得したクッキーをRequestsのセッションにセット
#for cookie in selenium_cookies:
#    session.cookies.set(cookie['name'], cookie['value'])

#cookieをセット
session=get_page_with_cookies('./cookie.pkl')
# Requestsでデータを操作
target_url = 'https://p.eagate.573.jp/game/ddr/ddrworld/top/index.html'
flare_url =  'https://p.eagate.573.jp/game/ddr/ddrworld/playdata/flare_data_single.html'
status_url=  'https://p.eagate.573.jp/game/ddr/ddrworld/playdata/index.html'


data_song_lv(session)

'''
print('='*50)
response = session.get(target_url)
print("取得したデータtop:")
print(target_url)
print(response.url)
file=open('result.html','w')
file.write(str(BeautifulSoup(response.content,"html.parser")))
file.close()
print('='*50)


response= session.get(status_url)
print("取得したデータstatus:")
print(status_url)
print(response.url)
response= session.get(status_url)
file2=open('result2.html','w')
file2.write(str(BeautifulSoup(response.content,"html.parser")))
file2.close()

response= session.get(flare_url)
print("取得したデータflare:")
print(flare_url)
print(response.url)
response= session.get(flare_url)
file3=open('result3.html','w')
file3.write(str(BeautifulSoup(response.content,"html.parser")))
file3.close()

'''





# ブラウザを終了




