# cli tool
import bs4
import sys
import json
import requests

# query sample focus to retrieve the download link from their page
LINK = sys.argv[1]
response = requests.get(LINK)
print("getting page " + str(response.status_code))

# extract the link
soup = bs4.BeautifulSoup(response.content, features="html.parser")
element = soup.find_all("div", {"class": "sample-hero-waveform-container"})[0]
data = json.loads(element.attrs["data-react-props"])
name = data["sample"]["name"]
mp3_link = data["sample"]["sample_mp3_url"]

# download sample and save it as mp3
print("downloading from " + mp3_link)
response = requests.get(mp3_link)
with open("./" + name + ".mp3", "wb") as f:
    f.write(response.content)

print("download successful")