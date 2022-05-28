import random
import urllib.parse
from time import sleep

from bs4 import BeautifulSoup
import requests

"""
A simple scrape script that downloads the entire office script hosted on a fan site.
"""

weburl = 'https://transcripts.foreverdreaming.org/'


def scrape_transcript(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("title").text.replace("/", ",")

    f = open(f"output/{title}.txt", "w")

    sleep(1)

    transcript_parent_div = soup.find("div", {"class": "boxbody"})
    tags = transcript_parent_div.find("div").find("div").find("div").findAll(["p", "hr"])
    for tag in tags:
        if tag.name == "hr":
            f.write("---\n")
        else:
            f.write(tag.text + "\n")


if __name__ == '__main__':
    parent_pages = [
        "https://transcripts.foreverdreaming.org/viewforum.php?f=574",
        "https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=3f0020ceecc00206bd91f802c774380f&start=25",
        "https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=3f0020ceecc00206bd91f802c774380f&start=50",
        "https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=3f0020ceecc00206bd91f802c774380f&start=75",
        "https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=3f0020ceecc00206bd91f802c774380f&start=100",
        "https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=3f0020ceecc00206bd91f802c774380f&start=125",
        "https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=3f0020ceecc00206bd91f802c774380f&start=150",
        "https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=3f0020ceecc00206bd91f802c774380f&start=175",
    ]

    for parent in parent_pages:
        print(f"scraping {parent}")
        sleep(random.normalvariate(11,3))
        page = requests.get(parent)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll("a", href=True)

        for link in links:
            if link.text.find("x") == 2:
                print(f"scraping {link}")
                sleep(random.normalvariate(11, 3))
                scrape_transcript(urllib.parse.urljoin(weburl,link['href']))
