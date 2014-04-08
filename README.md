badmusic
========

Simple program that detects low bitrate music in a directory.

Rather simplistic, currently assumes that anything 128kbps or lower is low bitrate, regardless of format.
Supports the following formats: mp3, m4a, wma. Will not pick up files without those suffixes.
If it has any problems determining bitrate or other details, it will ignore that file and continue.

Usage
-----

python badmusic/bad_music_finder.py /example/music > lowqualityalbums.txt


Output
------

Directly to standard output, a list of low-quality albums in the format 'Artist  |  Album'
e.g.

Ladytron  |  Witching Hour<br/>
Neutral Milk Hotel  |  In The Aeroplane Over The Sea<br/>
The Go! Team  |  Thunder, Lightning, Strike<br/>
