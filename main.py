from bs4 import BeautifulSoup
import requests
import os
from twilio.rest import Client

account_sid = "AC00feed0d53f15aca041d0f7107f189ae"
auth_token = os.environ.get("AUTH_TOKEN_TWILIO")

url = "https://www.amazon.co.uk/Keter-Factor-Outdoor-Plastic-Storage/dp/B00AFSU05C/ref=sr_1_1_sspa?crid=VTT3F4NQHJ5Z&keywords=keter+shed&qid=1664885420&qu=eyJxc2MiOiI1Ljk1IiwicXNhIjoiNS4yNiIsInFzcCI6IjQuMDAifQ%3D%3D&sprefix=keter%2Caps%2C141&sr=8-1-spons&psc=1"

browser_header = {
    "Accept-Language": "en-GB,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
}

response = requests.get(url=url, headers=browser_header)
site_data = response.text

soup = BeautifulSoup(site_data, "lxml")

price = int(soup.find(name="span", class_="a-price-whole").get_text().strip("."))

if price < 605:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"You're shed is cheaper today, {price}. \n{url}",
        from_='+16507694295',
        to='+447960879066'
    )