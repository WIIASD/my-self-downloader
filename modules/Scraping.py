from bs4 import BeautifulSoup
from bs4 import element

def find_myself_episode_url(i: element.Tag) -> str:
    # myself-bbs
    r = i.find("a", {"class": "various fancybox.iframe", "data-href": lambda s: "myself-bbs" in s}, )
    return r["data-href"]

def find_episode_url_list(main_page_html : str) -> list[str]:
    soup = BeautifulSoup(main_page_html, "html5lib")
    ul = soup.find("ul", {"class": "main_list"})
    li = ul.findAll("li", recursive=False)
    urls = [find_myself_episode_url(i) for i in li]
    return urls