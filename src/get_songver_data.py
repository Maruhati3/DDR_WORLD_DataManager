from selenium import webdriver
from bs4 import BeautifulSoup
from load_cookie import get_page_with_cookies

def TuneCrump(Crump):
    tmp=Crump
    if Crump=='cl_none':
        tmp='Noplay'
    elif Crump=='cl_clear':
        tmp='Clear'
    elif Crump=='cl_li4clear':
        tmp='Life4'
    elif Crump=='cl_good':
        tmp='FC'
    elif Crump=='cl_great':
        tmp='GFC'
    elif Crump=='cl_perf':
        tmp='PFC'
    else :
        tmp='MFC'
    return tmp

def data_asong(session):
    allscore_url='https://p.eagate.573.jp/game/ddr/ddrworld/playdata/music_data_single.html?offset=4&filter=7&filtertype=18&display=score'
    baseallsocre_url1='https://p.eagate.573.jp/game/ddr/ddrworld/playdata/music_data_single.html?offset='
    baseallscore_url3=      '&filter=7&filtertype='
    baseallscore_url5=      '&display=score'
    baseallsocre_url_rival1='https://p.eagate.573.jp/game/ddr/ddrworld/rival/music_data_single.html?offset='
    baseallscore_url_rival3= '&filter=0&filtertype=0&display=score&rival_id=71393284'
    #offset:=ページ
    #filtertype:=バージョン

    csvfilename='songpage_withVer.csv'
    with open(csvfilename,'w',encoding="utf-8") as fname:
        
        fname.write("SPDP;Version;曲名;難易度;Lv;SCORE;Crank;Crump;Fskill;Frank\n")
        NumOfVer=[0,0,0,0,0, 0,0,0,1,0, 1,1,1,1,2, 2,1,2,3,4]
        for filtertypeindex in range(0,20):
            
            print('version='+str(filtertypeindex))

            #各バージョンのページを読み込み
            for offsetindex in range(0,NumOfVer[filtertypeindex]+1):
                #読み込むURLを設定
                index_url=baseallsocre_url1+str(offsetindex)+baseallscore_url3+str(filtertypeindex)+baseallscore_url5
                print('='*50)
                response = session.get(index_url)
                print("取得したデータ一覧:")
                print(index_url)
                print(response.url)
                #ページのhtml全体を取得
                soup=BeautifulSoup(response.content,'lxml')
                alltr=soup.find_all("tr",class_="data") 

                print(len(alltr))
                if len(alltr)<=0:
                    break


                for songindex in range(len(alltr)):
                    alltd=alltr[songindex].find_all("td")
                    #print("曲名:",alltd[0].find_all("a")[0].text)
                    for c in range(1,6):
                        Songname=alltd[0].find_all("a")[0].text
                        #print("曲名:",Songname)
                        Difficulty=alltd[c]['id']
                        #print("\n"+Difficulty+"="*20)
                        if alltd[c].find("a"):
                            diff=alltd[c].find("a")
                            SCORE=diff.find_all("div")[0].text
                            if SCORE=='---':
                                SCORE='0'
                            #print("SCORE: "+SCORE)
                            Crank=diff.find_all("div")[1].find("img")['src'].rsplit('/', 1)[-1].rsplit('.', 1)[0]
                            Crank=Crank.split("rank_s_")[1].replace("_p","+").replace("_m","-").upper()
                            #print("ClearRank: "+Crank)
                            Crump=diff.find_all("div")[2].find("img")['src'].rsplit('/', 1)[-1].rsplit('.', 1)[0]
                            Crump=TuneCrump(Crump)

                            #print("ClearRump:",Crump)
                            Fskill=diff.find_all("div")[3].text
                            if Fskill=='---':
                                Fskill='0'
                            #print("F-Skill:"+Fskill)
                            Frank=diff.find_all("div")[4].find("img")['src'].rsplit('/', 1)[-1].rsplit('.', 1)[0]
                            Frank=Frank.split("flare_")[1].upper()
                            #print("F-Rank:"+Frank)
                            fname.write(f"SP;{filtertypeindex};{Songname};{Difficulty};Lv;{SCORE};{Crank};{Crump};{Fskill};{Frank}\n")
                        '''
                        else:
                            print("NoSong")
                        '''
                


                        
            



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


data_asong(session)

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




