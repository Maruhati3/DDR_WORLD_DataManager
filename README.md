# DDR_WORLD_DataManager

## 参加者: mixik

## 備考: 
### 2024/11/30 mixik
参考にしたサイト(seleniumの隠蔽): https://www.zenrows.com/blog/selenium-stealth#limitations-and-alternatives

### 2024/12/01 mixik
フレアスキル対象曲を取得するスクリプトfetch_flare2.pyを作成  
* 同様の操作をするfetch_flare.py(+ flare_output.py)よりも高速
    * fetch_flare.py: seleniumによる実装
    `1.08s user 0.63s system 15% cpu 11.022 total`
    * fetch_flare2.py: requests&Beautifulsoupによる実装
    `0.20s user 0.04s system 7% cpu 3.410 total`