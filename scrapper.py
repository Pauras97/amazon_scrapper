import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.amazon.com/dp/B072MHN91T/?coliid=ILVKVKWWEKMQT&colid=N074BLNAI2M6&psc=1&ref_=lv_ov_lig_dp_it"

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"}

def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = float(soup.find(id="priceblock_ourprice").get_text()[1:6])
    #con = float(price[1:6])
    if price < 100.0:
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("paurasjadhav@gmail.com", "uieuhfarpkvttsxs")

    subject = "Apple Keyboard Price Drop!!!"
    body = "Check the Amazon Link https://www.amazon.com/dp/B072MHN91T/?coliid=ILVKVKWWEKMQT&colid=N074BLNAI2M6&psc=1&ref_=lv_ov_lig_dp_it"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "paurasjadhav@gmail.com",
        "pauras2497@gmail.com",
        msg
    )
    print("EMAIL SENT")

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)