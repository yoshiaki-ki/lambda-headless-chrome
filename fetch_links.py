from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def lambda_handler(event,context):
    # Headless Chromeを使うための設定を追加
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--v=99")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    # Headless Chromeを起動
    options.binary_location = "./bin/headless-chromium"
    driver = webdriver.Chrome(executable_path="./bin/chromedriver", chrome_options=options)

    # 検索ワードを取得
    keyword = ''
    for key in event:
        if keyword == '':
            keyword += event[key]
        else:
            keyword += ' ' + event[key]

    # Chromeの検索結果ページにアクセス
    driver.get('https://www.google.co.jp/search?num=10&q='+ ' '.join(keyword))

    links = []
    for counter in range(1,11):
        link = driver.find_element_by_xpath("//*[@id='rso']/div/div/div["+str(counter)+"]/div/div/div/a")
        links.append(link.get_attribute("href"))

    # ブラウザを閉じる
    driver.close()
    # Google Chrome Canaryを終了する
    driver.quit()

    return links