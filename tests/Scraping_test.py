from modules.Scraping import find_episode_url_list
import unittest
import os

CURRENT_DIR = os.path.dirname(__file__)
HTML_FILES = [open(os.path.join(CURRENT_DIR, f"html/1.html"), "rb").read().decode("utf-8")]
EXPECTED_URLS = [
    'https://v.myself-bbs.com/player/AgADPQcAApoxyVU\n', 
    'https://v.myself-bbs.com/player/play/48795/001\n', 
    'https://v.myself-bbs.com/player/play/48795/002\n', 
    'https://v.myself-bbs.com/player/play/48795/003\n', 
    'https://v.myself-bbs.com/player/play/48795/004\n', 
    'https://v.myself-bbs.com/player/play/48795/005\n', 
    'https://v.myself-bbs.com/player/AgADJQcAAhx7WFQ\n', 
    'https://v.myself-bbs.com/player/AgADJgcAAhx7WFQ\n', 
    'https://v.myself-bbs.com/player/AgAD6QcAAhGfAAFV\n', 
    'https://v.myself-bbs.com/player/AgAD2wcAAksgAAFV\n', 
    'https://v.myself-bbs.com/player/AgAD6gcAAvZ5sVQ\n', 
    'https://v.myself-bbs.com/player/AgAD-QcAAibiQFU\n', 
    'https://v.myself-bbs.com/player/AgADKgoAAqV-2VU\n', 
    'https://v.myself-bbs.com/player/AgADYggAAkVdoVU\n'
    ]

class ScrapingTest(unittest.TestCase):
    
    def test_find_episode_url_list(self):
        self.assertEqual(find_episode_url_list(HTML_FILES[0]), EXPECTED_URLS)
        pass    
    
    
if __name__ == '__main__':
    unittest.main()