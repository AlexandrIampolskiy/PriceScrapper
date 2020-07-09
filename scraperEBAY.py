import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.ebay.de/itm/Apple-iPhone-11-Pro-Max-512GB-Nachtgrun-Green-Ohne-Simlock-A2218-MWHR2ZD-A-Neu/113922762393?epid=7034220560&hash=item1a86536699:g:oVEAAOSwDHRdjLbH'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find(id="itemTitle").get_text().strip()
    price = soup.find(id="prcIsum").get_text()
    converted_price = float(price[4:9])

    if(converted_price > 1.000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('scrapermessage@gmail.com', 'siemmfkhkgqairyj')

    subject = 'Price fell down!!!'
    body = 'Check the Ebay link https://www.ebay.de/itm/Apple-iPhone-11-Pro-Max-512GB-Nachtgrun-Green-Ohne-Simlock-A2218-MWHR2ZD-A-Neu/113922762393?epid=7034220560&hash=item1a86536699:g:oVEAAOSwDHRdjLbH'
    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'scrapermessage@gmail.com', 'sask06823t@gmail.com', msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()
check_price()
# while(True):
#     check_price()
#     time.sleep(60)





