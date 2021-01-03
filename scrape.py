import requests
import json
import os
import argparse
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

parser = argparse.ArgumentParser()

parser.add_argument('-p', '-playlist', type=str, default="playlist.m3u8", help='Playlist file in the .m3u8 format.')
parser.add_argument('-f', '-final_track_name', type=str, default="MADEON_SET.mp3", help='Final track name.')

args = parser.parse_args()

playlist_file = args.p
final_track_name = args.f

if __name__ == '__main__':

  # headers = {
  #   "Accept": "*/*",
  #   "Accept-Encoding": "gzip, deflate, br",
  #   "Accept-Language": "en-US,en;q=0.9",
  #   "Cache-Control": "no-cache",
  #   "Connection": "keep-alive",
  #   "Host": "cf-hls-media.sndcdn.com",
  #   "Origin": "https://soundcloud.com",
  #   "Pragma": "no-cache",
  #   "Referer": "https://soundcloud.com/",
  #   "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
  #   "sec-ch-ua-mobile": "?0",
  #   "Sec-Fetch-Dest": "empty",
  #   "Sec-Fetch-Mode": "cors",
  #   "Sec-Fetch-Site": "cross-site",
  #   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
  # }

  final_track = None
  count = 1
  with open(playlist_file, 'r') as playlist:
    for line in playlist:
      if line.startswith('https://'):
        res = None
        try:
          res = requests.get(line.strip()) 
        except Exception as e:
          print("SOMETHING FAILED LMAO")
        print(f"Downloading snippet {count}...")
        if res.ok:
          snippet = AudioSegment.from_mp3(BytesIO(res.content))
          if final_track:
            final_track += snippet
          else:
            final_track = snippet
        count += 1
  
  print("\nExporting final track...")
  final_track.export(final_track_name, format="mp3")
  print("\nDone!")
