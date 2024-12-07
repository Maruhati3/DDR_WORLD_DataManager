from selenium import webdriver
from bs4 import BeautifulSoup
from load_cookie import get_page_with_cookies


def data_song_lv(session):
    allscore_url='https://p.eagate.573.jp/game/ddr/ddrworld/music/index.html?offset=0&filter=7&filtertype=0&playmode=2'
    baseallsocre_url1='https://p.eagate.573.jp/game/ddr/ddrworld/music/index.html?offset='

    baseallscore_url3=      '&filter=7&filtertype=0&playmode=2'
    csvfilename='songlv.csv'
    with open(csvfilename,'w',encoding="utf-8") as fname:
        offsetindex=0
        fname.write("曲名;アーティスト名;bSP;BSP;DSP;ESP;CSP;BDP;DDP;EDP;CDP\n")
        #初回だけlen(alltr)の値を取得するためにwhileの外で実行
        index_url=baseallsocre_url1+str(offsetindex)+baseallscore_url3      
        print('='*50)
        response = session.get(index_url)
        print("取得したデータ一覧:")
        print(index_url)
        print(response.url)
        soup=BeautifulSoup(response.content,'lxml')
        alltr=soup.find_all("tr",class_="data")
            
        while len(alltr)!=0:
            
            print(len(alltr))
            for songindex in range(len(alltr)):
                alltd=alltr[songindex].find_all("td")
                #print(alltd)
                Songname=alltd[1].text
                Artistname=alltd[2].text
                print("曲名:",Songname)
                print("アーティスト名:",Artistname)
                bSP=alltd[3].text
                BSP=alltd[4].text
                DSP=alltd[5].text
                ESP=alltd[6].text
                CSP=alltd[7].text
                BDP=alltd[8].text
                DDP=alltd[9].text
                EDP=alltd[10].text
                CDP=alltd[11].text
                fname.write(f"{Songname};{Artistname};{bSP};{BSP};{DSP};{ESP};{CSP};{BDP};{DDP};{EDP};{CDP}\n")
            offsetindex+=1

            index_url=baseallsocre_url1+str(offsetindex)+baseallscore_url3
            print('='*50)
            response = session.get(index_url)
            print("取得したデータ一覧:")
            print(index_url)
            print(response.url)
            soup=BeautifulSoup(response.content,'lxml')
            alltr=soup.find_all("tr",class_="data")
                        
            



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




