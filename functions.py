from lyricsgenius import Genius
import json
import re

with open("apikeys.json") as fp:
    keys=  json.load(fp)
genius = Genius(keys['genius']['token'])



def format_lyrics(s: str):
    pos = s.find('[')
    s = s[pos:]

    # replace junk words
    s=s.replace("You might also like","")
    s=s.replace("[Music Video]","")
    if s.endswith("Embed"):
        s= s[:-len("Embed")]
    s = re.sub(r'\d+$', '', s)

    # needed for st.write
    s = s.replace("\n", "  \n")
    return s

def get_lyrics(song_name, artist=""):
    song = genius.search_song(title=song_name, artist=artist)
    return format_lyrics(song.lyrics)

def split_lyrics(lyrics: str):
    pattern = re.compile(r'(\[[^\]]+\])([^[]*)')
    matches = pattern.findall(lyrics)
    result = [(label.strip(), text.strip()) for label, text in matches]
    
    return result
    