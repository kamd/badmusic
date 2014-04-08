__author__ = 'Keir MacDonald'
__license__ = 'GPLv3'

import sys
import os
import fnmatch
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.asf import ASF
from mutagen.mp4 import MP4

LOW_BITRATE = 128


def get_music_files(path):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for suffix in ['mp3', 'wma', 'm4a']:
            for filename in fnmatch.filter(filenames, '*.' + suffix):
                matches.append(os.path.join(root, filename))
    return matches


def get_music_info(path):
    if path.endswith('mp3'):
        id3 = EasyID3(path)
        return MP3(path).info.bitrate / 1000, id3['artist'][0], id3['album'][0]
    if path.endswith('wma'):
        wma = ASF(path)
        return wma.info.bitrate / 1000, wma['Author'][0], wma[u'WM\AlbumTitle'][0].value
    if path.endswith('m4a'):
        mp4 = MP4(path)
        return mp4.info.bitrate / 1000, mp4.tags['\xa9ART'][0], mp4.tags['\xa9alb'][0]
    raise AssertionError


directory = os.curdir
if len(sys.argv) > 1:
    directory = sys.argv[1]

low_quality_albums = set()
for filename in get_music_files(directory):
    try:
        bitrate, artist, album = get_music_info(filename)
        if bitrate <= LOW_BITRATE:
            low_quality_albums.add((artist, album))
    except:
        continue

for artist, album in low_quality_albums:
    print artist, ' | ', album
