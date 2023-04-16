from modules.EpisodeInfo import EpisodeInfo
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from time import sleep
from modules.Downloader import downloadAll
import modules.M3u8Tool as M3u8Tool
import modules.Scraping as Scraping
import requests


def get_url(s : requests.Session, url : str) -> requests.Response:
    r = s.get(url)
    if r.status_code != 200:
        raise Exception(f"Unexpected status code: {r.status_code}")
    return r

def download_ts(s: requests.Session, ts: list[str]):
    # Download first episode .ts files
    # TODO: implement some failure/retry logic  
    i = 1
    failures = []
    
    for ts_url in tqdm(episode_1):
        try:
            ts = get_url(s, ts_url)
            with open(f"ts/{i}.ts", "ab") as f:
                f.write(ts.content)
        except Exception as e:
            failures.append[(i, str(e))]
        i += 1
    return failures

def get_m3u8_content(s: requests.Session, m3u8_url: str, retries = 3) -> str:
    try:
        sleep(0.2)
        return get_url(s, m3u8_url).content.decode("utf-8")
    except Exception as e:
        if retries <= 0:
            raise Exception(f"Cannot get m3u8 content, caused by:\n {str(e)}")
        return get_m3u8_content(s, m3u8_url, retries-1)
    
    

header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    "origin": "https://v.myself-bbs.com",
    "referer": "https://v.myself-bbs.com/"
}

if __name__ == '__main__':
    s = requests.session()
    s.mount("https://", adapter = HTTPAdapter(max_retries=3))
    s.headers.update(header)
    
    print("fetching main page...")
    r = get_url(s, "https://myself-bbs.com/thread-48795-1-1.html")
    
    print("scraping episodes information...")
    episode_infos = [EpisodeInfo(i) for i in Scraping.find_episode_url_list(r.content)]
    
    print("retreving m3u8 urls...")
    # TODO make this async as well
    m3u8_urls = [f"https:{M3u8Tool.get_m3u8_url(i, header)}" for i in tqdm(episode_infos)]
    
    print("retreving m3u8 contents...")
    # m3u8_contents = [get_m3u8_content(s, url) for url in tqdm(m3u8_urls)]
    # TODO: make this prettier, segmenting batch requests of size 5
    # TODO: patch individual steps into functions
    m3u8_contents = [c.decode("utf-8") for c in downloadAll(m3u8_urls[:5])]
    m3u8_contents += [c.decode("utf-8") for c in downloadAll(m3u8_urls[5:10])]
    m3u8_contents += [c.decode("utf-8") for c in downloadAll(m3u8_urls[10:])]
    
    print("parsing m3u8 contents...")
    segment_urls: list[list[str]] = [
        M3u8Tool.process_m3u8_file(m3u8, url) 
        for m3u8 in tqdm(m3u8_contents) 
        for url in tqdm(m3u8_urls)
        ]
    
    episode_1 = segment_urls[0]
    print("grabing episode 1...")
    # failures = download_ts(s, episode_1)
    
    r = downloadAll(episode_1)
    i = 1
    for ts in r:
        if ts is Exception:
            print(f"Segment {i} failed!")
            i += 1
            continue
        with open(f"ts/{i}.ts", "ab") as f:
            f.write(ts)
        i += 1
    
    # print(len(failures))
    
    # r = get_url(s, m3u8_url)

    # with open("myvideo.ts", "wb") as f: # opening a file handler to create new file 
    #     f.write(r.content) # writing content to file