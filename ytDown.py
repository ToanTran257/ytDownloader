from subprocess import call
from bs4 import BeautifulSoup
import urllib.request

f = open("music.txt", "r")

for x in f:
    # take in "text" -> URL
    textToSearch = x

    if "https://" not in x:
        print("Looking up " + x)
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        URL = 'https://www.youtube.com' + soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]['href']
        command = "youtube-dl -o .\\saveFold\\%(title)s.%(ext)s -f bestaudio/best --extract-audio --audio-format mp3 --no-playlist " + URL
        call(command.split(), shell=False)