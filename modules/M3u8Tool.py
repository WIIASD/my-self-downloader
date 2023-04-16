from websocket import create_connection
from contextlib import closing
from modules.EpisodeInfo import EpisodeInfo
import json
import re

def get_m3u8_url(episode_info : EpisodeInfo, header: dict) -> str:
    with closing(create_connection("wss://v.myself-bbs.com/ws", header = header)) as ws:
        ws.send(
            json.dumps(
                {
                    "tid": episode_info.info["tid"], 
                    "vid": episode_info.info["vid"], 
                    "id": episode_info.info["id"]
                }
            )
        )
        recv = json.loads(ws.recv())
        return recv["video"]
    
def process_m3u8_file(m3u8: str, m3u8_url: str) -> list[str]:
    # Example:
    # process https://vpx49.myself-bbs.com/hls/wQ/gA/Ah/AgADwQgAAhk5WVc/index.m3u8 and a m3u8 file
    # to a list of urls similar to this form:
    # https://vpx49.myself-bbs.com/hls/wQ/gA/Ah/AgADwQgAAhk5WVc/0103.ts
    url_prefix = re.search("(^(.+?)/)[^/]*\.m3u8", str(m3u8_url))
    if url_prefix == None:
        return []
    return [
        f"{url_prefix.group(1)}{file_name}" 
        for 
        file_name 
        in 
        list(filter(lambda s: len(s) > 0 and s[0].isdigit(), m3u8.split("\n")))
        ]