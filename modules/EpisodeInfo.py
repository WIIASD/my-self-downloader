import re
class EpisodeInfo:
    def __init__(self, url : str) -> None:
        self.original_url = url
        self.info = self.parse_url(url)
        self.valid_url = True
        if self.info["tid"] == "" and self.info["vid"] == "" and self.info["id"] == "":
            self.valid_url = False
        pass
    
    def __str__(self) -> str:
        return (
            f"EpisodeInfo: "
            f"{{ 'tid': '{self.info['tid']}', "
            f"'vid': '{self.info['vid']}', "
            f"'id': '{self.info['id']}', "
            f"'original_url': '{self.original_url}'}}"
            f"'valid_url': '{self.valid_url}'"
        )
    
    def __repr__(self):
        return str(self)
    
    def parse_url(self, url : str) -> dict:
        # https://v.myself-bbs.com/player/play/48795/001
        re_search_1 = re.search("play/(\d+)/(\d+)", str(url))
        # https://v.myself-bbs.com/player/AgADKggAArTNsVQ
        re_search_2 = None if re_search_1 else re.search("player/(.+)", str(url))
        
        dict = {
            "tid" : "" if not re_search_1 else re_search_1.group(1),
            "vid" : "" if not re_search_1 else re_search_1.group(2),
            "id" : "" if not re_search_2 else re_search_2.group(1)
        }
        
        return dict