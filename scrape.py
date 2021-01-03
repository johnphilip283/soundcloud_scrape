import requests
import json
import os
import argparse
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

parser = argparse.ArgumentParser()

parser.add_argument('-p', '-playlist', required=True, type=str, help='Playlist file in the .m3u8 format.')
parser.add_argument('-f', '-final_track_name', required=True, type=str, help='Final track name.')

args = parser.parse_args()

playlist_file = args.p
final_track_name = args.f

if __name__ == '__main__':

  final_track = None
  count = 1
  with open(playlist_file, 'r') as playlist:
    for line in playlist:
      if line.startswith('https://'):
        res = requests.get(line.strip())
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
