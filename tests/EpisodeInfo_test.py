import unittest
from modules.EpisodeInfo import EpisodeInfo

URL1 = "https://v.myself-bbs.com/player/play/48795/001\n"
URL2 = "https://v.myself-bbs.com/player/AgADKggAArTNsVQ\n"

class EpisodeInforTests(unittest.TestCase):
    def test_parse_url(self):
        """
        url example: 
        1. https://v.myself-bbs.com/player/play/48795/001
            - tid = "48795"
            - vid = "001"
            - id = ""
        2. https://v.myself-bbs.com/player/AgADKggAArTNsVQ
            - tid = ""
            - vid = ""
            - id = "AgADKggAArTNsVQ"
        """
        i1 = EpisodeInfo(URL1)
        i2 = EpisodeInfo(URL2)
        expected_info1 = {
            "tid" : "48795",
            "vid" : "001",
            "id" : ""
        }
        expected_info2 = {
            "tid" : "",
            "vid" : "",
            "id" : "AgADKggAArTNsVQ"
        }
        self.assertEqual(i1.info, expected_info1)
        self.assertEqual(i2.info, expected_info2)
        self.assertEqual(i1.valid_url, True)
        self.assertEqual(i2.valid_url, True)


if __name__ == '__main__':
    unittest.main()