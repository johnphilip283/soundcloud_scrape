import requests
import json
import os
from pydub import AudioSegment
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-o', '-output', type=str, required=True, default="MADEON" help='Output folder for mp3 snippets.')
parser.add_argument('-p', '-playlist', type=str, required=True, default="playlist.m3u8", help='Playlist file in the .m3u8 format.')
parser.add_argument('-f', '-final_track_name', type=str, required=True, default="MADEON_SET.mp3", help='Final track name.')

print(parser.parse_args())

import sys
sys.exit()

args = parser.parse_args()

FOLDER_NAME = 'MADEON'

if __name__ == '__main__':
  
  folder = os.path.join(os.getcwd(), FOLDER_NAME)

  if not os.path.exists(folder):
    os.mkdir(folder)

  headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "cf-hls-media.sndcdn.com",
    "Origin": "https://soundcloud.com",
    "Pragma": "no-cache",
    "Referer": "https://soundcloud.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
  }

  final_track = None
  count = 1
  with open('playlist.m3u8', 'r') as playlist:
    for line in playlist:
      if line.startswith('https://'):
        with open(f"{folder}/{count}.mp3", 'wb') as outfile:
          res = requests.get(line.strip(), headers=headers)
          print(f"Downloading snippet {count}...")
          if res.ok:
            outfile.write(res.content)
            snippet = AudioSegment.from_mp3(f"{folder}/{i}.mp3")
            if not final_track:
              final_track = snippet
            else:
              final_track += snippet
          count += 1
  
  beeg_song.export("MADEON_SET.mp3", format="mp3")
