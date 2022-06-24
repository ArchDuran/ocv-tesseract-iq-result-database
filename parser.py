import urllib
import urllib.request
import asyncio

url = "https://amthauer-ist.com/graph.php?id="
path_to_file = "./images/img"

def downloader(tries):
    for i in range(1, tries + 1):
        urllib.request.urlretrieve(url + str(i), path_to_file + str(i))