import unittest
import os
import modules.M3u8Tool as M3u8Tool
from unittest.mock import Mock

CURRENT_DIR = os.path.dirname(__file__)
M3U8_FILES = [open(os.path.join(CURRENT_DIR, f"m3u8/{i}.m3u8"), "rb").read().decode("utf-8") for i in range(1,3)]
M3U8_URLS = m3u8_urls = [
        'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/index.m3u8', 
        'https://vpx08.myself-bbs.com/vpx/48795/001/720p.m3u8',
        ]
EXPECTED_1 = [
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0000.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0001.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0002.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0003.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0004.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0005.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0006.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0007.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0008.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0009.ts', 
    'https://vpx32.myself-bbs.com/hls/PQ/cA/Ap/AgADPQcAApoxyVU/0010.ts'
    ]
EXPECTED_2 = [
    'https://vpx08.myself-bbs.com/vpx/48795/001/0000.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0001.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0002.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0003.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0004.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0005.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0006.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0007.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0008.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0009.ts', 
    'https://vpx08.myself-bbs.com/vpx/48795/001/0010.ts'
    ]

class M3u8ToolTest(unittest.TestCase):
    
    def test_process_m3u8_file(self):
        ts_results = [M3u8Tool.process_m3u8_file(m3u8, urls) for m3u8 in M3U8_FILES for urls in M3U8_URLS]
        self.assertEqual(ts_results[0], EXPECTED_1)
        self.assertEqual(ts_results[1], EXPECTED_2)
        return
    
    def test(self):
        mockWebSocket = Mock()
        mockWebSocket.recv.return_value = "kasdjflkasjdkfjas"
        
        ws = Mock()
        ws.create_connection.return_value = mockWebSocket
        
        print(ws.create_connection().recv())


if __name__ == '__main__':
    unittest.main()